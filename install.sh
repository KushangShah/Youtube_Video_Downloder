#!/bin/bash

# Install Python packages from requirements.txt
echo "Installing Python dependencies..."
pip3 install -r /Users/kushangshah/Documents/GitHub/Youtube_Video_Downloder/requirements.txt

# Install ffmpeg using Homebrew
echo "Checking for ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "ffmpeg not found. Installing..."
    brew install ffmpeg
else
    echo "ffmpeg is already installed."
fi

# Create a command alias for running the app
echo "Setting up command..."
sudo bash -c 'echo "#!/bin/bash
python3 /Users/kushangshah/Documents/GitHub/Youtube_Video_Downloder/app.py" > /usr/local/bin/youtube'
sudo chmod +x /usr/local/bin/youtube

echo "Installation complete! Run the app using 'youtube'."

