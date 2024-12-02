# "Генераторы"


def all_variants(text: str):
    start_slice = 0
    end_slice = 0
    offset = 1
    while end_slice < len(text):
        slice = text[start_slice:end_slice+1]
        yield slice
        start_slice += 1
        end_slice += 1
        if offset < len(text) and end_slice == len(text):
            start_slice = 0
            end_slice = offset
            offset += 1




# Пример работы функции:
a = all_variants("abcde")
for i in a:
    print(i)