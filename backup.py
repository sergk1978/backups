import shutil
from datetime import datetime
from pathlib import Path
from filesize import Size

class Bak:
    def __init__(self, path):   
        self.path = path                           # 'path.txt'
        self.src, self.dst = self.__file_read()
        self.src = self.src.strip('\n').strip()
        self.dst = self.dst.strip()
        self.s = Size(self.dst)                    # 'D:\\Python\\backups\\test\\destination_обмен'

    def __file_read(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines

    def backup(self):
        try:
            # path = self.__file_read()
            # src = path[0][0:-1].strip()
            # dst = path[1].strip()
            #print(self.src)
            #print(self.dst)
            if self.src != self.dst:
                shutil.copytree(self.src, self.dst+self.__new_folder(), dirs_exist_ok=True)
                #print(self.new_folder())
                print("Копирование успешно завершено!")
            else:
                print("Источник и папка назначения совпадают")    
        except PermissionError:
            print(f"Устройство не готово {self.src}")
        except IndexError:
            print("Ошибка чтения файла")
        except ValueError: 
            print("Отсутствует один, или оба пути назначения")

    def time_copy(self):
        return datetime.now()

    def __new_folder(self):
        return f'/{Path(self.time_copy().strftime("%Y-%m-%d"))}'