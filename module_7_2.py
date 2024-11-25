# "Записать и запомнить"


def custom_write(file_name, strings):
    result_dict = {}
    line_number = 0
    name = file_name
    file = open(name, 'a', encoding='utf-8')
    for string in strings:
        key_tuple = []
        line_number += 1
        key_tuple.append(line_number)
        key_tuple.append(file.tell())
        result_dict[tuple(key_tuple)] = string
        file.write(string + '\n')
    return result_dict


    pass


if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
