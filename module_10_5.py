from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    all_data = []
    a = open(name, 'r')
    for i in a:
        all_data.append(i)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

dt = datetime.now()
for i in filenames:
    read_info(i)
dt2 = datetime.now()
print(dt2 - dt)

# Многопроцессный

#if __name__ == '__main__':
#    r = datetime.now()
#    with Pool(5) as p:
#        p.map(read_info, filenames)
#    r1 = datetime.now()
#    print(r1-r)

