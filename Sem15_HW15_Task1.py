# Задача взята за основу с последнего семинара без логирования и argparse

import argparse
import pathlib
import logging
from collections import namedtuple

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

DIRSUBJECT = namedtuple('DIRSUBJECT', ['file_name', 'ext', 'flag', 'name_dir'])

def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))
    return new_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve directory information")
    parser.add_argument("path", type=str, help="Path to the directory")
    args = parser.parse_args()

    try:
        result = dir_info(args.path)
        for item in result:
            logger.info(f"File Name: {item.file_name}, Extension: {item.ext}, Is Directory: {item.flag}, Parent Directory: {item.name_dir}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# C:/Users/Imp1/AppData/Local/Programs/Python/Python311/python.exe "e:/Учеба/Учусь/Dive into Python/Sem15_HW15_Task1.py" "E:\Учеба\Учусь\Dive into Python"