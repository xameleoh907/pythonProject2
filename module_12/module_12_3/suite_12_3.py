# Задача "Заморозка кейсов"


import unittest
import test_module_12_1 as RunnerTest
import test_module_12_2 as TournamentTest


test_runner = unittest.TestSuite()
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_runner)