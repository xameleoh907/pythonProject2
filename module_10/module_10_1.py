# "Потоковая запись в файлы"
import threading
import time
from time import sleep
import time
from turtledemo.penrose import start


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какоое-то слово №{str(i + 1)}\n')
            time.sleep(0.1)
        else:
            print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f'Работа потоков 1: {end_time - start_time}')

start_time = time.time()
thread_5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
thread_5.join()
thread_6.join()
thread_7.join()
thread_8.join()
end_time = time.time()
print(f'Работа потоков 2: {end_time - start_time}')