#!/usr/bin/env python
import os
from pathlib import Path
import shutil

PROJECT_DIRECTORY = Path.cwd()

TYPER_GLOB = "**/typer_*"
APP_GLOB = "**/app_*"



def drop_files(glob_str):
    for fs_obj in PROJECT_DIRECTORY.glob(glob_str):
        fs_obj.unlink() if fs_obj.is_file() else shutil.rmtree(fs_obj)

def rename_files(glob_str, drop_text):
    for file in PROJECT_DIRECTORY.glob(glob_str):
        file.rename(Path(file.parent, file.name.replace(drop_text, "")))


if __name__ == '__main__':

    if '{{cookiecutter.use_typer_cli}}' == "y":
        drop_files(APP_GLOB)
        rename_files(TYPER_GLOB, "typer_")
    
    else:
        drop_files(TYPER_GLOB)
        rename_files(APP_GLOB, "app_")
