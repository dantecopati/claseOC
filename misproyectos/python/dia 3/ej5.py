def may(n0,n1,n2):
    if n0>n1 and n2:
        return n0
    elif n1>n2:
        return n1
    else:
        return n2
num0=int(input("Ingrese tres números: ")) 
num1=int(input()) 
num2=int(input())
print(f"El mayor número entre los tres es: {may(num0,num1,num2)}")
