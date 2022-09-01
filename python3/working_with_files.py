# based on Linkedin Learning course: Python: Working with files
# URL: https://www.linkedin.com/learning/python-working-with-files/navigate-the-file-system-with-os-module?autoSkip=true&autoplay=true&resume=false
import glob
import os
from pathlib import Path
from datetime import datetime

seconds = datetime.now().second
minutes = datetime.now().minute
hours = datetime.now().hour


def display_cwd():
    cwd = os.getcwd()
    print(f"This is the Current Working Directory: {cwd}")


def show_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f"Directory name is: {entry}")


def show_files(directory):
    with os.scandir(directory) as entries:
        i = 0
        for entry in entries:
            if entry.is_file():
                i += 1
                print(f"File name is: {entry}")
        print(f"There are {i} files in this directory")


def parent_folder():
    os.chdir("../")


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date


def ls_scandir(directory):
    with os.scandir(directory) as entries:
        i = 0
        for entry in entries:
            i += 1
            print(f"{i}: Name: {entry.name}")
            info = entry.stat()
            print(f"Creation Time: {format_datetime(info.st_ctime)}")
            print(f"Last accessed: {format_datetime(info.st_atime)}")
            print(f"Size: {info.st_size}Kb")


def display_pys():
    py_files = glob.glob('*.py')
    # with glob.glob('filenamea"') we can search for files by name or part of a name.
    print(py_files)


def mk_dir():
    try:
        os.mkdir("chickens/")
    except FileExistsError as ex:
        print("This directory already exists, please try another name.")


def make_model_dir():
    dir_path = Path("model/")
    dir_path.mkdir(exist_ok=True)


def make_view_dir():
    dir_path = Path("view/")
    dir_path.mkdir(exist_ok=True)


def make_controller_dir():
    dir_path = Path("controller/")
    dir_path.mkdir(exist_ok=True)


def mvc_dirs():
    make_model_dir()
    make_view_dir()
    make_controller_dir()


if __name__ == "__main__":
    display_cwd()
    parent_folder()
    display_cwd()
    ls_scandir("python3")
    show_directories("python3")
    show_files("python3")
    display_pys()
    mk_dir()
    mvc_dirs()


print(f"Information retrieved at: {hours}:{minutes}:{seconds}")