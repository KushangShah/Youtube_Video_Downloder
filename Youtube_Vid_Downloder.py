import customtkinter as ctk 
import yt_dlp 
import threading 
from tkinter import  filedialog, Tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Code for main program
class YoutubeDownloder(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Youtube Video/Short Downloder")
        self.geometry("500x350")
        
        # initialize function
        self.label = ctk.CTkLabel(self, text="Enter Video link:")
        self.UrlEntry = ctk.CTkEntry(self, width=400)
        self.Option_Variable = ctk.StringVar(value='Video')
        self.VideoD = ctk.CTkRadioButton(self, text='Video (.mp4)',variable=self.Option_Variable, value='Video')
        self.SongD = ctk.CTkRadioButton(self, text='Song (.mp3)',variable=self.Option_Variable, value='Song')
        self.StatusLabel = ctk.CTkLabel(self, text="Done/Error: ")
        
        # position of function
        self.label.pack(pady=10)
        self.UrlEntry.pack(pady=10)
        self.VideoD.pack(pady=10)
        self.SongD.pack(pady=10)
        self.StatusLabel.pack(pady=10)
        
    
# lunch the app
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = YoutubeDownloder()
    app.mainloop()