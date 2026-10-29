import shutil
from datetime import datetime

class Bak:
    def __file_read(self):
        with open('path.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines

    def backup(self):
        try:
            path = self.__file_read()
            src = path[0][0:-1]
            dst = path[1]
            # print(src)
            # print(dst)
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print("Копирование успешно завершено!")
        except PermissionError:
            print(f"Устройство не готово {src}")
        except IndexError:
            print("Ошибка чтения файла")

    def time_copy(self):
        return datetime.now()
