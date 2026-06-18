while True:
    try:
        nota=int(input("ingresa tu nota del examen"))
        if nota<6:
            print ("tu examen esta reprobado")
        elif nota>=6:
            print("tu examen esta aprobado")
        break
    except ValueError :
        print("error, escribir  con numeros ")