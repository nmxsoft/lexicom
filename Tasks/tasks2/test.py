def file_name(names: list) -> list:
    valid_names = []
    len_max = len(max(names, key=len))

    for name in names:
        # Проверка на повтор символа в имени
        chars = set()
        for char in name:
            if char not in chars:
                chars.add(char)
            else:
                raise Exception(f'Недопустим повтор букв имени файла: {name}')
        del chars
        # Дополнение имени до максимального значения
        if len(name) >= len_max:
            valid_names.append(name)
        else:
            valid_names.append(''.join([name, '_' * (len_max - len(name))]))

    return valid_names
