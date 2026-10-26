import shutil

def bakup():
    try:
        src = 'D:\\Python_projects\\source_обмен'
        dst = 'D:\\Python_projects\\destination_обмен'
        #shutil.copytree(src, dst, dirs_exist_ok=True)
        print('OK')
    except FileNotFoundError:
        print("Не удается найти указанный путь")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bakup()

