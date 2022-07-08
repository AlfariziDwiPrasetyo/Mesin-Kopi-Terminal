import os
import data
from art import logo

def clear():
    os.system('cls')

def menu():
    return data.MENU

def harga(pilihan):
    return menu()[pilihan]['cost']

def resources():
    return data.resources
bahan = resources()

def coinInput():
    ceban = 10000
    gocap = 50000
    coin = 0
    customerInput1 = int(input("Masukan uang 10.000 an = "))
    customerInput2 = int(input("Masukkan uang 50.000 an = "))
    coin = customerInput1 * ceban + customerInput2 * gocap
    return coin

def habis(input):
    habis = False
    for i, j in bahan.items():
        if bahan[i] < menu()[input]['ingredients'][i]:
            habis = True
            return habis

saldo = 0
end = False
print(logo)
while not end:
    choice = input("Mau latte espresso atau cappuccino : \n")

    if choice == 'laporan':
        for key, value in bahan.items():
            print(f"{key} = {bahan[key]}")

    elif choice == 'saldo':
        print(f"Rp{saldo}")

    elif habis(choice):
        print("Maaf stok habis")
        end = True

    else: 
        coin = coinInput()
        kembalian = coin - harga(choice)

        if kembalian < 0 :
            print("Maaf uang kamu kurang")
            end = True

        elif kembalian == 0 :
            print("uangnya pas ya")

        else:
            print(f"ini kembaliannya {kembalian}")
            saldo += harga(choice)

        for key, value in bahan.items():
            bahan[key] -= menu()[choice]['ingredients'][key]
        print(f"ini kopi {choice} ☕  anda\n")
        
        


