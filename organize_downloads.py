import os
import shutil
import datetime
import sys

# ========== ФУНКЦИЯ СОРТИРОВКИ (общая для ручного и авторежима) ==========
def sort_files(target_path, log_mode="full"):
    """
    Сортирует файлы в указанной папке
    log_mode: "full" - полный лог, "quiet" - только итог
    """
    # Настройки
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".psd", ".tif", ".heic"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".htm"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi", ".msix"],
        "Games": [".iso", ".bin", ".cue", ".torrent"]
    }
    
    skip_extensions = [".crdownload", ".tmp", ".part", ".parts"]
    system_files = ["desktop.ini", "Thumbs.db", "sort_log.txt"]
    
    def write_log(message, log_file):
        with open(log_file, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")
        if log_mode == "full":
            print(message)
    
    def get_file_year(file_path):
        mod_time = os.path.getmtime(file_path)
        return datetime.datetime.fromtimestamp(mod_time).strftime("%Y")
    
    def create_folder_if_not_exists(path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    # Лог-файл
    log_file = os.path.join(target_path, "sort_log.txt")
    if os.path.exists(log_file):
        os.remove(log_file)
    
    write_log("=" * 50, log_file)
    write_log("ЗАПУСК СОРТИРОВКИ", log_file)
    write_log(f"Папка: {target_path}", log_file)
    
    # Сортируем уже существующие папки по годам
    write_log("ПРОВЕРКА СУЩЕСТВУЮЩИХ ПАПОК", log_file)
    for folder in folders:
        folder_path = os.path.join(target_path, folder)
        if not os.path.exists(folder_path):
            continue
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if not os.path.isfile(file_path):
                continue
            if file in system_files:
                continue
            parent = os.path.basename(folder_path)
            if parent.isdigit() and len(parent) == 4:
                continue
            year = get_file_year(file_path)
            target = os.path.join(folder_path, year)
            create_folder_if_not_exists(target)
            shutil.move(file_path, os.path.join(target, file))
            write_log(f"✅ {folder}/{file} -> {folder}/{year}/", log_file)
    
    # Создаём основные папки
    for folder in folders:
        path = os.path.join(target_path, folder)
        create_folder_if_not_exists(path)
    
    # Сортируем файлы из корня
    moved_count = 0
    skipped_count = 0
    
    for file in os.listdir(target_path):
        file_path = os.path.join(target_path, file)
        if not os.path.isfile(file_path):
            continue
        if file in system_files:
            continue
        if any(file.lower().endswith(ext) for ext in skip_extensions):
            write_log(f"⏭ Пропущен (незакончен): {file}", log_file)
            skipped_count += 1
            continue
        
        moved = False
        for folder, extensions in folders.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                year = get_file_year(file_path)
                target = os.path.join(target_path, folder, year)
                create_folder_if_not_exists(target)
                shutil.move(file_path, os.path.join(target, file))
                write_log(f"✅ {file} -> {folder}/{year}", log_file)
                moved_count += 1
                moved = True
                break
        
        if not moved:
            other = os.path.join(target_path, "Other")
            create_folder_if_not_exists(other)
            shutil.move(file_path, os.path.join(other, file))
            write_log(f"❓ Неизвестный тип: {file} -> Other", log_file)
            moved_count += 1
    
    write_log(f"ГОТОВО! Перемещено: {moved_count}, пропущено: {skipped_count}", log_file)
    write_log("=" * 50, log_file)
    
    return moved_count, skipped_count


# ========== ФУНКЦИИ ДЛЯ РАБОТЫ С АВТОЗАПУСКОМ ==========
def get_startup_folder():
    """Возвращает путь к папке автозагрузки текущего пользователя"""
    return os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

def create_auto_script(script_dir):
    """Создаёт файл auto_sort.py в папке со скриптом"""
    auto_script_path = os.path.join(script_dir, "auto_sort.py")
    
    # Содержимое auto_sort.py
    auto_script_content = '''import os
import shutil
import datetime

# ========== ФУНКЦИЯ СОРТИРОВКИ (полный лог, без вопросов) ==========
def sort_files_auto(target_path):
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".psd", ".tif", ".heic"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".htm"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi", ".msix"],
        "Games": [".iso", ".bin", ".cue", ".torrent"]
    }
    
    skip_extensions = [".crdownload", ".tmp", ".part", ".parts"]
    system_files = ["desktop.ini", "Thumbs.db", "sort_log.txt"]
    
    def write_log(message, log_file):
        with open(log_file, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\\n")
    
    def get_file_year(file_path):
        mod_time = os.path.getmtime(file_path)
        return datetime.datetime.fromtimestamp(mod_time).strftime("%Y")
    
    def create_folder_if_not_exists(path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    log_file = os.path.join(target_path, "sort_log.txt")
    if os.path.exists(log_file):
        os.remove(log_file)
    
    write_log("=" * 50, log_file)
    write_log("АВТОМАТИЧЕСКАЯ СОРТИРОВКА", log_file)
    write_log(f"Папка: {target_path}", log_file)
    
    # Сортируем существующие папки по годам
    for folder in folders:
        folder_path = os.path.join(target_path, folder)
        if not os.path.exists(folder_path):
            continue
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if not os.path.isfile(file_path):
                continue
            if file in system_files:
                continue
            parent = os.path.basename(folder_path)
            if parent.isdigit() and len(parent) == 4:
                continue
            year = get_file_year(file_path)
            target = os.path.join(folder_path, year)
            create_folder_if_not_exists(target)
            shutil.move(file_path, os.path.join(target, file))
            write_log(f"✅ {folder}/{file} -> {folder}/{year}/", log_file)
    
    for folder in folders:
        path = os.path.join(target_path, folder)
        create_folder_if_not_exists(path)
    
    moved_count = 0
    skipped_count = 0
    
    for file in os.listdir(target_path):
        file_path = os.path.join(target_path, file)
        if not os.path.isfile(file_path):
            continue
        if file in system_files:
            continue
        if any(file.lower().endswith(ext) for ext in skip_extensions):
            write_log(f"⏭ Пропущен: {file}", log_file)
            skipped_count += 1
            continue
        
        moved = False
        for folder, extensions in folders.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                year = get_file_year(file_path)
                target = os.path.join(target_path, folder, year)
                create_folder_if_not_exists(target)
                shutil.move(file_path, os.path.join(target, file))
                write_log(f"✅ {file} -> {folder}/{year}", log_file)
                moved_count += 1
                moved = True
                break
        
        if not moved:
            other = os.path.join(target_path, "Other")
            create_folder_if_not_exists(other)
            shutil.move(file_path, os.path.join(other, file))
            write_log(f"❓ {file} -> Other", log_file)
            moved_count += 1
    
    write_log(f"ГОТОВО! Перемещено: {moved_count}, пропущено: {skipped_count}", log_file)
    write_log("=" * 50, log_file)

# ========== ОСНОВНАЯ ЛОГИКА АВТОЗАПУСКА ==========
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.txt")
    bat_path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "sort_downloads.bat")
    
    if not os.path.exists(config_path):
        # Нет config.txt -> удаляем .bat и выходим
        if os.path.exists(bat_path):
            os.remove(bat_path)
        sys.exit(0)
    
    with open(config_path, "r", encoding="utf-8") as f:
        target_path = f.read().strip()
    
    if not os.path.exists(target_path):
        # Путь не существует -> удаляем .bat и config.txt
        if os.path.exists(bat_path):
            os.remove(bat_path)
        if os.path.exists(config_path):
            os.remove(config_path)
        sys.exit(0)
    
    # Всё хорошо -> сортируем
    sort_files_auto(target_path)
'''
    
    with open(auto_script_path, "w", encoding="utf-8") as f:
        f.write(auto_script_content)
    return auto_script_path

def setup_autostart(script_dir, target_path):
    """Создаёт или обновляет автозапуск"""
    startup_folder = get_startup_folder()
    bat_path = os.path.join(startup_folder, "sort_downloads.bat")
    config_path = os.path.join(script_dir, "config.txt")
    auto_script_path = os.path.join(script_dir, "auto_sort.py")
    
    # Создаём auto_sort.py если нет
    if not os.path.exists(auto_script_path):
        create_auto_script(script_dir)
    
    # Сохраняем путь в config.txt
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(target_path)
    
    # Создаём .bat файл
    bat_content = f'@echo off\npython "{auto_script_path}"\n'
    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(bat_content)
    
    print(f"✅ Автозапуск установлен")
    print(f"   Путь сохранён: {config_path}")
    print(f"   Файл автозапуска: {bat_path}")
    return True

def remove_autostart(script_dir):
    """Удаляет автозапуск"""
    startup_folder = get_startup_folder()
    bat_path = os.path.join(startup_folder, "sort_downloads.bat")
    config_path = os.path.join(script_dir, "config.txt")
    
    # Удаляем .bat
    if os.path.exists(bat_path):
        os.remove(bat_path)
        print(f"✅ Удалён файл автозапуска: {bat_path}")
    
    # Удаляем config.txt
    if os.path.exists(config_path):
        os.remove(config_path)
        print(f"✅ Удалён config.txt")
    
    # auto_sort.py не удаляем (оставляем на случай повторного включения)

def check_and_fix_autostart(script_dir):
    """Проверяет, ведёт ли .bat на актуальный путь. Если нет - пересоздаёт"""
    startup_folder = get_startup_folder()
    bat_path = os.path.join(startup_folder, "sort_downloads.bat")
    config_path = os.path.join(script_dir, "config.txt")
    auto_script_path = os.path.join(script_dir, "auto_sort.py")
    
    if not os.path.exists(bat_path):
        return  # нет .bat - ничего не делаем
    
    # Читаем .bat и проверяем, ведёт ли он на существующий auto_sort.py
    with open(bat_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ожидаемый путь в .bat: python "C:\...\auto_sort.py"
    expected = f'python "{auto_script_path}"'
    if expected not in content:
        # Неправильный путь - удаляем старый .bat
        os.remove(bat_path)
        print("⚠️ Обнаружена устаревшая ссылка в автозагрузке. Удалено.")
        # Если есть config.txt - тоже удаляем (чтобы не было рассинхрона)
        if os.path.exists(config_path):
            os.remove(config_path)
        return False
    
    # Проверяем, существует ли auto_sort.py
    if not os.path.exists(auto_script_path):
        os.remove(bat_path)
        if os.path.exists(config_path):
            os.remove(config_path)
        print("⚠️ auto_sort.py не найден. Автозапуск отключён.")
        return False
    
    return True


# ========== ОСНОВНАЯ ПРОГРАММА ==========
if __name__ == "__main__":
    print("=" * 50)
    print("ОРГАНИЗАТОР ФАЙЛОВ")
    print("=" * 50)
    
    # Получаем путь к папке, где лежит скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Проверяем и чиним автозапуск (если есть мёртвые ссылки)
    check_and_fix_autostart(script_dir)
    
    # Шаг 1: путь для сортировки
    while True:
        target = input("\nВведите путь к папке для сортировки\n(Enter = папка Загрузки): ").strip().strip('"').strip("'")
        if not target:
            target = os.path.join(os.environ["USERPROFILE"], "Downloads")
            print(f"✅ Использую: {target}")
        
        if os.path.exists(target) and os.path.isdir(target):
            break
        else:
            print(f"❌ Ошибка: Папка '{target}' не найдена! Попробуйте ещё раз.")
    
    # Шаг 2: режим автозапуска
    while True:
        mode = input("\nАвтоматический режим? (on/off, Enter = пропустить): ").strip().lower()
        if mode in ["on", "off", ""]:
            break
        else:
            print("❌ Введите 'on', 'off' или нажмите Enter")
    
    # Обрабатываем режим
    autostart_changed = False
    if mode == "on":
        setup_autostart(script_dir, target)
        autostart_changed = True
        wait_at_end = False  # не ждём Enter
    elif mode == "off":
        remove_autostart(script_dir)
        autostart_changed = True
        wait_at_end = True   # ждём Enter
    else:  # Enter - пропустить
        wait_at_end = True   # ждём Enter
    
    # Шаг 3: запускаем сортировку
    print("\n🔄 Начинаю сортировку...\n")
    sort_files(target, log_mode="full")
    
    # Шаг 4: выход
    if wait_at_end:
        input("\nНажмите Enter для выхода...")