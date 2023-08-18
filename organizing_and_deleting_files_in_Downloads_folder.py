import os
import shutil
import zipfile

downloads_dir = os.path.expanduser("~/Downloads")

# Создание словаря типов файлов и соответствующих им папок 
file_types = {
    "Image": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".eps"],
    "Code": [".ipynb",".py", ".js", ".html", ".css", ".php", ".cpp", ".h", ".java"],
    "Document": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Video": [".mp4", ".avi", ".mov", ".flv", ".wmv", ".mpeg"],
    "Photoshop": [".psd"],
}

# Создание папок для каждого типа файла 
for folder_name in file_types.keys():
    folder_path = os.path.join(downloads_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Итерация по файлам в папке Downloads
for filename in os.listdir(downloads_dir):
    filepath = os.path.join(downloads_dir, filename)

# Распаковка и удаление файлов .zip 
    if filename.endswith(".zip"):
        # Проверяет, распакован ли файл 
        unzip_dir = os.path.join(downloads_dir, filename[:-4])
        if not os.path.exists(unzip_dir):
            # Распаковка файла .zip
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(downloads_dir)
        # Удаление файла .zip
        os.remove(filepath)
        print(f"Unzipped and removed {filename}")

    # Удаление файлов .torrent 
    elif filename.endswith(".torrent"):
        os.remove(filepath)
        print(f"Removed {filename}")

    # Перемещение файлов .srt в папку .subtitle внутри папки Video 
    elif filename.endswith(".srt"):
        dest_folder = os.path.join(downloads_dir, "Video", ".subtitle")
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        shutil.move(filepath, os.path.join(dest_folder, filename))
        print(f"Moved {filename} to {dest_folder}")

    # Перемещение файла в соответствующую папку в зависимости от его расширения 
    else:
        for folder_name, extensions in file_types.items():
            if any(filename.endswith(ext) for ext in extensions):
                dest_folder = os.path.join(downloads_dir, folder_name)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"Moved {filename} to {dest_folder}")
                break