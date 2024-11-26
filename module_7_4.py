# "Форматирование строк"


class Competitions:

    def __init__(self, name: str, team_num: int, score: int, team_time: float):
        self.name = name
        self.team_num = team_num
        self.score = score
        self.team_time = team_time

    def teams_num(self):
        print('В команде %s участников: %s !' % (self.name, self.team_num))

    def scores(self):
        print('Команда {} решила задач: {} !'.format(self.name, self.score))

    def teams_time(self):
        print('{} решили задачи за {} c'.format(self.name, self.team_time))


class ResultCompetitions():
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def result(self):
        print('Итого сегодня в командах участников: %s и %s !' % (self.team1.team_num, self.team2.team_num))
        print(f'Команды решили {self.team1.score} и {self.team2.score} задач.')
        print(f'Результат битвы: {self.result_battle()}')
        print(f'Сегодня было решено {self.team1.score + self.team2.score} задач, в среднем по'
              f' {round((self.team1.team_time + self.team2.team_time) / (self.team1.score + self.team2.score), 2)} '
              f'секунды на задачу!')
        print('Сегодня было решено {} задач, в среднем по {:.2f} секунды на задачу!'
              .format(self.team1.score + self.team2.score, (self.team1.team_time + self.team2.team_time) /
                      (self.team1.score + self.team2.score)))
        print('Сегодня было решено %s задач, в среднем по %.2f секунды на задачу!' % (
            self.team1.score + self.team2.score, (self.team1.team_time + self.team2.team_time) /
            (self.team1.score + self.team2.score)))


    def result_battle(self):
        if (self.team1.score > self.team2.score or self.team1.score == self.team2.score
                and self.team1.team_time > self.team2.team_time):
            return f'Победа команды {self.team1.name}'
        elif (self.team1.score < self.team2.score or self.team1.score == self.team2.score
              and self.team1.team_time < self.team2.team_time):
            return f'Победа команды {self.team2.name}'
        else: return 'Ничья!'



# Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

team_1 = Competitions('Мастера кода', team1_num, score_1, team1_time)
team_2 = Competitions('Волшебники данных', team2_num, score_2, team2_time)
team_1.teams_num()
team_1.scores()
team_1.teams_time()
team_2.teams_num()
team_2.scores()
team_2.teams_time()
result = ResultCompetitions(team_1, team_2)
result.result()
