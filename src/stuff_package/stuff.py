# stuff
# Created by Sergey Yaksanov at 29.10.2021
# Copyright © 2020 Yakser. All rights reserved.

import argparse


class FilenameParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="Stuff.py creates .py and .txt test files")
        self._parser.add_argument('filename', metavar='filename', type=str, help='Filename without extension')

    def get_filename(self):
        return self._get_args().filename

    def _get_args(self):
        return self._parser.parse_args()


class StuffCreator:
    def __init__(self, filename: str):
        self._filename = filename
        self._PYTHON_FILE_TEMPLATE = f"with open('{self.filename + '-test.txt'}') as file:\n" \
                                     f"    data = file.read().strip().split('\\n')\n"

    def create_stuff(self):
        self._create_python_file()
        self._create_test_files()

    def _create_python_file(self):
        python_file = open(f"{self.filename}.py", 'w')
        python_file.write(self._PYTHON_FILE_TEMPLATE)

    def _create_test_files(self):
        open(f"{self.filename}-test.txt", 'w')
        open(f"{self.filename}-A.txt", 'w')
        open(f"{self.filename}-B.txt", 'w')

    @property
    def filename(self):
        return self._filename

    @filename.getter
    def get_filename(self):
        return self._filename


if __name__ == '__main__':

    parser = FilenameParser()
    filename = parser.get_filename()

    stuff_creator = StuffCreator(filename)
    stuff_creator.create_stuff()
