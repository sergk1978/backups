from pathlib import Path
from shutil import rmtree
import time

class Delete:
    def __init__(self, path, days):  
        self.path = path             # путь до папки (обмен)
        self.days = days             # количество дней 
    
    
    def dir_list(self):
        # добавление папок по дате, если созданы больше x дней
        dirs = [path for path in Path(self.path).iterdir() if self.__dir_time_delta(path) > self.days and not path.is_file()]
        return dirs
    
    
    def dir_list_2(self):
        # добавление папок по дате, если созданы больше x дней
        dirs = [str(path)[len(str(self.path))+1:] for path in Path(self.path).iterdir() if self.__dir_time_delta(path) > self.days]
        return dirs

    
    def dir_delete(self):
        if len(self.dir_list())>0:
            for dir in self.dir_list():
                #rmtree(dir)
                print(f'Удалена папка - {dir}')
        else:
            print('Каталогов, соответствующих условию, для удаления нет')  

    def __dir_time_delta(self, dir):      
        # отклонение времени создания файла(папки) от текущего времени                
        dir_timestamp = Path(dir).stat().st_ctime
        #print(dir_timestamp)
        dir_delta = (time.time() - dir_timestamp) // (60 * 60 * 24) 
        return int(dir_delta)




# d = Delete('D:\\Python\\backups\\test3\\arhivator', 10) 
# print(d.dir_list())
# d.dir_delete()
#print(d.__dir_time_delta('main.py'))   