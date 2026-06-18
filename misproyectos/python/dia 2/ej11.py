import random
numram=random.randint(1,100)
num=()
while numram!=num:
    num=int(input("intenta adivinar el numero "))
    if numram>num:
        print("tu numero es mas chico")
    elif numram<num:
        print("tu numero es mas grande")
print(f"felicidades adivinaste el numero, el numero era {numram}")