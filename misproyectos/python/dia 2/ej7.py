print("Ingrese numeros hasta encontrar el correcto")
print("Estos se van sumando sucesivamente")
sumtol=0
num=1
while num!=0:
    num=int(input("Ingrese un numero "))
    sumtol=sumtol+num
    if num==0:
        print(f"Ha encontrado el numero; este era el cero. Suma total= {sumtol}")