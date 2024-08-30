# Bankamatik uygulaması

TugbaHesap={

  "ad": "Tuğba Duran",
  "hesapNo": "1324567",
  "bakiye": 3000,
  "ekHesap": 2000

}


TugceHesap={

  "ad": "Tuğçe Duran",
  "hesapNo": "4534567",
  "bakiye": 2000,
  "ekHesap": 1000

}


def paraCek(hesap,miktar):
  print(f"Merhaba {hesap['ad']}" )

  if(hesap["bakiye"]>= miktar):
    hesap["bakiye"] -= miktar
    print("Paranızı alabilirsiniz.")
    bakiySorgulama(hesap)

  else:
    toplam= hesap["bakiye"] + hesap["ekHesap"]

    if(toplam >= miktar):

      ekHesapKullanimi = input("Ek hesap kullanılsın mı (e/h)")

      if ekHesapKullanimi == "e":
        ekHesapKullanilacakMiktar= miktar-hesap["bakiye"]
        hesap["bakiye"]= 0
        hesap["ekHesap"] -= ekHesapKullanilacakMiktar
        print("Paranınızı alabilirsiniz")
        bakiySorgulama(hesap)

      else:
        print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır")
      
    else:
      print("Üzgünüz bakiye yetersiz.")
      bakiySorgulama(hesap)

def bakiySorgulama(hesap):
  print(f"{hesap['hesapNo']} nolu hesabınızda  {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(TugbaHesap, 3000)


print("***********************")

paraCek(TugbaHesap, 2000)
