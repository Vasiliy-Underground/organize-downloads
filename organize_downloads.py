import os
import shutil
import datetime
import sys

# ========== ЗАЩИТА ОТ ОШИБОК В ТИХОМ РЕЖИМЕ ==========
if "--auto" in sys.argv:
    def input(prompt=""):
        raise RuntimeError("input() в тихом режиме")

# ========== ПУТЬ К НАСТРОЙКАМ ==========
def get_config_path():
    appdata = os.environ.get("APPDATA", os.path.expanduser("~"))
    config_dir = os.path.join(appdata, "OrganizeDownloads")
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "config.txt")

# ========== ФУНКЦИЯ СОРТИРОВКИ (без логов) ==========
def sort_files(target_path, silent=False):
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".psd", ".tif", ".heic"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".htm"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi", ".msix"],
        "Games": [".iso", ".bin", ".cue", ".torrent"]
    }
    
    skip_extensions = [".crdownload", ".tmp", ".part", ".parts"]
    system_files = ["desktop.ini", "Thumbs.db"]
    
    def get_file_year(file_path):
        return datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y")
    
    def create_folder(path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    if not silent:
        print("🔄 Сортировка...")
    
    # Сортируем файлы внутри существующих папок по годам
    for folder in folders:
        folder_path = os.path.join(target_path, folder)
        if not os.path.exists(folder_path):
            continue
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if not os.path.isfile(file_path) or file in system_files:
                continue
            parent = os.path.basename(folder_path)
            if parent.isdigit() and len(parent) == 4:
                continue
            year = get_file_year(file_path)
            target = os.path.join(folder_path, year)
            create_folder(target)
            shutil.move(file_path, os.path.join(target, file))
            if not silent:
                print(f"  {file} -> {folder}/{year}")
    
    # Создаём основные папки
    for folder in folders:
        create_folder(os.path.join(target_path, folder))
    
    # Сортируем файлы из корня
    moved = 0
    skipped = 0
    
    for file in os.listdir(target_path):
        file_path = os.path.join(target_path, file)
        if not os.path.isfile(file_path) or file in system_files:
            continue
        if any(file.lower().endswith(ext) for ext in skip_extensions):
            if not silent:
                print(f"  ⏭ Пропущен: {file}")
            skipped += 1
            continue
        
        found = False
        for folder, exts in folders.items():
            if any(file.lower().endswith(ext) for ext in exts):
                year = get_file_year(file_path)
                target = os.path.join(target_path, folder, year)
                create_folder(target)
                shutil.move(file_path, os.path.join(target, file))
                if not silent:
                    print(f"  {file} -> {folder}/{year}")
                moved += 1
                found = True
                break
        
        if not found:
            other = os.path.join(target_path, "Other")
            create_folder(other)
            shutil.move(file_path, os.path.join(other, file))
            if not silent:
                print(f"  {file} -> Other")
            moved += 1
    
    if not silent:
        print(f"\n✅ Готово! Перемещено: {moved}, пропущено: {skipped}")

# ========== ФУНКЦИИ АВТОЗАПУСКА ==========
def get_startup_folder():
    return os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

def get_exe_path():
    if getattr(sys, 'frozen', False):
        return sys.executable
    return os.path.abspath(__file__)

def setup_autostart():
    bat = os.path.join(get_startup_folder(), "organize_downloads.bat")
    with open(bat, "w") as f:
        f.write(f'@echo off\n"{get_exe_path()}" --auto\n')
    print("✅ Автозапуск включён")

def remove_autostart():
    bat = os.path.join(get_startup_folder(), "organize_downloads.bat")
    if os.path.exists(bat):
        os.remove(bat)
        print("✅ Автозапуск выключен")

def autostart_enabled():
    return os.path.exists(os.path.join(get_startup_folder(), "organize_downloads.bat"))

# ========== ОСНОВНАЯ ПРОГРАММА ==========
if __name__ == "__main__":
    config = get_config_path()
    
    # Тихий режим
    if "--auto" in sys.argv:
        if not os.path.exists(config):
            sys.exit(0)
        with open(config, "r") as f:
            path = f.read().strip()
        if os.path.exists(path):
            sort_files(path, silent=True)
        sys.exit(0)
    
    # Ручной режим
    print("=" * 50)
    print("ОРГАНИЗАТОР ФАЙЛОВ")
    print("=" * 50)
    
    while True:
        target = input("\nПуть к папке (Enter = Загрузки): ").strip().strip('"').strip("'")
        if not target:
            target = os.path.join(os.environ["USERPROFILE"], "Downloads")
        if os.path.isdir(target):
            break
        print("❌ Папка не найдена")
    
    # Сохраняем путь
    with open(config, "w") as f:
        f.write(target)
    
    status = "включён" if autostart_enabled() else "выключен"
    print(f"\nАвтозапуск: {status}")
    
    while True:
        mode = input("Включить автозапуск? (on/off, Enter = пропустить): ").strip().lower()
        if mode in ["on", "off", ""]:
            break
        print("❌ Введите on, off или Enter")
    
    if mode == "on":
        setup_autostart()
    elif mode == "off":
        remove_autostart()
    
    print()
    sort_files(target, silent=False)
    input("\nНажмите Enter для выхода...")
    