import threading
from turtledemo.penrose import start
from time import sleep

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def ricari(self, name, power):
        p = 0
        lock = threading.Lock()
        lock.acquire()
        for i in range(100, 0 , -power):
            p = p + 1
            sleep(1)
            print(f"{name} сражается {p}..., осталось {i-power} воинов.")
        print(f"{name} одержал победу спустя {p} дней(дня)!")

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.ricari(self.name, self.power)


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')

