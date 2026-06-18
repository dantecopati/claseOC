while True:
    try:
        print("Promedio de 3 notas ")
        nt1=float(input("Ingrese la primer nota: "))
        nt2=float(input("Ingrese la segunda nota: "))
        nt3=float(input("Ingrese la tercer nota: "))
        prom=(nt1+nt2+nt3)/3
        print(f"El promedio de sus 3 notas es :{prom}")
        break
    except ValueError:
        print("error, escribir  con numeros ")