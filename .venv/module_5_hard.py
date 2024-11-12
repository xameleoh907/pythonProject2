# Свой YouTube
from time import sleep

class User:
    """
    Класс пользователя содержит атрибуты:
    nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    """
    Класс видео содержит атрибуты:
    title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

class UrTube:
    """
    Класс UrToub содержит:
    атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    +Методы: log_in, который принимает на вход аргументы: nickname, password
    +Метод register, который принимает три аргумента: nickname, password, age
    +Метод log_out для сброса текущего пользователя на None.
    +Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos
    +Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово
    Метод watch_video, который принимает название фильма
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь с именем {nickname} уже существует')
                return
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Вход пользователем {nickname} выполнен успешно')

    def log_out(self):
        self.current_user = None

    def add(self, *args): # добавление видео
            for video in args:
                if isinstance(video, (str, Video)) and video not in self.videos:
                    self.videos.append(video)

    def get_videos(self, search_query): # поиск видео по совпадению
        search_video = []
        for video in self.videos:
             if search_query.lower() in video.title.lower():
                 search_video.append(video.title)
        if search_video:
            return search_video
        else: f'По вашему запросу ничего не найдено'

    def watch_video(self,title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if title == video.title:
                    if video.adult_mode and self.current_user.age < 17:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        while video.duration > video.time_now:
                            video.time_now += 1
                            print(video.time_now, end=' ')
                            sleep(1)
                        print('Конец видео')
                        video.time_now = 0




if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video('Лучший язык программирования 2024 года', 200)

    # Добавление видео
    ur.add(v1, v2, v3)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.log_out()
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')