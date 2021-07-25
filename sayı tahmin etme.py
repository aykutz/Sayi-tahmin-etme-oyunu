import random
import time

print("""*************************************************************

SAYI TAHMİN OYUNU

1 ile 50 arasındaki sayıyı tahmin edin.

Tahmin için 5 hakkınız vardır !!!!!

*************************************************************
""")

rastgele_sayı = random.randint(1,50) // Eğer değeri değiştirmek isterseniz burdan ayarlayabilirsiniz.
tahmin_hakkı = 5

while True:

    tahmin = int(input("tahmininiz: "))


    if(tahmin < rastgele_sayı):
        print("tahmininiz kontrol ediliyor...")
        time.sleep(1)

        print("daha yüksek bir sayı girin")
        tahmin_hakkı -=1
        print("tahmin hakkınız: ",tahmin_hakkı)

    elif(tahmin > rastgele_sayı):
        print("tahmininiz kontrol ediliyor...")
        time.sleep(1)

        print("daha küçük bir sayı girin")
        tahmin_hakkı -= 1
        print("tahmin hakkınız: ", tahmin_hakkı)

    else:
        print("tahmininiz kontrol ediliyor...")
        time.sleep(1)
        print("TEBRİKLER! saymımız: ",rastgele_sayı)
        break
    if(tahmin_hakkı == 0):
        print("üzgünüm bilemedin tahmin hakkın kalmadı")
        print("sayımız: ",rastgele_sayı)
        break
