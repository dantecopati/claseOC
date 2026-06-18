while True :
    try:
        print ("¿Par o Impar?")
        numero=int(input("Ingrese un número: "))
        nump = numero%2
        if nump == 0:
            print("Su número es par ")
        else:
            print("Su número es impar ")
        break
    except ValueError :
        print("error, debes scribir con numeros , no con letras ")