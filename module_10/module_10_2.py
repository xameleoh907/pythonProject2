# "За честь и отвагу!"


import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.number_of_players = 100

    def bittle_nime(self, name, power):
        count = 0
        while self.number_of_players:
            time.sleep(1)
            self.number_of_players -= self.power
            count += 1
            print(f'{self.name} сражается {count} дней, осталось {self.number_of_players} воинов.')
        print(f'{self.name} одержал победу спустя {count} дней(дня)!')


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.bittle_nime(self.name, self.power)


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')