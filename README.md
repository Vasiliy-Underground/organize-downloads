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
- ✅ Полный лог всех действий

## 🚀 Быстрый старт

```bash
git clone https://github.com/Vasiliy-Underground/organize-downloads.git
cd organize-downloads
python organize_downloads.py