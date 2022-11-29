from pathlib import Path
import os
import time
from win10toast import ToastNotifier

wait_time = 10 # wait time for the program to run in seconds (10-60 recommended)
img_ex = [".png", ".jpg", ".jpeg", ".gif"] # image extensions
vid_ex = [".mp4", ".avi", ".mov", ".wmv", ".flv", ".webm"] # video extensions
doc_ex = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf"] # document extensions
music_ex = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma"] # music extensions

home = str(Path.home())
downloads = home + '\\Downloads'

start = ToastNotifier()
start.show_toast("Segregation Started 👍", "Downloads Segregator is now running in the background.", duration=5)

while True:
    print("Running segregator...")
    try:
        os.mkdir(home + "\\Pictures\\Downloads")
    except FileExistsError:
        pass

    try:
        os.mkdir(home + "\\Videos\\Downloads")
    except FileExistsError:
        pass

    try:
        os.mkdir(home + "\\Music\\Downloads")
    except FileExistsError:
        pass

    try:
        os.mkdir(home + "\\Documents\\Downloads")
    except FileExistsError:
        pass

    files = [f for f in os.listdir(downloads) if os.path.isfile(os.path.join(downloads, f))]
    pics, docs, vids, mus, err = 0, 0, 0, 0, 0

    for file in files:
        file_name, file_extension = os.path.splitext(os.path.join(downloads, file))
        for x in img_ex:
            if x == file_extension:
                try:
                    os.rename(os.path.join(downloads, file), os.path.join(home + "\\Pictures\\Downloads", file))
                    pics += 1
                except FileExistsError:
                    err += 1
                break
        for x in vid_ex:
            if x == file_extension:
                try:
                    os.rename(os.path.join(downloads, file), os.path.join(home + "\\Videos\\Downloads", file))
                    vids += 1
                except FileExistsError:
                    err += 1
                break
        for x in doc_ex:
            if x == file_extension:
                try:
                    os.rename(os.path.join(downloads, file), os.path.join(home + "\\Documents\\Downloads", file))
                    docs += 1
                except FileExistsError:
                    err += 1
                break
        for x in music_ex:
            if x == file_extension:
                try:
                    os.rename(os.path.join(downloads, file), os.path.join(home + "\\Music\\Downloads", file))
                    mus += 1
                except FileExistsError:
                    err += 1
                break

    if (pics + docs + vids + mus + err) > 0:
        toast = ToastNotifier()
        toast.show_toast(f"Total {pics + vids + docs + mus} Downloads Organized ✨",
        "Files organized: \n"
        + ((str(pics) + " pictures\n") if pics > 0 else "")
        + ((str(vids) + " videos\n") if vids > 0 else "")
        + ((str(docs) + " documents\n") if docs > 0 else "")
        + ((str(mus) + " music\n") if mus > 0 else "")
        + ((str(err) + " errors\n") if err > 0 else ""), duration=10)
    
    print(f"Sleeping for {wait_time if wait_time > 0 else 60}s...")
    time.sleep(wait_time if wait_time > 0 else 60)
