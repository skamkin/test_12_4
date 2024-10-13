import logging
import Runner
import unittest
import inspect

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner('Sergey', -5)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning('Неверная скорость для Runner', exc_info=exc)



    def test_run(self):
         try:
            runner_2 = Runner( 'Anton', 5)
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
         except ValueError as exc:
             logging.warning('Неверный тип данных для объекта Runner', exc_info=exc)


    def test_challenge(self):
        runner_3 = Runner('Kirill')
        runner_4 = Runner('Denis')
        for i in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)



