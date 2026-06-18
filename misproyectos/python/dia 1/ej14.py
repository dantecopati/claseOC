while True:
    try:
        cc = "listo"
        ing=input("ingrese la palabra listo ")
        if ing=="listo":
            print("acceso concedido")
        else:
            print("acceso denegado")
            break
    except ValueError :
        print("error, escribir  con numeros ")