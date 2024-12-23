# "Потоки гостей в кафе"

import threading
import queue
from time import sleep
from random import randint


class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time = randint(3, 10)
        sleep(time)


class Cafe():
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in range(len(guests)):
            if len(self.tables) > i:
                if self.tables[i].guest is None:
                    self.tables[i].guest = guests[i].name
                    th = guests[i]
                    th.start()
                    print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
            else:
                self.queue.put(guests[i].name)
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        i = 0
        while not self.queue.empty() or self.empty_table():
            #for i in range(len(self.tables)):
            if not (tables[i].guest is None) and not (guests[i].is_alive()):
                guests[i].join()
                print(f'{tables[i].guest} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {tables[i].number} свободен')
                if not self.queue.empty():
                    guest = self.queue.get()
                    tables[i].guest = guest
                    print(f'{tables[i].guest} вышел(-ла) из очереди и сел(-а) за стол номер {tables[i].number}')
                    th = Guest(guest)
                    th.start()
                else:
                    tables[i].guest = None
            i += 1
            if i == len(self.tables):
                i = 0

    def empty_table(self):
        for i in range(len(self.tables)):
            if not (self.tables[i].guest is None):
                return True
        else: return False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()