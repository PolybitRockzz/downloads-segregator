# Downloads Segregator
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

A program in Python3 which automatically segregates the downloads folder for ease of access of files.

## Features
The program loops every 10 seconds (by default) and checks if the downloads folder contains specific files and moves them to the appropriate folders.
Supported Image Files: `*.png`, `*.jpg`, `*.jpeg`, `*.gif`
Supported Video Files: `*.mp4`, `*.avi`, `*.mov`, `*.wmv`, `*.flv`, `*.webm`
Supported Document Files: `*.doc`, `*.docx`, `*.xls`, `*.xlsx`, `*.ppt`, `*.pptx`, `*.pdf`
Supported Music Files: `*.mp3`, `*.wav`, `*.aac`, `*.flac`, `*.ogg`, `*.wma`

## Installation guide
Make sure you have Git installed in your PC.
```
git clone https://github.com/polybit-tech/downloads-segregator downloads-segregator
cd downloads-segregator
pip install -r requirements.txt
python app.py
```

## Startup guide
> This step will be automated in the future. Stay tuned :)
Use the shortcut `Windows + R` to open Run dialog, and enter `shell:startup` to get startup folder.
Create a shortcut of `downloader-segregator.bat` in the startup folder.
To run the program minimized, right click on shortcut and go to `Properties > Shortcut > Run > Minimized`.

## Upcoming features
* Add support for other file types
* Automate initial startup setup
* Add optional renaming of files based on date and time