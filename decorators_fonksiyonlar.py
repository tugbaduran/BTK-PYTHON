# def my_decorator(func):
#   def wapper(name):
#     print("Fonksiyondan önceki işlemler")
#     func(name)
#     print("Fonksiyondan sonraki işlemler")
#   return wapper

# @my_decorator
# def sayHello(name):
#   print("Hello", name)
# sayHello("Tuğba")

# def sayGreeting():
#   print("greeting")

# # sayHello= my_decorator(sayHello)
# # sayGreeting= my_decorator(sayGreeting)
# # sayGreeting()
# # #sayHello()


import math
import time

def calculate_time(func):
  def inner(*args, **kwargs):

    start = time.time()
    time.sleep(1)

    func(*args,**kwargs)

    finish= time.time()
    print("fonksiyon " + func.__name__ +" "+ str(finish-start)+ "saniye sürdü.")

  return inner

@calculate_time
def us_alma(a,b):
  print(math.pow(a,b))


@calculate_time
def faktoriyel(num):
  print(math.factorial(num))


def toplama(a,b):
  print(a+b)

us_alma(2,3)
faktoriyel(4)
toplama(10,20)