# import customtkinter as ctk
# import yt_dlp
# import threading
# from tkinter import filedialog, Tk

# # initialize app
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("green")

# class YouTubeDownloadApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Download YouTube Video")
#         self.geometry("500x350")

#         # initialize widgets
#         self.label = ctk.CTkLabel(self, text="Enter YouTube Link:")
#         self.UrlEntry = ctk.CTkEntry(self, width=400)
#         self.OptionVariable = ctk.StringVar(value='Video')
#         self.VideoD = ctk.CTkRadioButton(self, text="Download Video (.mp4)", variable=self.OptionVariable, value="Video")
#         self.AudioD = ctk.CTkRadioButton(self, text="Download Audio (.mp3)", variable=self.OptionVariable, value="Audio")
#         self.SubtitleD = ctk.CTkRadioButton(self, text="Download Subtitle", variable=self.OptionVariable, value="Subtitle")
#         self.Button = ctk.CTkButton(self, text="DOWNLOAD", command=self.ask_directory)
#         self.StatusLabel = ctk.CTkLabel(self, text="")

#         # set positions
#         self.label.pack(pady=10)
#         self.UrlEntry.pack(pady=10)
#         self.VideoD.pack(pady=10)
#         self.AudioD.pack(pady=10)
#         self.SubtitleD.pack(pady=10)
#         self.Button.pack(pady=10)
#         self.StatusLabel.pack(pady=10)

#     def ask_directory(self):
#         self.filepath = filedialog.askdirectory()
#         if self.filepath:
#             self.Start_Download()
#         else:
#             self.StatusLabel.configure(text="Please Select a File Path", text_color='red')

#     def Start_Download(self):
#         url = self.UrlEntry.get()
#         option = self.OptionVariable.get()

#         if not url:
#             self.StatusLabel.configure(text='Please Enter a Valid URL.', text_color='red')
#             return
        
#         self.StatusLabel.configure(text='Downloading...', text_color='teal')
#         threading.Thread(target=self.Download, args=(url, option)).start()

#     def progress_hook(self, d):
#         if d['status'] == 'downloading':
#             percent = d['_percent_str']
#             eta = d['_eta_str']
#             total = d['_total_bytes_str']
#             self.StatusLabel.configure(text=f"{percent} of {total} - ETA {eta}")
#         elif d['status'] == 'finished':
#             self.StatusLabel.configure(text="Download Completed Successfully", text_color='cyan')

#     def Download(self, url, option):
#         ydl_opts = {
#             'progress_hooks': [self.progress_hook],
#             'outtmpl': f'{self.filepath}/%(title)s.%(ext)s',
#             'merge_output_format': 'mp4'  # Change this to "mkv" if you prefer MKV
#         }

#         if option == "Video":
#             ydl_opts['format'] = 'bestvideo+bestaudio'  # Ensures both video and audio are downloaded and merged

#         elif option == "Audio":
#             ydl_opts.update({
#                 'format': 'bestaudio/best',
#                 'postprocessors': [{
#                     'key': 'FFmpegExtractAudio',
#                     'preferredcodec': 'mp3',
#                     'preferredquality': '192',
#                 }]
#             })

#         elif option == "Subtitle":
#             ydl_opts.update({
#                 'writesubtitles': True,
#                 'subtitleslangs': ['en'],
#                 'skip_download': True,
#             })

#         try:
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([url])
#         except Exception as e:
#             self.StatusLabel.configure(text=f"Error: {e}", text_color='red')


# # launch the app
# if __name__ == "__main__":
#     root = Tk()
#     root.withdraw()
#     app = YouTubeDownloadApp()
#     app.mainloop()
# ----------------------------------------------------------------------------------------------------------------

# import module
import yt_dlp

# def download
def start_download():
    
    # ask for url
    url = input("Enter the YouTube URL: ").strip()
    if not url:
        print("Please enter a valid URL.")
        return

    # ask for options
    print("Select download option:")
    print("1. Download Video (.mp4)")
    print("2. Download Audio (.mp3)")
    print("3. Download Subtitle")

    option = input("Enter your choice (1/2/3): ").strip()
    if option not in ["1", "2", "3"]:
        print("Invalid option. Please try again.")
        return

    # downloading mp4 if option == 1
    ydl_opts = {}
    if option == "1":
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s'
        }
    
    # downloading mp3 if option == 2
    elif option == "2":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s'
        }
    
    # downloading subtitle if optiont == 3
    elif option == "3":
        ydl_opts = {
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'skip_download': True,
            'outtmpl': '%(title)s.%(ext)s'
        }

    # show successfully or error mssg
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_download()