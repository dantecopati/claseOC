while True:
    try:
        sem=str(input("¿que color de semaforo hay ?"))
        if sem=="verde":
            print("avance" )
        elif sem=="rojo":
            print("no avance ")
        else :
            print("espere un momento ")
        break
    except  ValueError:
        print("error, escribir  con letras ")