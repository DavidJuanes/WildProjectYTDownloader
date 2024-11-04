from typing import Any
import yt_dlp

CHANNEL_URL='https://www.youtube.com/@TheWildProject/videos'
MAX_VIDEOS=10


def download_audio(url: str, output_dir: str) -> None:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def list_last_podcasts(channel_url) -> list[str]:
    ydl_opts = {
        'playlist_items': f'1-{MAX_VIDEOS}',
        'extract_flat': 'in_playlist',
    }
    podcasts_videos: list[Any] = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        for i, entry in enumerate(info['entries']):
            duration_in_minutes = entry['duration']/60
            if duration_in_minutes > 60: # We can consider it a podcast because it's a very long video
                #print(f"{i}. Title: {entry['title']}, Duration: {entry['duration']/60}")
                podcasts_videos.append(entry)
        
    return podcasts_videos

# Example usage:
videos = list_last_podcasts(CHANNEL_URL)


for video in videos:
    print(f"Title: {video['title']}, Duration: {video['duration']/60}")
    download_audio(video['url'], "output")
    