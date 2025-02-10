# temparary file, Do not run this
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