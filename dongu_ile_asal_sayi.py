girilenSayi=int(input("Bir sayı giriniz: "))
asalmi= True

if girilenSayi==1:
  asalmi= False

for i in range(2,girilenSayi):

  if girilenSayi%i==0:
    asalmi=False
    break
if asalmi:
  print("Sayı asaldır")
else:
  print(f"Girilen sayı {girilenSayi} sayı asal değil.")