
# library
from customtkinter import *
from tkinter import filedialog, messagebox
import yt_dlp

# create a app
class App(CTk):
    def __init__(self):
        super().__init__()

        # App title
        self.title("YT Downloader")
        self.geometry("500x600")

        # URL Label and Entry
        self.label = CTkLabel(self, text="Enter video link here:")
        self.label.pack(pady=10)

        self.entry = CTkEntry(self, placeholder_text="Paste it here", width=300)
        self.entry.pack(pady=10)

        # Format Selection
        self.format_label = CTkLabel(self, text="Select format:")
        self.format_label.pack(pady=10)

        # quality option
        self.format_var = StringVar(value="mp4")
        self.mp4_radio = CTkRadioButton(self, text="MP4", variable=self.format_var, value="mp4", command=self.toggle_quality)
        self.mp4_radio.pack()
        self.mp3_radio = CTkRadioButton(self, text="MP3", variable=self.format_var, value="mp3", command=self.toggle_quality)
        self.mp3_radio.pack()

        # Quality Selection (for MP4)
        self.quality_label = CTkLabel(self, text="Select quality:")
        self.quality_label.pack(pady=10)

        # audio quality
        self.quality_var = StringVar(value="best")
        self.best_radio = CTkRadioButton(self, text="Best", variable=self.quality_var, value="best")
        self.best_radio.pack()
        self.low_radio = CTkRadioButton(self, text="Low", variable=self.quality_var, value="worst")
        self.low_radio.pack()

        # Download Button
        self.button = CTkButton(self, text="Download", command=self.download_yt)
        self.button.pack(pady=20)

        # Status Label
        self.label1 = CTkLabel(self, text="")
        self.label1.pack(pady=10)

        self.toggle_quality()

    # setting toggle quality
    def toggle_quality(self):
        if self.format_var.get() == "mp3":
            self.quality_label.pack_forget()
            self.best_radio.pack_forget()
            self.low_radio.pack_forget()
        else:
            self.quality_label.pack(pady=10)
            self.best_radio.pack()
            self.low_radio.pack()

    # Download video
    def download_yt(self):
        url = self.entry.get()
        
        # if url is not entered
        if not url:
            messagebox.showerror("Error", "URL cannot be empty")
            return

        # ask user where to save video
        output_dir = filedialog.askdirectory()
        if not output_dir:
            return

        format_choice = self.format_var.get()
        quality_choice = self.quality_var.get()

        options = {
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'noplaylist': True
        }

        if format_choice == "mp4":
            options['format'] = quality_choice
            options['writesubtitles'] = True
            options['subtitleformat'] = 'srt'
        elif format_choice == "mp3":
            options['format'] = 'bestaudio/best'
            options['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
            self.label1.configure(text="Download complete! Check the selected folder.")
        except Exception as e:
            self.label1.configure(text="An error occurred.")
            messagebox.showerror("Error", str(e))

# run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
