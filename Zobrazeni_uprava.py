import math
import sys

#Kartograficke zobrazeni

#Lambertovo
#zakl vzorce pro vypocet:
#x = R* v , y = R*sin u
#vzorec pro vypocet rovnobezek:
#y = R*sin u

#R = 6371.11 km


zobrazeni = input("Zadej typ zobrazeni (L nebo A, M, B): ")
R = int(input("Zadej poloměr Země (0 pro standardní polomer 6371.11 km): "))
if R == 0:
    R = 6371.11
elif R < 0:
    sys.exit("polomer Země nemůže být záporné číslo")
m = int(input("Zadej meritko ve formatu 1:(tvoje zadane cislo): "))
if m <= 0:
    sys.exit("meritko musi byt vetsi nez 0")
v = int(input("Zadej interval poledniku ve stupnich, zadej 0 pro základní interval (10°): "))
if v == 0:
    v = 10
elif v < 0:
    sys.exit("interval nemuze byt záporné číslo")
u = int(input("Zadej interval souradnic rovnobezky, 0 pro základní interval (10°): "))
if u == 0:
    u = 10
elif u < 0:
    sys.exit("interval nemuze byt zaporne cislo")
n = int(input("Kolik poledniku chces narysovat od stredu? Zadej 0 pro základní počet (18): "))
if n == 0:
    n = 18
elif n < 0:
    sys.exit("cislo nemůže být záporné")
k = int(input("Kolik rovnobezek chces narysovat od stredu? Zadej 0 pro základní počet (9): "))
if k == 0:
    k = 9
elif k < 0:
    sys.exit("číslo nemůže být záporné")

if zobrazeni == "L":
    for v in range(n):
        x = R*(v*n)
        if x/m>(100):
            print("polednik bude - cm od stredu")
        else:
            print("polednik bude", x/m, "cm od stredu")
    for v in range(n):
        x2 = R*(-v*n)
        if x2/m<-100:
            print("polednik bude - cm od stredu")
        elif x2/m<=0:
            print("polednik bude", x2/m, "cm od stredu")
        else:
            print("polednik bude - cm od stredu")
    for u in range(k):
        y = R * math.sin(u * math.pi / 180 * k)
        if y / m * 100 > 100:
            print("rovnobezka bude - cm od stredu")
        else:
            print("rovnobezka bude", '%.1f' % (y / m * 100), "cm od stredu")
    for u in range(k):
        y2 = R * math.sin(-u * math.pi / 180 * k)
        if y2 / m * 100 < -100:
            print("rovnobezka bude - cm od stredu")
        elif y2 / m * 100 <= 0:
            print("rovnobezka bude", '%.1f' % (y2 / m * 100), "cm od stredu")
        else:
            print("rovnobezka bude - cm od stredu")

# Marinovo zobrazeni
# x=R*v, y=R*u

elif zobrazeni == "A":
    print("Marinovo zobrazeni")
    for v in range(n):
        x = R * (v * n)
        if x / m > (100):
            print("polednik bude - cm od stredu")
        else:
            print("polednik bude", '%.1f' % (x / m), "cm od stredu")
    for v in range(n):
        x2 = R * (-v * n)
        if x2 / m < -100:
            print("polednik bude - cm od stredu")
        elif x2 / m <= 0:
            print("polednik bude", '%.1f' % (x2 / m), "cm od stredu")
        else:
            print("polednik bude 0 cm od stredu")
    for u in range(k):
        y = R * (u * k)
        if y / m > 100:
            print("rovnobezka bude - cm od stredu")
        else:
            print("rovnobezka bude", '%.1f' % (y / m), "cm od stredu")
    for u in range(k):
        y2 = R * (-u * k)
        if y2 / m < -100:
            print("rovnobezka bude - cm od stredu")
        elif y2 / m <= 0:
            print("rovnobezka bude", '%.1f' % (y2 / m), "cm od stredu")
        else:
            print("rovnobezka bude - cm od stredu")

# Braunovo zobrazení
# x = R*v, y = 2*R*tg(u/2)

elif zobrazeni == "B":
    print("Braunovo zobrazeni")
    for v in range(n):
        # provede postupne vypocet tolikrat, kolik bylo zadano poledniku
        x = R * (v * n)
        if x / m > (100):
            print("polednik bude - cm od stredu")
        else:
            print("polednik bude", '%.1f' % (x / m), "cm od stredu")
    for v in range(n):
        x2 = R * (-v * n)
        if x2 / m < -100:
            print("polednik bude - cm od stredu")
        elif x2 / m <= 0:
            print("polednik bude", '%.1f' % (x2 / m), "cm od stredu")
        else:
            print("polednik bude 0 cm od stredu")
    for u in range(k):
        y = 2 * R * math.tan(u * k * math.pi / 180 / 2)
        if y / m > 100:
            print("rovnobezka bude - cm od stredu")
        else:
            print("rovnobezka bude", '%.1f' % (y / m * 100), "cm od stredu")
    for u in range(k):
        y2 = 2 * R * math.tan(-u * k * math.pi / 180 / 2)
        if y2 / m * 100 < -100:
            print("rovnobezka bude - cm od stredu")
        elif y2 / m * 100 <= 0:
            print("rovnobezka bude", '%.1f' % (y2 / m * 100), "cm od stredu")
        else:
            print("rovnobezka bude - cm od stredu")

# Mercatorovo zobrazeni
# x = R*v, y = R*ln(cotg(psi/2)) nebo y = R*0.5*ln((1+sin(u)/(1-sin(u)))

elif zobrazeni == "M":
    print("Mercatorovo zobrazeni")
    for v in range(n):
        # provede postupne vypocet tolikrat, kolik bylo zadano poledniku
        x = R * (v * n)
        print("polednik", v, "bude", '%.1f' % (x / m), "cm od stredu")
    for v in range(n):
        x2 = R * (-v * n)
        print("polednik", v, "bude", '%.1f' % (x2 / m), "cm od stredu")
    for u in range(k):
        y = R * 0.5*math.log(1+math.sin((u*k*math.pi/180)))/(1-math.sin((u*k*math.pi/180)))
        if y / m > 100:
            print("rovnobezka bude - cm od stredu")
        else:
            print("rovnobezka bude", '%.1f' % (y / m), "cm od stredu")
    for u in range(k):
        y2 = R * -0.5*math.log(1+math.sin((u*k*math.pi/180)))/(1-math.sin((u*k*math.pi/180)))
        if y2 / m < -100:
            print("rovnobezka bude - cm od stredu")
        elif y2 / m <= 0:
            print("rovnobezka bude", '%.1f' % (y2 / m), "cm od stredu")
        else:
            print("rovnobezka bude 0 cm od stredu")
else:
    print("Toto zobrazeni nelze vypocitat")
