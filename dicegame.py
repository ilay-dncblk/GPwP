import random
from asyncio.windows_events import NULL
import os
import time 

yapayzeka=NULL
kullanıcı=NULL
toplam = 0
i=0
kullanıcıbakiye=10000

def zarGorsellestir(zar):
    zar1 = """------------------
|                |
|                |
|       1        |
|                |
|                |
------------------"""

    zar2 = """------------------
|                |
|  2             |
|                |
|            2   |
|                |
------------------"""

    zar3 = """------------------
| 3              |
|                |
|       3        |
|                |
|             3  |
------------------"""

    zar4 = """------------------
|  4          4  |
|                |
|                |
|                |
|  4          4  |
------------------"""

    zar5 = """------------------
|  5          5  |
|                |
|       5        |
|                |
|  5          5  |
------------------"""

    zar6 = """------------------
| 6            6 |
|                |
| 6            6 |
|                |
| 6            6 |
------------------"""

    if zar == 1:
        print(zar1)
    elif zar == 2:
        print(zar2)
    elif zar == 3:
        print(zar3)
    elif zar == 4:
        print(zar4)
    elif zar == 5:
        print(zar5)
    else :
        print(zar6)

def işleme():
        print(".", end=" " )
        time.sleep(0.5)
        print(".", end=" " )
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
while(True):
    while(True):
        print(kullanıcıbakiye, "Tl paranız var. İstediğiniz gibi harcamanız dileğiyle")
        masaseçimi=['100 Tl lik masa için','500 Tl lik masa için ','1000 Tl lik masa için','2500 Tl lik masa için', \
            '5.000 Tl lik masa için ','10.000 Tl lik masa için','25.000 Tl lik masa için ','50.000 Tl lik masa için ','100.000Tl lik masa için']
        b = 0
        for j in masaseçimi:
            b = b + 1
            print( b,".",j)
            time.sleep(0.5)
        masaseçimi=input("Lütfen oynamak istedğiniz masa numarasını giriniz. : ")
        
        if(masaseçimi=="1"):
            bahis=100
        elif(masaseçimi=="2"):
            bahis=500
        elif(masaseçimi=="3"):
            bahis=1000
        elif(masaseçimi=="4"):
            bahis=2500
        elif(masaseçimi=="5"):
            bahis=5000
        elif(masaseçimi=="6"):
            bahis=10000
        elif(masaseçimi=="7"):
            bahis=25000
        elif(masaseçimi=="8"):
            bahis=50000
        elif(masaseçimi=="9"):
            bahis=100000
        os.system('CLS')
        if (kullanıcıbakiye<bahis):
            print("\nBakiyenizden yüksek masa seçimi yaptınız. Tekrar deneyiniz. \n")
        else:
            break
    kullanıcıbakiye=kullanıcıbakiye-bahis
    
   
    while(True):
        yapayzeka  = random.randint(1,6)
        print('Sıra yapay zekanın, yapay zekaya gelen zar:' )
        time.sleep(0.5)
        zarGorsellestir(yapayzeka)
        time.sleep(0.5)
        kullanici=input("Sıra sizde, zar atmak için enter tuşuna basın:")
        if (kullanici==""):
            kullanıcı = random.randint(1,6)
            print('size gelen zar:' )
            time.sleep(0.5)
            zarGorsellestir(kullanıcı)
            time.sleep(0.5)
        if(yapayzeka > kullanıcı):
            print("yapay zeka kazandı")
            toplam = toplam + 1
    
        elif(kullanıcı > yapayzeka):
            print("siz kazandınız.")
            toplam = toplam - 1

        elif(kullanıcı==yapayzeka):
            i=i-1
            print("Beraberlik dolayısıyla tekrar zar atılmalı.")
        i=i+1
        if(i==3):
            i=0
            break
        print("Diğer tura geçtiniz.")
        işleme()


    os.system('CLS')
    print("Oyun sonu.")

    if (toplam<0):
        print("Siz kazandınız.")
        kullanıcıbakiye = kullanıcıbakiye + bahis*2
        print(kullanıcıbakiye)

    elif(toplam>0):
        print("Yapay zeka kazandı.")
        print("Kalan bakiyeniz: ", kullanıcıbakiye)


    a=(input("oyundan çıkmak için 0 a bas. Tekrar oynamak için enter a basınız."))
    if (a=='0'):
        break 
