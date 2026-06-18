while True:
    try:
        gc=float(input("cuantos grados celcius "))
        fa=(gc*9/5)+32
        print(f"hacen {fa} grados fahrenheit")
        break
    except ValueError :
        print("error, escribir  con numeros ")
