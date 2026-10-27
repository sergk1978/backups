import shutil


def file_read():
    with open('path.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines


def bakup():
    try:
        path = file_read()
        src = path[0][0:-1]
        dst = path[1]
        print(src)
        print(dst)
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print("Копирование успешно завершено!")
    except PermissionError:
        print(f"Устройство не готово {src}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bakup()

