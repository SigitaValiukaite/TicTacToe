import random

lentele = [" " for j in range(9)]


def spausdinti_lentele():
    print(lentele[0] + "|" + lentele[1] + "|" + lentele[2])
    print("-+-+-")
    print(lentele[3] + "|" + lentele[4] + "|" + lentele[5])
    print("-+-+-")
    print(lentele[6] + "|" + lentele[7] + "|" + lentele[8])


def zaidejo_ejimas():
    while True:
        ejimas = input("Pasirinkite skaičių nuo 1-9: ")
        if ejimas.isdigit() and int(ejimas) in range(1, 10):
            if lentele[int(ejimas) - 1] == " ":
                lentele[int(ejimas) - 1] = "X"
                break
            else:
                print("Deja, langelis užimtas")
        else:
            print("Rinkitės tik nurodytus skaičius (1-9)")


def kompiuterio_ejimas():
    ejimai = [j for j in range(9) if lentele[j] == " "]
    pasirinkimas = random.choice(ejimai)
    lentele[pasirinkimas] = "O"


def lentele_uzpildyta():
    return " " not in lentele


def laimetojas(xo):
    return ((lentele[0] == xo and lentele[1] == xo and lentele[2] == xo) or
            (lentele[3] == xo and lentele[4] == xo and lentele[5] == xo) or
            (lentele[6] == xo and lentele[7] == xo and lentele[8] == xo) or
            (lentele[0] == xo and lentele[3] == xo and lentele[6] == xo) or
            (lentele[1] == xo and lentele[4] == xo and lentele[7] == xo) or
            (lentele[2] == xo and lentele[5] == xo and lentele[8] == xo) or
            (lentele[0] == xo and lentele[4] == xo and lentele[8] == xo) or
            (lentele[2] == xo and lentele[4] == xo and lentele[6] == xo))


spausdinti_lentele()

for j in range(9):
    if j % 2 == 0:
        zaidejo_ejimas()
        if laimetojas("X"):
            print("Tu laimėjai:)!")
            break
    else:
        kompiuterio_ejimas()
        spausdinti_lentele()
        if laimetojas("O"):
            print("Tu pralaimėjai:(")
            break
    if lentele_uzpildyta():
        print("Lygiosios:)!")
        break

spausdinti_lentele()