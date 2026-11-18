from pathlib import Path
from collections import Counter
from shutil import rmtree
import time

# Объединение компонентов пути
# print(Path('usr') / 'bin' / 'spam')
# print(Path.home())
# print(Path.cwd())
# print(Path('filesize.py').is_file())
# print(Path('backup.py').stat().st_size)
# print(Path('backup.py').stat())

# print(Path(Path.cwd()) / 'test3')
# for f in Path(Path.cwd()).iterdir():
#     print(f)

# dirs = [str(f) for f in Path(Path.cwd()).iterdir()]
# print(dirs)

# print(Path(__file__).parent)
# print(Path('backup.py').suffix)
# print(list(map(lambda x: str(x)[18:], Path.cwd().glob("*.py"))))
# print(Counter(path.suffix for path in Path.cwd().iterdir()))

# print(Path.cwd())

# try:
#     rmtree(Path(Path.cwd() / 'test3'))
# except FileNotFoundError: 
#     print('нет такого каталога')    

# print(Path('backup.py').stat().st_ctime)
# print(Path('backup.py').stat().st_mtime)

# dir_timestamp = Path('build').stat().st_mtime
# print(dir_timestamp)
# dir_delta = (time.time() - dir_timestamp) #// (60 * 60 * 24) 
# print(dir_delta)
# print(dir_delta // (60 * 60 * 24) )
rmtree(Path('test4'))