
while True:
    try:  
        cuenta = float(input("¿Cuál es el total de la cuenta?:"))
        porcentaje = int(input("¿Cuál es el porcentaje que usted desea (10,15,20?):"))
        propina = cuenta/100*porcentaje 
        print(f"La propina que usted desea dejar es de {propina}")
        break
    except ValueError :
        print("Error; ingrese el total en números ")

  
    
