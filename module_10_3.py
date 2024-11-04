import threading
from random import randint
from time import sleep
lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            sleep(0.001)
            k = randint(50, 500)
            self.balance = self.balance + k
            print(f"Пополнение: {k}. Баланс: {self.balance}")
            if self.balance >= 500 and lock.locked() == True:
                lock.release()


    def take(self):
        for i in range(100):
            sleep(0.001)
            a = randint(50, 500)
            print(f"Запрос на {a}")
            if a <= self.balance:
                self.balance = self.balance - a
                print(f"Снятие: {a}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')