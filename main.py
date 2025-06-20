import tkinter as tk
import os
from tkinter import messagebox
import yt_dlp

ffmpeg_path=os.getenv('FFMPEG_PATH', 'ffmpeg')

def download_audio():
  url = url_entry.get().strip()
  if not url:
    messagebox.showerror("Error","Please enter a valid URL")
    return
  
  status_label.config(text="Downloading...")
  ydl_opts={
     'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'keepvideo':False,
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
  }
  try:
    with yt_dlp.YoutubeDL(ydl_opts)as ydl:
      ydl.download([url])
    status_label.config(text="Download complete!")
  except Exception as e:
    status_label.config(text="Download failed!")
    messagebox.showerror("Error",str(e))

# if __name__=="__main__":
#   link=input("Enter YouTube URL: ")
#   download_audio(link)

# GUI SETUP

root = tk.Tk()
root.title("YouTube to MP3 Downloader")
tk.Label(root,text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root,width=50)
url_entry.pack(padx=10,pady=5)
download_btn = tk.Button(root,text="Download MP3",command=download_audio)
download_btn.pack(pady=10)

status_label = tk.Label(root,text="")
status_label.pack(pady=5)

root.mainloop()