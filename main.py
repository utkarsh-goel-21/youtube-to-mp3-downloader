import yt_dlp
def download_audio(url):
  ydl_opts={
     'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'keepvideo':False,
        'ffmpeg_location': r'C:\Users\Utkarsh\Downloads\ffmpeg\ffmpeg-7.1.1-essentials_build\bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
  }
  with yt_dlp.YoutubeDL(ydl_opts)as ydl:
    ydl.download([url])

if __name__=="__main__":
  link=input("Enter YouTube URL: ")
  download_audio(link)