def crear_mail(name,surname):
    print("Creador de E-mail")
    print("Su E-mail creado es: ")
    print(f"{name}.{surname}@movistar.com")
name=input("Ingrese su nombre(minúscula): ")
surname=input("Ingrese su apellido(minúscula): ")
crear_mail(name,surname)