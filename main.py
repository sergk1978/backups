from backup import Bak
import time



if __name__ == '__main__':
    bak = Bak('path.txt')
    start = bak.time_copy()   # старт программы
    bak.create_folder()       # создание папки с датой
    bak.backup()              # копирование с диска на диск
    stop = bak.time_copy()    # завершение программы
    time_end = stop-start
    print(f'Время выполнения: - {str(time_end).split('.')[0]} размер: - {bak.s.format_size()}')
    input('Нажмите Enter для выхода')
