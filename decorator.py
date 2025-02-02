import time
import random
from functools import wraps
n = int(input())
def logging_decorator(func):
    @wraps(func)
    def wrapper():
        global n
        print("Вызванна функция ", func.__name__," с аргументом ",n)
        func()
        
        
    return wrapper



def timing_decotator(func):
    @wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Функция",func.__name__, "выполнена за",elapsed_time ,"секунд")
    return wrapper

@logging_decorator
@timing_decotator
def count():
    global n
    a = 0
    for i in range(1,n+1):
        a += i
    print(a)

count()



@logging_decorator
@timing_decotator
def random_list():
    global n
    list = []
    for i in range(n):
        num = random.randint(0,1000)
        list.append(num)
    print(*sorted(list))

random_list()






