maasAli= 5000 # maasAli burada değişkenimiz oluyor. 5000'nde maasAli'nin değeri oluyor.
maasAhmet= 4000
vergi= 0.27

print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))

#Değişken Tanımlama Kuralları

# Rakam ile başlayamaz.
# 1number= 7 olamaz. nuber1=80 şeklinde olur yada _number=9 şeklinde de olur.

number1=10
print(number1)

number1=20
print(number1)

number1+=30
print(number1)

#Büyük Küçük harf duyarlılığı vardır.

age=20
AGE=30

print(age)
print(AGE)

#Türkçe karakter kullanılmaz. Yani örneğin "yaş" değil de "yas" yada "age".

yas=20
_age=20

x=1            #int
y=2.3          #float
name= "Tuğçe"  #string
isStudent=True #bool

a="10"
b="20" 
print(a+b)  # Ekran çıktısı 1020 olacaK. Çünkü buradaki + birleştirme görevinde.

firstName="Tuğba"
lastName=" Duran"
print(firstName+lastName) # Ekran çıktısı Tuğba Duran olacaK. Çünkü buradaki + birleştirme görevinde.

# x,y,name,isStudent=(1,2.3,"Tuğçe",True) bu şekilde de değişkenleri tek satırda tanımlayabiliriz.