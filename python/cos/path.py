from pathlib import Path
import shutil

PROJECT_DIR = (Path(__file__) / "../../..").resolve()


class PathError(Exception):
    pass


def copy(source, dest):
    if Path(source).is_file():
        shutil.copy2(source, dest)
    elif Path(source).is_dir():
        shutil.copytree(source, dest)
    else:
        raise PathError(source)
