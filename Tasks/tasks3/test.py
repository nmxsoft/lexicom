from tasks1.test import service
from tasks2.test import file_name


if __name__ == '__main__':
    # Вызов функции задачи 3.1
    base = service()
    for name in base:
        print(name + ':', base[name])
    # Вызов функции задачи 3.2
    print(file_name(['qwer', 'qwansd567', 'sdfgr', 'fghj']))
