while True:
    try:
        num=int(input("ingresa un numero :"))
        if num<0:
            print("tu numero negativo")
        elif num>0:
            print("tu numero es positivo")
        else:
            print("tu numero es 0")
            break
    except ValueError :
        print("error, escribir  con numeros ")
