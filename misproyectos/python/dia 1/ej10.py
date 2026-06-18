while True:
    try:
        print("Ingrese dos numeros que quiera dividir (Número 1/Número2)")
        n1=float(input("Número 1: "))
        n2=float(input("Número 2: "))
        if n2 ==0:
            print("Error: no se puede dividir por 0")
        else:
            div=n1/n2
            print("Resultado de la division")
            print(f"{div}")
        break
    except ValueError :
        print("error, escribir  con numeros ")