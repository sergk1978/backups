from pathlib import Path
from shutil import rmtree
import time
import stat

class Delete:
    def __init__(self, path, days):  
        self.path = path             # путь до папки назначения (обмен)
        self.days = days             # количество дней, от текущей даты
    
    
    def dir_list(self):
        # добавление папок по дате, если созданы больше x дней = days (исключая файлы)
        dirs = [path for path in Path(self.path).iterdir() if self.__dir_time_delta(path) >= self.days and not path.is_file()]
        return dirs
    
    
    def dir_list_2(self):
        # добавление папок по дате, если созданы больше x дней(для теста)
        dirs = [str(path)[len(str(self.path))+1:] for path in Path(self.path).iterdir() if self.__dir_time_delta(path) > self.days]
        return dirs

    
    def dir_delete(self):
        if len(self.dir_list())>0:
            print("Удаление началось ...")
            for dir in self.dir_list():
                #############
                # замена прав у папок и файлов на полные во избежание ошибки PermissionError: [WinError 5] Отказано в доступе
                dir = Path(dir)
                for item in dir.rglob('*'):
                    item.chmod(stat.S_IRWXU)      
                ##############
                rmtree(dir)
                print(f'Удалена папка - {dir}')
        else:
            print('Каталогов, соответствующих условию, для удаления нет')  

    def __dir_time_delta(self, dir):      
        dir_timestamp = Path(dir).stat().st_birthtime   # время создания папки
        #print(dir_timestamp)
        dir_delta = (time.time() - dir_timestamp) // (60 * 60 * 24) # отклонение времени создания файла(папки) от текущего времени 
        return int(dir_delta)


###### test #####

# d = Delete('D:\\Python\\backups\\test3\\arhivator', 10) 
# print(d.dir_list())
# d.dir_delete()
#print(d.__dir_time_delta('main.py'))   