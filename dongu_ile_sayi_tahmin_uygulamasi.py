# -100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)

#    ** "random modülü" için "python random" şeklinde arama yapın.

#    ** 100 üzerinden puanlama yapın. Her soru 20 puan.

#    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.


import random
rastgele=random.randint(1,100)
can= int(input("Kaç hakkınız olsun: "))
hak=can
sayac=0

while hak>0:
  hak -=1
  sayac +=1
  tahmin=int(input("Tahmin Ettiğiniz Sayı: "))

  if rastgele==tahmin:
   print(f"Tebrikler {sayac}. defa bildiniz Toplam puanınız: {100-(100/can)*(sayac-1)}.")
   break

  elif rastgele>tahmin:
   print("Rastgele Gelen Sayı Tahmininizden Yukarı")

  else:
   print("Rastgele Gelen Sayı Tahmininizden Aşağı")

  if hak==0:
   print(f"Hakkınız bitti. Tutulan sayı: {rastgele}")


