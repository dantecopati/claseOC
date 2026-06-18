while True:
    try:
        hr=5000
        chamba=int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        salario=hr*chamba
        print(f"Tu salario es de {salario} pesos")
        break
    except ValueError :
        print("error, escribir  con numeros ")