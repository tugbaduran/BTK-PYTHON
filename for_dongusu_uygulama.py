# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır? # 2- Sayilar listesinde sayıların toplamı kaçtır?
# sayilar=[1,3,5,7,9,12,19,21]
# for sayi in sayilar: 
#   if(sayi % 3==0):
#     print(sayi)

# 3- Sayilar listesindeki tek sayıların karesini alınız.

# sayilar=[1,3,5,7,9,12,19,21]
# for sayi in sayilar: 
#   if(sayi % 2==1):
#     print(sayi**2)


# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
# sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# for sehir in sehirler:
#   if (len (sehir) <=5):
#     print(sehir)



# 5- Ürünlerin fiyatları toplamı nedir ?

# urunler= [
# {'name': 'samsung S6', 'price': '3000' },
# {'name': 'samsung S7', 'price': '4000' },
# {'name': 'samsung S8', 'price': '5000' },
# {'name': 'samsung S9','price': '6000' },
# {'name': 'samsung S10', 'price': '7000' }
# ]


# toplam=0
# for urun in urunler:
#  fiyat= int(urun['price'])
#  toplam += fiyat
# print("toplam ürün fiyatı", toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

urunler= [
{'name': 'samsung S6', 'price': '3000' },
{'name': 'samsung S7', 'price': '4000' },
{'name': 'samsung S8', 'price': '5000' },
{'name': 'samsung S9','price': '6000' },
{'name': 'samsung S10', 'price': '7000' }
]

for urun in urunler:
  if (int(urun['price'])<=5000):
   print(urun['name'])

