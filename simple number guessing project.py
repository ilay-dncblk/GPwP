import random
sayi = random.randint(1,10)
count = 0
kullanıcı_verisi = 0 

while(True):
    kullanıcı_verisi = input("Tahmininizi giriniz. :")
    count +=1
    if (kullanıcı_verisi=="çık"):
        print("Oyundan çıktınız.")
        break
    kullanıcı_verisi=int(kullanıcı_verisi)
    if (kullanıcı_verisi > sayi):
        print("Daha küçük bir sayı giriniz.")
    elif(kullanıcı_verisi<sayi):
        print("daha büyük bir sayı giriniz.")
    else:
        print("kazandınz")
        print("Sayıyı bulduğunuz turun sayın :", str(count))
        break
