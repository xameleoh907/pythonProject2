#Задача "Многопроцессное считывание"
import time
import  multiprocessing
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            all_data.append(file.readline())
            if not file.readline():
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()
for file in filenames:
    read_info(file)
end_time = time.time()
print('Время выполнения линейного кода: ', end_time - start_time)
#Время выполнения линейного кода:  8.099064588546753


if __name__ == '__main__':

    pool = multiprocessing.Pool()
    with Pool(processes=len(filenames)) as pool:
        start_time = time.time()
        pool.map(read_info, filenames)
        end_time = time.time()
    print('Время выполнения многопроцессного кода: ', end_time - start_time)
    #Время выполнения линейного кода:  3.6711533069610596