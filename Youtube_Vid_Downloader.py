import yt_dlp
import os

def manage_cookies():
    cookies_file = 'cookies.txt'
    if os.path.exists(cookies_file):
        print(f"Deleting old cookies file: {cookies_file}")
        os.remove(cookies_file)
    print("Fetching fresh cookies from the browser...")
    os.system("yt-dlp --cookies-from-browser chrome --cookies cookies.txt")

manage_cookies()

# Function to start download
def start_download():
    
    # Ask for URL
    url = input("Enter the YouTube URL: ").strip()
    if not url:
        print("Please enter a valid URL.")
        return

    # Ask for options
    print("Select download option:")
    print("1. Download Video (.mp4)")
    print("2. Download Audio (.mp3)")
    print("3. Download Subtitle")

    option = input("Enter your choice (1/2/3): ").strip()
    if option not in ["1", "2", "3"]:
        print("Invalid option. Please try again.")
        return

    # Downloading mp4 if option == 1
    ydl_opts = {}
    if option == "1":
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'outtmpl': '%(title)s.mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }
    
    # Downloading mp3 if option == 2
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
    
    # Downloading subtitle if option == 3
    elif option == "3":
        ydl_opts = {
            'writesubtitles': True,
            'subtitleslangs': ['en'],  # English subtitles
            'outtmpl': '%(title)s.%(ext)s',
            'subtitlesformat': 'srt',  # Ensure the correct subtitle format
        }

    # Show success or error message
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully.")
        print("Checking for subtitles...")
        
        # Check if subtitle exists
        if ydl_opts.get('writesubtitles'):
            subtitle_file = f"{ydl_opts['outtmpl']}.srt"  # Subtitle file should have .srt extension
            if os.path.exists(subtitle_file):
                print(f"Subtitle found: {subtitle_file}")
            else:
                print("Subtitle not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_download()
