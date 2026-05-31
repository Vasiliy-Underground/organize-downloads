import os
import shutil
import datetime

# ========== НАСТРОЙКИ ==========
downloads = r"C:\Users\piree\Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".psd", ".tif", ".heic"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".htm"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi", ".msix"],
    "Games": [".iso", ".bin", ".cue", ".torrent"]
}

# Незаконченные загрузки (не трогать)
skip_extensions = [".crdownload", ".tmp", ".part", ".parts"]

# Системные файлы (не трогать)
system_files = ["desktop.ini", "Thumbs.db", "sort_log.txt"]

# ========== ФУНКЦИИ ==========
def write_log(message):
    """Записывает действие в лог-файл"""
    log_file = os.path.join(downloads, "sort_log.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def get_file_year(file_path):
    """Возвращает год последнего изменения файла"""
    mod_time = os.path.getmtime(file_path)
    return datetime.datetime.fromtimestamp(mod_time).strftime("%Y")

def create_folder_if_not_exists(path):
    """Создаёт папку, если её нет"""
    if not os.path.exists(path):
        os.makedirs(path)

def sort_existing_folders():
    """Сортирует уже разложенные файлы по папкам с годами"""
    write_log("ПРОВЕРКА СУЩЕСТВУЮЩИХ ПАПОК")
    
    for folder in folders:
        folder_path = os.path.join(downloads, folder)
        
        if not os.path.exists(folder_path):
            continue
        
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            if not os.path.isfile(file_path):
                continue
            if file in system_files:
                continue
            
            # Уже в папке с годом?
            parent = os.path.basename(folder_path)
            if parent.isdigit() and len(parent) == 4:
                continue
            
            year = get_file_year(file_path)
            target = os.path.join(folder_path, year)
            create_folder_if_not_exists(target)
            
            shutil.move(file_path, os.path.join(target, file))
            write_log(f"✅ {folder}/{file} -> {folder}/{year}/")

def sort_downloads():
    """Основная функция сортировки"""
    write_log("=" * 50)
    write_log("ЗАПУСК СОРТИРОВКИ")
    
    # 1. Сортируем уже существующие папки по годам
    sort_existing_folders()
    
    # 2. Создаём основные папки
    for folder in folders:
        path = os.path.join(downloads, folder)
        create_folder_if_not_exists(path)
    
    # 3. Сортируем новые файлы из корня Downloads
    moved_count = 0
    skipped_count = 0
    
    for file in os.listdir(downloads):
        file_path = os.path.join(downloads, file)
        
        if not os.path.isfile(file_path):
            continue
        if file in system_files:
            continue
        if any(file.lower().endswith(ext) for ext in skip_extensions):
            write_log(f"⏭ Пропущен: {file}")
            skipped_count += 1
            continue
        
        moved = False
        for folder, extensions in folders.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                year = get_file_year(file_path)
                target = os.path.join(downloads, folder, year)
                create_folder_if_not_exists(target)
                
                shutil.move(file_path, os.path.join(target, file))
                write_log(f"✅ {file} -> {folder}/{year}")
                moved_count += 1
                moved = True
                break
        
        if not moved:
            other = os.path.join(downloads, "Other")
            create_folder_if_not_exists(other)
            shutil.move(file_path, os.path.join(other, file))
            write_log(f"❓ {file} -> Other")
            moved_count += 1
    
    write_log(f"ГОТОВО! Перемещено: {moved_count}, пропущено: {skipped_count}")
    write_log("=" * 50)

# ========== ЗАПУСК ==========
if __name__ == "__main__":
    sort_downloads()