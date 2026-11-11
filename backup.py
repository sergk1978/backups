import shutil
from datetime import datetime
from filesize import Size
from pathlib import Path


class Bak:
    def __init__(self, path):   
        self.path = path                           # 'path.txt'
        self.src, self.dst = self.__file_read()
        self.src = self.src.strip('\n').strip()
        self.dst = self.dst.strip()
        self.dst = self.__new_folder()
        self.s = Size(self.dst)                    # 'D:\\Python\\backups\\test\\destination_обмен'

    def __file_read(self):
        if Path(self.path).exists():
            with open(self.path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines)<2:
                    print("в файле path.txt отсутствуют один, или оба пути назначения!")
                    exit(1)
                return lines
        else:
            print("Отсутствует файл: path.txt")
            exit(1)

    def time_copy(self):
        return datetime.now()

    def __new_folder(self):
        return f'{self.dst+"\\"+self.time_copy().strftime("%d-%m-%Y")}'  # путь назначения

    def create_folder(self):
        #print(self.dst)
        try:
            if not Path(self.dst).exists():
                Path(self.dst).mkdir(parents=True, exist_ok=True) 
        except FileNotFoundError:
            print(f"Системе не удается создать указанный путь: {self.dst}")

    def backup(self):
        try:
            # path = self.__file_read()
            # src = path[0][0:-1].strip()
            # dst = path[1].strip()
            #print(self.src)
            #print(self.dst)
            if Path(self.dst).exists():
                    shutil.copytree(self.src, self.dst, dirs_exist_ok=True)
                    print("Копирование успешно завершено!")
            else:
                print("Копирование отменено!")
        except PermissionError:
            print(f"Устройство не готово {self.src}")
        except IndexError:
            print("Ошибка чтения файла")
        #except ValueError: 
            #print("Отсутствует один, или оба пути назначения")


