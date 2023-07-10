import datetime

"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""


class Timer:
    def __enter__(self):
        self.first = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = datetime.datetime.now() - self.first
        return self.elapsed_time

with Timer() as timer:
    pass

print("Execution time:", timer.elapsed_time)
