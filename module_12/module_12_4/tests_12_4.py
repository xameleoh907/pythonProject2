import logging
import unittest
import module_12_4


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            test = module_12_4.Runner('Mark', -5)
            logging.info('test_walk выполнен без ошибок')
            for i in range (10):
                test.walk()
            self.assertEqual(test.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            test = module_12_4.Runner(000)
            for i in range (10):
                test.run()
            self.assertEqual(test.distance, 100)
            logging.info('test_run выполнен без ошибок')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',
                            exc_info=True)

    def test_challenge(self):
        test_1 = module_12_4.Runner('Mark')
        test_2 = module_12_4.Runner('Yan')
        for i in range (10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':

    unittest.main()