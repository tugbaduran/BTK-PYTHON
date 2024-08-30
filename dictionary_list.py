# plakalar={"Kocaeli": 41 , "İstanbul": 34}

# print(plakalar["Kocaeli"])
# print(plakalar["İstanbul"])

# plakalar["Ankara"]= 6
# plakalar["Kocaeli"]= "new value"
# print(plakalar)

users={
  "Tuğba Duran":{
    "age": 21,
    "roles": ["users"],
    "email": "tugba@gmail.com",
    "address": "İstanbul",
    "phone": 123456
  },
  "Tuğçe Duran":{
    "age": 22,
    "roles": ["admin","users"],
    "email": "tugce@gmail.com",
    "address": "İstanbul",
    "phone": 654847
}
}

print(users["Tuğba Duran"])
print(users["Tuğba Duran"] ["age"])
print(users["Tuğba Duran"] ["email"])
print(users["Tuğba Duran"] ["address"])
print(users["Tuğçe Duran"] ["roles"][0])