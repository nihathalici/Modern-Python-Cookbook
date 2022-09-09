# Exer-08-Leveraging-the-exception-matching-rules

from pathlib import Path
import shutil
import os

source_path = Path(os.path.expanduser('source'))
target_path = Path(os.path.expanduser('/demo/'))
for source_file_path in source_path.glob('*/*.rst'):
    source_file_detail = source_file_path.relative_to(source_path)
    target_file_path = target_path / source_file_detail
    try:
        shutil.copy(str(source_file_path), str(target_file_path))
    except FileNotFoundError:
        os.makedirs(target_file_path.parent)
        shutil.copy(str(source_file_path), str(target_file_path))
    except OSError as ex:
        print(ex)

###

try:
    shutil.copy(str(source_file_path), str(target_file_path))
except FileNotFoundError:
    try:
        os.makedirs(str(target_file_path.parent))
        shutil.copy(str(source_file_path), str(target_file_path))
    except OSError as ex:
        print(ex)

###

try:
    try:
        shutil.copy(str(source_file_path), str(target_file_path))
    except FileNotFoundError:
        os.makedirs(str(target_file_path.parent))
        shutil.copy(str(source_file_path), str(target_file_path))
except OSError as ex:
        print(ex)

