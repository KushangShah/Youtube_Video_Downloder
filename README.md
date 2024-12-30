
<h1 align='center'>YouTube Video Downloader 🎥</h1>

---

### A simple, efficient YouTube Video Downloader created with **Python**. Easily download high-quality video, audio, or subtitles from YouTube through a user-friendly CLI interface!

---

## 🌟 Features

- **Command-Line Simplicity**: Download YouTube content directly from the terminal.
- **Video and Audio Download Options**: Choose between **MP4** video or **MP3** audio formats.
- **Subtitle Support**: Download subtitles in your preferred language (default: English).
- **Error Handling**: Validates user inputs and gracefully handles exceptions.

---

## 🛠 Installation

### 1. **Clone this repository:**
   ```bash
   git clone https://github.com/KushangShah/Youtube_Video_Downloder.git
   cd Youtube_Video_Downloder
   ```

### 2. **Set up a virtual environment** (optional but recommended):
   - **On Windows**:
     ```bash
     python -m venv ytvenv
     ytvenv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     python3 -m venv ytvenv
     source ytvenv/bin/activate
     ```

   To deactivate the virtual environment later, simply type:
   ```bash
   deactivate
   ```

### 3. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

### 4. **Install FFmpeg**:
   - **On Windows**:
     1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
     2. Extract the downloaded file and add the `bin` folder to your system's PATH.
   - **On macOS**:
     ```bash
     brew install ffmpeg
     ```
   - **On Linux** (Ubuntu/Debian):
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```

   To verify the installation, run:
   ```bash
   ffmpeg -version
   ```

### 5. **Run the script:**
   ```bash
   python3 Youtube_Vid_Downloder.py
   ```

---

## 📂 Usage

1. **Enter the YouTube URL** when prompted.
2. **Choose the desired format**:  
   - **1**: Download Video (MP4)  
   - **2**: Download Audio (MP3)  
   - **3**: Download Subtitles  
3. Follow the prompts to complete your download.
4. **Enjoy your downloaded content!**

---

## 📚 Dependencies

- `yt_dlp`: Core library for downloading YouTube content.
- `FFmpeg`: Required for audio extraction and conversion.

---

## 💡 Future Plans

- **Additional download options** (e.g., more resolutions, formats).
- **Support for downloading playlists**.
- **Enhanced error messages** for better debugging.

---

## 🤝 Contributing

Feel free to open issues, submit PRs, or suggest new features! For major changes, please discuss them with the repository maintainers beforehand.

---

## 🔒 License

This project is licensed under the MIT License. See [LICENSE](/LICENSE) for more details.

---

## Connect With Me

<p align="center">
    <a href="https://twitter.com/kushang97157764" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="kushang" height="30" width="40" /></a>
    <a href="https://linkedin.com/in/kushang-s-388959268/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="kushang" height="30" width="40" /></a>
    <a href="https://instagram.com/bhootiya.renderr/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="bhootiya.renderr" height="30" width="40" /></a>
    <a href="mailto:kushangshah41@gmail.com" target="blank"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Send Mail to Kushang" height="30" width="40" /></a>
</p>

---

Happy downloading! 🎉


### Changes made/added:

1. Simplified the description to align with the CLI-based functionality of the updated script.
2. Removed references to CustomTkinter as the current code is CLI-based.
3. Updated features to reflect the new implementation details (e.g., input validation, subtitle support).
4. Enhanced the usage section to include step-by-step instructions.
5. Minor adjustments to formatting for consistency and readability.
6. **Steps to create and activate a virtual environment** for both Windows and macOS/Linux.
7. **Detailed FFmpeg installation guide** for Windows, macOS, and Linux.
8. A verification step for FFmpeg installation.