def precio(d):
    pcd=p-(p/100*d)
    print(f"Tu precio final es de : {pcd}")
    return pcd
d=int(input("¿De cuánto es tu descuento ? "))
p=int(input("¿Cuánto sale tu producto ? "))
precio(d)