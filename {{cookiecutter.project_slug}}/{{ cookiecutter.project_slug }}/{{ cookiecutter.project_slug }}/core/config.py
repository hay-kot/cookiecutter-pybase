from pathlib import Path

from schema.config import AppConfig

BASE_DIR = Path(__file__).parent.parent
APP_VERSION = "{{ cookiecutter.version }}"


config = AppConfig()
