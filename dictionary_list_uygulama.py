# soru 1 kulanıcıdan girilen 3 öğrncinin bilgilerini dictionary liste içinde saklayınız?
ogrenciler={}

number=input("öğrenci no: ")
name=input("öğrenci ad: ")
surname=input("öğrenci soyad: ")
phone=input("öğrenci tel: ")

ogrenciler.update({
number:{

  "ad": name,
  "soyad": surname,
  "tel" : phone
}
})


number=input("öğrenci no: ")
name=input("öğrenci ad: ")
surname=input("öğrenci soyad: ")
phone=input("öğrenci tel: ")

# ogrenciler[number]={

#   "ad": name,
#   "soyad": surname,
#   "tel" : phone

# }

ogrenciler.update({
number:{

  "ad": name,
  "soyad": surname,
  "tel" : phone
}
})

number=input("öğrenci no: ")
name=input("öğrenci ad: ")
surname=input("öğrenci soyad: ")
phone=input("öğrenci tel: ")

ogrenciler.update({
number:{

  "ad": name,
  "soyad": surname,
  "tel" : phone
}
})
print('*'*50)

#soru 2 öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin?

ogrNo=input("öğrenci no: ")
ogrenci=ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve numarası ise {ogrenci['tel']}")