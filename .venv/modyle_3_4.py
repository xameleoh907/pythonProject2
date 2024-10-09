#Однокоренные

def single_root_words (root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.upper() in other_words[i].upper() or other_words[i].upper() in root_word.upper():
        # Проверка входит root_word в элемент кортежа other_words[i] или наоборот
            same_words.append((other_words[i]))
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)