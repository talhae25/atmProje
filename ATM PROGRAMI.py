bakiye=4

print("atm programına hoş geldiniz")
print("Bakiye görüntülemek istiyorsanız lütfen '1'e basınız./n")
print("Hesabınızdan para çekmek istiyorsanız lütfen '2'ye basınız./n")
print("Hesabınıza para yatırmak istiyorsanız lütfen '3'e basınız./n")
print("ATM'den çıkmak istiyorsanız lütfen '4'e basınız./n")



while True:
      t=input("Yapmak istediğiniz işlemi seçiniz")
      if t =="1":
            print("Bakiyeniz:",bakiye)

      elif t =="2":
            miktar =int(input("miktarı girin:"))
            if miktar > bakiye:
                  print("Bakiyeniz yetersidir.")
            else:
                  bakiye = bakiye - miktar
                  print("Bakiyeniz:", bakiye)


      elif t == "3":
            miktar = int(input("miktarı girin:"))



            bakiye = bakiye + miktar
            print("Bakiyeniz:", bakiye)
      elif t == "4":
            print("'ATM'den çıkış yapılıyor...")
            break