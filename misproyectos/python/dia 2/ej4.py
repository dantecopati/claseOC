print("decime una frase")
frase=input()
cont=0
for letras in frase:
    if letras in "aAeEiIoOuU":
     cont=cont+1
print(cont)
    