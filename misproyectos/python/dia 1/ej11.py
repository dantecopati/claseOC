while True:
    try:
        n1=int(input("Ingrese un número "))
        n2=int(input("Ingresa otro número "))
        if n2<n1:
            may=n1
        else :
            may=n2
            print(f"El número mayor es {may}")
        break
    except ValueError :
        print("error, escribir  con numeros ")
