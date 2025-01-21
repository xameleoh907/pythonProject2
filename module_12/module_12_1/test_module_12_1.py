# "Простые Юнит-Тесты"
from symtable import Class

import module_12_1
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test = module_12_1.Runner('Mark')
        for i in range (10):
            test.walk()
        self.assertEqual(test.distance, 50)

    def test_run(self):
        test = module_12_1.Runner('Yan')
        for i in range (10):
            test.run()
        self.assertEqual(test.distance, 100)

    def test_challenge(self):
        test_1 = module_12_1.Runner('Mark')
        test_2 = module_12_1.Runner('Yan')
        for i in range (10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)


if __name__ == '__main__':
    unittest.main()

