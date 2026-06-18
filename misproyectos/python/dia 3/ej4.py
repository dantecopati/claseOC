def par(num):
    par=num%2
    if par==1:
        print("Su número es impar")
    else:
        print("Su número es par")
num=int(input("Ingrese el número: "))
par(num)