while True:
    try:
        cntd=float(input("cuantos dias queres pasar a segundos "))
        res=cntd*24*60*60
        print(f"cantidad de segundos en dias {res}")
        break
    except ValueError :
        print("error, escribir  con numeros ")