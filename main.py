from backup import Bak



if __name__ == '__main__':
    bak = Bak()
    start = bak.time_copy()
    bak.backup()
    stop = bak.time_copy()
    time_end = stop-start
    print(f'Время выполнения: - {time_end}')
