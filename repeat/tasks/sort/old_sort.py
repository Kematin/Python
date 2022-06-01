import watchdog
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler
import sys
import threading
import shutil

# This code taken from old repository (https://github.com/Kematin/Qt5/tree/master/sort%20programm)


#Main function
    def sort(self):
        threading.Thread(target=self.quick_sort).start()


    def quick_sort(self):
        if os.path.exists(self.input_folder.text()) == True and os.path.exists(self.output_folder.text()) == True:
            self.location_of_input = self.input_folder.text()
            self.location_of_output = self.output_folder.text()
        else:
            error = QMessageBox()

            error.setText('Выбранного каталогая не существует')
            error.setWindowTitle('Ошибка')
            error.setStandardButtons(QMessageBox.Ok)
            error.setWindowIcon(QIcon('sort.png'))

            error.exec_()


        if os.path.exists(self.location_of_output + '/Sort') == False:
            os.mkdir(self.location_of_output + '/Sort')
            os.mkdir(self.location_of_output + '/Sort' + '/Изображения')
            os.mkdir(self.location_of_output + '/Sort' + '/Аудио')
            os.mkdir(self.location_of_output + '/Sort' + '/Видео')
            os.mkdir(self.location_of_output + '/Sort' + '/Тексты')
            os.mkdir(self.location_of_output + '/Sort' + '/Приложения')
            os.mkdir(self.location_of_output + '/Sort' + '/Архивы')
            os.mkdir(self.location_of_output + '/Sort' + '/Файлы расчётов')



        image = ['png', 'jpg', 'svg', 'ico', 'webp', 'bmp', 'gif', 'jpeg', 'psd', 'tiff', 'ai']
        video = ['mp4', 'avi', 'webm', 'mpg', 'mpeg']
        audio = ['mp3', 'amr']
        txt = ['txt', 'docx', 'csv']
        app = ['exe', 'apk']
        zip_rar = ['zip', 'rar', 'iso', '7z']
        calculation = ['html', 'py', 'xls', 'pdf']



        for fl in os.listdir(self.location_of_input):
            ex = fl.split('.')
            if self.all_files.isChecked():
                if len(ex) > 1 and ex[1].lower() in image:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Изображения/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in video:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Видео/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in audio:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Аудио/" + fl
                    shutil.move(file, new_path)
        
                elif len(ex) > 1 and ex[1].lower() in txt:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Тексты/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in app:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Приложения/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in zip_rar:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Архивы/" + fl
                    shutil.move(file, new_path)  

                elif len(ex) > 1 and ex[1].lower() in calculation:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Файлы расчётов/" + fl
                    shutil.move(file, new_path)


            else:
                for_sort = []
                if self.image.isChecked():
                    for_sort.append('image')

                if self.audio.isChecked():
                    for_sort.append('audio')

                if self.video.isChecked():
                    for_sort.append('video')

                if self.txt.isChecked():
                    for_sort.apend('txt')

                if self.rar.isChecked():
                    for_sort.append('rar')

                if self.files_exe.isChecked():
                    for_sort.append('files_exe')

                if self.checkBox_9.isChecked():
                    for_sort.append('checkBox_9')


                
                if len(for_sort) < 1:
                    error = QMessageBox()

                    error.setText('Не был выбран ни один тип файлов')
                    error.setWindowTitle('Ошибка')
                    error.setStandardButtons(QMessageBox.Ok)
                    error.setWindowIcon(QIcon('C:/Icons/error.ico'))

                    error.exec_()
                    break

                else:
                    for type_ in for_sort:
                        if type_ == 'image':
                            if len(ex) > 1 and ex[1].lower() in image:
                                file = self.location_of_input + "/" + fl
                                new_path = self.location_of_output + '/Sort' + "/Изображения/" + fl
                                shutil.move(file, new_path)
                        elif type_ == 'video':
                            if len(ex) > 1 and ex[1].lower() in video:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Видео/' + fl
                                shutil.move(file, new_path)

                        elif type_ == 'audio':
                            if len(ex) > 1 and ex[1].lower() in audio:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Аудио/' + fl
                                shutil.move(file, new_path) 

                        elif type_ == 'zip_rar':
                            if len(ex) > 1 and ex[1].lower() in zip_rar:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Архивы/' + fl
                                shutil.move(file, new_path)
                                     
                        elif type_ == 'app':
                            if len(ex) > 1 and ex[1].lower() in app:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Приложения/' + fl
                                shutil.move(file, new_path) 

                        elif type_ == 'calculation':
                            if len(ex) > 1 and ex[1].lower() in calculation:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Файлы расчётов/' + fl
                                shutil.move(file, new_path)
                                     
                        elif type_ == 'txt':
                            if len(ex) > 1 and ex[1].lower() in txt:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Тексты/' + fl
                                shutil.move(file, new_path)


        done = QMessageBox()

        done.setText('Сортировка окончена')
        done.setWindowTitle('Конец')
        done.setStandardButtons(QMessageBox.Ok)
        done.setWindowIcon(QIcon('C:/Icons/done.ico'))

        done.exec_()
