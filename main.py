from backup import Bak



if __name__ == '__main__':
    bak = Bak('path.txt')
    start = bak.time_copy()   # время старта программы
    bak.d.dir_delete()        # удаление папок в хранилище по истечении x дней
    bak.create_folder()       # создание папки с датой
    bak.backup()              # копирование с диска на диск
    stop = bak.time_copy()    # время завершения программы
    time_end = stop-start     # продолжительность работы 
    print(f'Время выполнения: - {str(time_end).split('.')[0]} общий размер папки: - {bak.s.format_size()}')
    print("\n© Автор программы: Сергей Куршаков\n")
    input('Нажмите Enter для выхода...')

