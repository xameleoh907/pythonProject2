# "Методы Юнит-тестирования"


import module_12_2
import unittest


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.list_runners = [
            module_12_2.Runner('Усэйн', 10),
            module_12_2.Runner('Андрей', 9),
            module_12_2.Runner('Ник', 3)
            ]

    @classmethod
    def tearDownClass(cls):
        for i, f in cls.all_results.items():
            print("{}:".format(f))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        finish_1 = module_12_2.Tournament(90, self.list_runners[0], self.list_runners[2])
        result = finish_1.start()
        self.assertTrue(list(result.values())[-1] == "Ник")
        self.all_results[1] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        finish_2 = module_12_2.Tournament(90, self.list_runners[1], self.list_runners[2])
        result = finish_2.start()
        self.assertTrue(list(result.values())[-1] == "Ник")
        self.all_results[2] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        finish_3 = module_12_2.Tournament(90, self.list_runners[0], self.list_runners[1], self.list_runners[2])
        result = finish_3.start()
        self.assertTrue(list(result.values())[-1] == "Ник")
        self.all_results[3] = result


if __name__ == '__main__':
    unittest.main()

'''
Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.

Данная ошибка возникает на небольших дистанциях при условии, что начинает забег спринтер с меньшей скоростью.
Решение:
Сортировка бегунов в методе start класса Tournament по скорости бега от большего к меньшему.
'''