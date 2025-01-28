# "Простые Юнит-Тесты"
from pickle import FALSE
from symtable import Class

import module_12_1
import unittest


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test = module_12_1.Runner('Mark')
        for i in range (10):
            test.walk()
        self.assertEqual(test.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test = module_12_1.Runner('Yan')
        for i in range (10):
            test.run()
        self.assertEqual(test.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_1 = module_12_1.Runner('Mark')
        test_2 = module_12_1.Runner('Yan')
        for i in range (10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)


if __name__ == '__main__':
    unittest.main()

