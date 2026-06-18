def puede_votar(edad):
    if edad>=18:
        print("Usted puede votar")
    else:
        print("Usted no puede votar")
edad=int(input("Ingrese su edad: "))
puede_votar(edad)