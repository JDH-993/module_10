from fileinput import close
from threading import Thread
from time import sleep
from datetime import datetime
from turtledemo.penrose import start


def write_words(word_count, file_name):
    a = open(file_name, 'a' , encoding='utf-8')
    b = open(file_name, 'a' , encoding='utf-8')
    for i in range(1, word_count+1):
        a.write(f'Какое-то слово № {i}\n')
    print(f"Завершилась запись в файл {file_name}")
    sleep(0.1)
    close()


ts = datetime.now()
write_words(10,"example1")
write_words(30, 'example2')
write_words(200, '.example3')
write_words(100, 'example4')
tc = datetime.now()
print(tc - ts)

ts1 = datetime.now()
th = Thread(target=write_words, args=(10, 'example5'))
th1 = Thread(target=write_words, args=(30, 'example6'))
th2 = Thread(target=write_words, args=(200, 'example7'))
th3 = Thread(target=write_words, args=(100, 'example8'))



th.start()
th1.start()
th2.start()
th3.start()



th.join()
th1.join()
th2.join()
th3.join()


tc1 = datetime.now()

print(tc1 - ts1)


