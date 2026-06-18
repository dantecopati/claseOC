def tiempo(minutos):
    horas=minutos/60
    print(f"{minutos} son {horas} horas")
    return horas
minutos=int(input(f"pon cuantos minutos quieres pasar a horas "))
tiempo(minutos)
