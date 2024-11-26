# "Найдёт везде"


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        del_sings = (',', '.', '=', '!', '?', ';', ':', ' - ', ' \n')
        all_words = {}
        for file in self.file_names:
            with open(file, encoding= 'utf-8') as an_open_file:
                str_file = an_open_file.read().lower()
                for i in del_sings:
                    str_file = str_file.replace(i, ' ')
                all_words[file] = str_file.split()
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            poz_number = 0
            if word.lower() in words:
                while not word.lower() in words[poz_number]:
                    poz_number += 1
                find_dict[name] = poz_number + 1
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            number = 0
            if word.lower() in words:
                for i in words:
                    if word.lower() in i:
                        number += 1
                count_dict[name] = number
        return count_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_files.txt', 'test_files_2.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего