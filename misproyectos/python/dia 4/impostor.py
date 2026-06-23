import random
import time
ron=(0)
comidas=["pizza", "papas fritas", "hamburguesa", "panchos", "empanadas"]
clubes=["river", "boca", "independiente", "racing", "san lorenzo"]
paises=["bosnia y herzegovina", "rumania", "estados unidos", "japon", "brasil"]
jugadores=[]
print("IMPOSTOR")
cat=input("Ingrese la categoría (comidas, clubes, países)")
par=int(input("Ingrese la cantidad de participantes "))
numran=random.randint(0, (par-1))
numran2=random.randint(0,4)
if cat=="comidas" or "Comidas":
    palabra=comidas[numran2]
elif cat=="clubes" or "Clubes":
    palabra=clubes[numran2]
else:
    palabra=paises[numran2]
for i in range(par):
    ju=input(f"Ingrese el nombre del jugador {i} ")
    jugadores.append(ju)   
    if i!=numran:
        print(jugadores[i])
        print(f"La palabra es {palabra} ")
        time.sleep(3)
        print("\033[F\033[K" , end="")
    elif i==numran:
        print(jugadores[i])
        print("Usted es el impostor ")
        imp=jugadores[i]
        time.sleep(3)
        print("\033[F\033[K" , end="")
print("EMPIEZA EL JUEGO")
while imp:
    ron=ron+1
    print(f"RONDA {ron}")
    vot=input("Elijan un impostor ")
    if vot==imp:
        print("Usted a elegido al impostor, ha ganado")
        break
    else:
        print("Usted a elegido a un inocente")    
        jugadores.remove(vot)



        
    
    
     
