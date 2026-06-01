# 📁 Organize Downloads

**Универсальный инструмент для автоматической сортировки файлов в любой папке Windows**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-10%2B-green.svg)](https://www.microsoft.com/windows)

## 🎯 Что делает

Сортирует файлы в папке по типам и годам. Работает в двух режимах:
- **Ручной** — запустил один раз, отсортировал
- **Автоматический** — сортирует при каждом запуске компьютера

## ✨ Особенности

- ✅ Автоматическое создание папок: `Images`, `Documents`, `Videos`, `Archives`, `Programs`, `Games`
- ✅ Внутри каждой папки — сортировка по годам: `Images/2025/`, `Documents/2024/`
- ✅ Не трогает незаконченные загрузки (`.crdownload`, `.tmp`, `.part`)
- ✅ Сам создаёт и настраивает автозапуск Windows
- ✅ Сам чистит мёртвые ссылки при перемещении папки
- ✅ Полный лог всех действий в ручном режиме

## 🚀 Быстрый старт

```bash
git clone https://github.com/Vasiliy-Underground/organize-downloads.git
cd organize-downloads
python organize_downloads.py
```

## 📸 Скриншоты

### 1. Копирование пути к папке
![Скопировать путь](https://raw.githubusercontent.com/Vasiliy-Underground/organize-downloads/master/screenshots/1.png)

### 2. Ввод пути в программу
![Вставить путь](https://raw.githubusercontent.com/Vasiliy-Underground/organize-downloads/master/screenshots/2.png)

### 3. Настройка автозапуска
![Включить/выключить автозапуск](https://raw.githubusercontent.com/Vasiliy-Underground/organize-downloads/master/screenshots/3.png)

### 4. Добавление новых типов файлов и папок
![Изменение папок и форматов через код](https://raw.githubusercontent.com/Vasiliy-Underground/organize-downloads/master/screenshots/4.png)

📂 Структура после сортировки
```
Ваша папка/
├── Images/
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
├── Documents/
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
├── Videos/
├── Archives/
├── Programs/
├── Games/
└── Other/
```

🛠 Поддерживаемые форматы
```
Тип	Расширения
Images	.jpg, .jpeg, .png, .gif, .bmp, .webp, .psd, .tif, .heic
Documents	.pdf, .docx, .txt, .xlsx, .pptx, .htm
Videos	.mp4, .avi, .mkv, .mov
Archives	.zip, .rar, .7z
Programs	.exe, .msi, .msix
Games	.iso, .bin, .cue, .torrent
```

⚙️ Как отключить автозапуск
Просто запустите программу снова и введите off при вопросе об автозапуске.

📄 Лицензия
MIT — делайте что хотите, но ссылку на автора оставьте :)

👨‍💻 Автор
Vasiliy-Underground