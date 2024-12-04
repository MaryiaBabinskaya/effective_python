import argparse

wspolczynniki = []
stopni = []
wspolczynniki_pochodne = []
stopni_pochodne = []

def fun(string):
    start = True
    for s in string:
        if start == True and s!='x' and s!='*' and s!='+' and s!='-':
            wspolczynniki.append(int(s))
            start = False
        elif start == False and s!='x' and s!='*' and s!='+' and s!='-':
            stopni.append(int(s))
            start = True
        elif start == True and s=='x':
            wspolczynniki.append(1)
            start = False
        elif start == False and (s=='+' or s=='-'):
            stopni.append(1)
            start = True
    stopni.append(0)

def rozniczkowanie():
    for i in range(len(wspolczynniki)):
        wspolczynniki_pochodne.append(wspolczynniki[i] * stopni[i])
        stopni_pochodne.append(stopni[i] - 1)

def fun_x(x):
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik += wspolczynniki[i] * x**stopni[i]
    return wynik

def rozniczka_x(x):
    wynik = 0
    for i in range(len(wspolczynniki_pochodne)):
        wynik += wspolczynniki_pochodne[i] * x**stopni_pochodne[i]
    return wynik

parser = argparse.ArgumentParser(description="Znalezienie miejsca zerowego uzywajac metode Newtona")
parser.add_argument("function", type=str, help="Funkcja dla ktorej szukamy miejsca zerowe")
parser.add_argument("x0", type=float, help="miejsce zerowe")
parser.add_argument("h", type=float, help="wielkosc krokow w pochodnej")
parser.add_argument("count", type=int, help="ilosc krokow metody")
parser.add_argument("d", type=float, help="dokladnosc")
args = parser.parse_args()

fun(args.function)
rozniczkowanie()

x0 = args.x0
x1 = x0 - 1
f0 = fun_x(x0)
count = args.count
while(count > 0 and abs(f0) > args.d): 
    f1 = rozniczka_x(x0)
    x1 = x0
    x0 = x0 - f0/f1
    f0 = fun_x(x0)
    count -= 1
    print(x0)
print('miejsce zerowe= ',x0)