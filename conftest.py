"""
Конфигурационный файл для pytest.
Добавляет путь к проекту в sys.path для корректного импорта модулей.
"""
import sys
import os

# Добавляем корневую директорию проекта в путь Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))