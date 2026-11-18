from shutil import copytree, ignore_patterns
from datetime import datetime
from filesize import Size
from pathlib import Path
from delete import Delete


class Bak:
    def __init__(self, path):   
        self.path = path                                       # 'path.txt'
        self.src, self.dst, self.pattern, self.delet = self.__file_read()
        self.src = self.src.strip('\n').strip()
        self.dst = self.dst.strip()
        print(self.delet)
        print(self.dst)
        self.d = Delete(self.dst, int(self.delet))
        self.dst = self.__new_folder()
        self.pattern = self.pattern.strip().split(',')        # pattern (исключаемые каталоги и файлы)
        self.s = Size(self.dst)                               # размер скопированной папки


    def __file_read(self):
        if Path(self.path).exists():
            with open(self.path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines)<3:
                    print("в файле path.txt отсутствуют один, или оба пути назначения!, и(или) паттерн исключения каталогов(файлов)")
                    input('Нажмите Enter для выхода...')
                    exit(1)
                return lines
        else:
            print("Отсутствует файл: path.txt")
            input('Нажмите Enter для выхода...')
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
            print(f"Системе не удается создать папку назначения по указаннному пути: {self.dst}")
            print("Копирование отменено!")
            input('Нажмите Enter для выхода...')
            exit(1)


    def backup(self):
        # path = self.__file_read()
        # src = path[0][0:-1].strip()    
        # dst = path[1].strip()
        #print(self.src)
        #print(self.dst)
        #print(self.pattern)
        copytree(self.src, self.dst, ignore=ignore_patterns(*self.pattern), dirs_exist_ok=True)
        print("Копирование успешно завершено!")
        

            



