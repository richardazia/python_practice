import json

# based on Linkedin Learning course: Python: Working with files
# URL: https://www.linkedin.com/learning/python-working-with-files/navigate-the-file-system-with-os-module?autoSkip=true&autoplay=true&resume=false
# import glob
# import os
# from pathlib import Path
# from datetime import datetime
#
# seconds = datetime.now().second
# minutes = datetime.now().minute
# hours = datetime.now().hour
#
#
# def display_cwd():
#     cwd = os.getcwd()
#     print(f"This is the Current Working Directory: {cwd}")
#
#
# def show_directories(directory):
#     with os.scandir(directory) as entries:
#         for entry in entries:
#             if entry.is_dir():
#                 print(f"Directory name is: {entry}")
#
#
# def show_files(directory):
#     with os.scandir(directory) as entries:
#         i = 0
#         for entry in entries:
#             if entry.is_file():
#                 i += 1
#                 print(f"File name is: {entry}")
#         print(f"There are {i} files in this directory")
#
#
# def parent_folder():
#     os.chdir("../")
#
#
# def format_datetime(timestamp):
#     utc_timestamp = datetime.utcfromtimestamp(timestamp)
#     formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
#     return formated_date
#
#
# def ls_scandir(directory):
#     with os.scandir(directory) as entries:
#         i = 0
#         for entry in entries:
#             i += 1
#             print(f"{i}: Name: {entry.name}")
#             info = entry.stat()
#             print(f"Creation Time: {format_datetime(info.st_ctime)}")
#             print(f"Last accessed: {format_datetime(info.st_atime)}")
#             print(f"Size: {info.st_size}Kb")
#
#
# def display_pys():
#     py_files = glob.glob('*.py')
#     # with glob.glob('filenamea"') we can search for files by name or part of a name.
#     print(py_files)
#
#
# def mk_dir():
#     try:
#         os.mkdir("chickens/")
#     except FileExistsError as ex:
#         print("This directory already exists, please try another name.")
#
#
# def make_model_dir():
#     dir_path = Path("model/")
#     dir_path.mkdir(exist_ok=True)
#
#
# def make_view_dir():
#     dir_path = Path("view/")
#     dir_path.mkdir(exist_ok=True)
#
#
# def make_controller_dir():
#     dir_path = Path("controller/")
#     dir_path.mkdir(exist_ok=True)
#
#
# def mvc_dirs():
#     make_model_dir()
#     make_view_dir()
#     make_controller_dir()
#
#
# if __name__ == "__main__":
#     display_cwd()
#     parent_folder()
#     display_cwd()
#     ls_scandir("python3")
#     show_directories("python3")
#     show_files("python3")
#     display_pys()
#     mk_dir()
#     mvc_dirs()
#
# print(f"Information retrieved at: {hours}:{minutes}:{seconds}")
#
######################
# # Debug later
# import os
#
# def count_files_with_os_walk(path):
#     total_files = 0
#     for base, subdirs, files in os.walk(path):
#         for file in total_files:
#             total_files += 1
#     return total_files
#
#
# if __name__ == "__main__":
#     print(count_files_with_os_walk('.'))
#######################
#
# # scandir
# from pathlib import Path
#
#
# def count_files_with_scandir(path):
#     total = 0
#     for entry in os.scandir(path):
#         if entry.is_file():
#             total += 1
#         else:
#             total += count_files_with_scandir(entry)
#     return total
#
# def count_files_with_pathlib(path):
#     total = 0
#     for entry in Path(path).iterdir():
#         if entry.is_file():
#             total += 1
#         else:
#             total += count_files_with_pathlib(entry)
#     return total
#
#
# print(count_files_with_pathlib('.'))
# print(count_files_with_scandir('.'))

###########################################

# I suspect that the problem I had before is related to using windows rather than a mac.
# URL of code I tried: https://pynative.com/python-count-number-of-files-in-a-directory/
############################
# import os
#
# dir_path = r'.'
# file = 0
#
# for path in os.listdir(dir_path):
#     if os.path.isfile(os.path.join(dir_path, path)):
#         file += 1
#
# print(f"Number of files {file}")
#
# import fnmatch
#
# path = '.'
#
# count = len(fnmatch.filter(os.listdir(path), '*.*'))
#
# print(f"File Count with 'fnmath': {count}")
############################
# https://pynative.com/python-create-file/
import os
# fp = open('monday_later.txt', 'x')
# fp.close()

fp = open('huts.txt', 'w')
fp.write('Python is creating and then adding text to a file')
fp.close()

fp = open('consolidation.txt', 'a')
fp.write('\nI am not a PBY-Catalina')
fp.write('\nA frolicking chicken')
fp.close()

# add datetime log info

from datetime import datetime

current_time = datetime.now()

filename = current_time.strftime('%d-%m-%Y.text')
with open(filename, 'a') as fp:
    print(f"Created: {filename}")

seconds = current_time.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(seconds, 'w') as fp:
    print(f"Created: {seconds}")

# To check what we have done

import os

print(os.listdir())

print(f"File created: {os.path.isfile('huts.txt')}")

########################################
# Python - working with files course

def print_content():
    f = open('read_me_now.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()


def write_new_content():
    f = open('read_me_now.txt', 'a')
    f.write("\nThe sun does not always rise at the same time. It changes by three minutes per day, depending on where you live\neof")
    f.close


def read_ten_bytes():
    with open('read_me_now.txt', 'r') as f:
        print(f.read(15))


def print_file_content_readlines():
    with open('read_me_now.txt', 'r') as f:
        lines = f.readlines()
        print(lines)
        print(f"Line 3: {lines[3]}")


def teleprompter():
    with open('read_me_now.txt', 'r') as f:
        line = f.readline()
        ln = 0
        while line != '':

            print(f"{ln}: {line}")
            line = f.readline()
            ln += 1
################################


def read_and_display_json():
    with open('duck.json') as f:
        content_json = json.load(f)
        print("I am JSON")
        print(content_json)


if __name__ == '__main__':
    print_content()
    write_new_content()
    print_content()
    read_ten_bytes()
    print_file_content_readlines()
    read_ten_bytes()
    teleprompter()
    read_and_display_json()



