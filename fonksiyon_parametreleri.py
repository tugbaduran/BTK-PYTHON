# def changeName(n):
#   n= 'ada'
# name="yiğit"

# changeName(name)
# print(name)


# def change(n):

#   n[0]="İstabul"

# sehirler=["ankara", "izmir"]

# change(sehirler[:]) #slicing
# print(sehirler)



# def add(*params):
#   print(params)
#   return sum((params))
  

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60))


# def add(*params):
#   sum=0

#   for n in params:
#     sum= sum+n
#   return sum
  

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60))




def displayUser(**args):
  for key, value in args.items():
    print('{} is {} '.format(key,value))

displayUser(name="Tuğba", age=21, city="İstanbul")
displayUser(name="Tuğçe", age=22, city="Bilecik", phone="12345")
displayUser(name="Tülay", age=18, citiy="Kocaeli", phone="76594", email="tulay@duran.com")


def myFunc(a,b,*args,**kwargs):
  print(a)
  print(b)
  print(args)
  print(kwargs)

myFunc(10,20,30,40,50, key1="value1", key2="value2")