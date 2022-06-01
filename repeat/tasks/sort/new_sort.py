import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import sys
import shutil

# This is refactoring old code (old_sort.py)

class Sort:
    
    def valid_folder(self, text):
        folder = input(text)
        while not os.path.exists(fr'{folder}'):
            folder = input('Вы указали неверный (несуществующий путь)\nУкажите полный путь\n: ')

        return folder

    def main(self):
        folder_for_sort = self.valid_folder('Какую папку вы хотите отсартировать? (укажите полный путь)\n: ')
        place_for_scrapped = self.valid_folder('В каком месте будут лежать отсартированные файлы? (в ней автоматически создаста папка Sort)\n: ')

        extensions = {

           'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 
                     'h264', 'flv', 'rm', 'swf', 'vob'],

            'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 
                    'tar', 'xml'],

            'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
                     'cda'],

            'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 
                     'tiff'],

            'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

            'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

            '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

            'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

            'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

            'font': ['otf', 'ttf', 'fon', 'fnt'],

            'gif': ['gif'],

            'exe': ['exe'],

            'bat': ['bat'],

            'apk': ['apk']
        }      


def start():
    start = Sort()
    start.main()


if __name__ == '__main__':
    start()
