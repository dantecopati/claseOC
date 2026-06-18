while True:
    try :
        print("Conversor Dólares-Pesos Argentinos")
        dol=1500
        catdol=int(input("Ingrese el monto de dólares que usted desea cambiar : "))
        can=dol*catdol
        print(f"usted tiene {can} pesos")
        break
    except ValueError:
        print("error, escribir  con numeros ")