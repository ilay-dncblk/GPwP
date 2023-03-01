import random
oyuntahtasi=[' ' for x in range(10)]

def ekrangöster():
    print(' '+oyuntahtasi[1]+'-'+'-'+oyuntahtasi[2]+'-'+'-'+oyuntahtasi[3])
    print('|'+' '+' '+'|'+' '+' '+'|')
    print(' '+oyuntahtasi[4]+'-'+'-'+oyuntahtasi[5]+'-'+'-'+oyuntahtasi[6])
    print('|'+' '+' '+'|'+' '+' '+'|')
    print(' '+oyuntahtasi[7]+'-'+'-'+oyuntahtasi[8]+'-'+'-'+oyuntahtasi[9])

def üctas(harf,konum):
    oyuntahtasi[konum]=harf

def alanbosmu(konum):
    return oyuntahtasi[konum] ==' '

def tahtadolu():
    if oyuntahtasi.count(' ')>1:
        return False
    else:
        return True

def kazanan(oyuntahtasi,harf):
    return (oyuntahtasi[1]==harf and oyuntahtasi[2]==harf and oyuntahtasi[3]==harf) or \
        (oyuntahtasi[4]==harf and oyuntahtasi[5]==harf and oyuntahtasi[6]==harf) or \
        (oyuntahtasi[7]==harf and oyuntahtasi[8]==harf and oyuntahtasi[9]==harf) or \
        (oyuntahtasi[1]==harf and oyuntahtasi[4]==harf and oyuntahtasi[7]==harf) or \
        (oyuntahtasi[3]==harf and oyuntahtasi[5]==harf and oyuntahtasi[7]==harf) or \
        (oyuntahtasi[1]==harf and oyuntahtasi[5]==harf and oyuntahtasi[9]==harf) or \
        (oyuntahtasi[2]==harf and oyuntahtasi[5]==harf and oyuntahtasi[8]==harf) or \
        (oyuntahtasi[3]==harf and oyuntahtasi[6]==harf and oyuntahtasi[9]==harf)
  
def oyuncuhareketi():
    konum=int(input("1-9 arasında bir konum giriniz :"))
    if alanbosmu(konum):
        üctas('X',konum)
        if kazanan(oyuntahtasi,'X'):
            ekrangöster()
            print("kazandınız.")
            exit()
        ekrangöster()
    else:
        print("Girdiğiniz alan dolu, Tekrar konum giriniz:")
        oyuncuhareketi()

def pchareket():
    musaitkonumlar = [konum for konum, harf in enumerate(oyuntahtasi) if harf == ' ' and konum != 0]

    hareket = 0

    for harf in ['O','X']:
        for i in musaitkonumlar:
            kopyatahta = oyuntahtasi[:]
            kopyatahta[i] = harf 
            if kazanan(kopyatahta, harf):
                hareket=i
                return hareket
    köşeler = []

    for i in musaitkonumlar:
        if i in [1,3,7,9]:
            köşeler.append(i)
    if len(köşeler) > 0:
        hareket=random.choice(köşeler)
        return hareket
    if 5 not in musaitkonumlar:
        hareket != 5
        return hareket
    
    içerisi = []

    for i in musaitkonumlar:
        if i in [2,4,5,6,8]:
            içerisi.append(i)
    if len(içerisi) > 0:
        hareket=random.choice(içerisi)
        return hareket

def oyun():
    print("XOX oyununa hoşgeldiniz.")
    ekrangöster()
    while not tahtadolu():
        oyuncuhareketi()
        if tahtadolu():
            print("Oyun berabere bitti.")
            exit()

        print("--------------------")
        pc_hareketi = pchareket()
        üctas('O', pc_hareketi)
        if kazanan(oyuntahtasi,'O'):
            ekrangöster()
            print("Bilgisayar kazandı.")
            exit()

        ekrangöster()
        if tahtadolu():
            print("Oyun berabere bitti.")
            exit()
            print("--------------------")

oyun()