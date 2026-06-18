while True:
    try:
        prec=int(input("ingresa el precio de tu producto para un descueto"))
        desc=int(input("ingresa el descuento q desea aplicar"))
        predesc=prec-(prec/100*desc)
        print(f"el precio final desu producto es de {predesc}")
        break
    except ValueError :
        print("error, escribir  con numeros ")