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
📸 Скриншоты
1. Ввод пути к папке
https://github.com/Vasiliy-Underground/organize-downloads/blob/master/screenshots/%25D0%2592%25D1%2581%25D1%2582%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25BF%25D1%2583%25D1%2582%25D1%258C.png?raw=true

2. Настройка автозапуска
https://github.com/Vasiliy-Underground/organize-downloads/blob/master/screenshots/%25D0%2592%25D0%25BA%25D0%25BB%25D1%258E%25D1%2587%25D0%25B8%25D1%2582%25D1%258C_%25D0%25B2%25D1%258B%25D0%25BA%25D0%25BB%25D1%258E%25D1%2587%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25B0%25D0%25B2%25D1%2582%25D0%25BE%25D0%25B7%25D0%25B0%25D0%25BF%25D1%2583%25D1%2581%25D0%25BA.png?raw=true

3. Настройка типов файлов и папок
https://github.com/Vasiliy-Underground/organize-downloads/blob/master/screenshots/%25D0%2598%25D0%25B7%25D0%25BC%25D0%25B5%25D0%25BD%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5%2520%25D0%25BF%25D0%25B0%25D0%25BF%25D0%25BE%25D0%25BA%2520%25D0%25B8%2520%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D0%25BE%25D0%25B2%2520%25D1%2587%25D0%25B5%25D1%2580%25D0%25B5%25D0%25B7%2520%25D0%25BA%25D0%25BE%25D0%25B4.png?raw=true

📂 Структура после сортировки
text
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
🛠 Поддерживаемые форматы
Тип	Расширения
Images	.jpg, .jpeg, .png, .gif, .bmp, .webp, .psd, .tif, .heic
Documents	.pdf, .docx, .txt, .xlsx, .pptx, .htm
Videos	.mp4, .avi, .mkv, .mov
Archives	.zip, .rar, .7z
Programs	.exe, .msi, .msix
Games	.iso, .bin, .cue, .torrent
⚙️ Как отключить автозапуск
Просто запустите программу снова и введите off при вопросе об автозапуске.

📄 Лицензия
MIT — делайте что хотите, но ссылку на автора оставьте :)

👨‍💻 Автор
Vasiliy-Underground