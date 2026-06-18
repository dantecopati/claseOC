saldo=40000
pin_usuario=1234
def verificar_pin(pin_usuario):
    if input_pint==1234:
        return True
    elif input_pint!=1234:

        print("Error; acceso denegado")
        return False
def retirar(monto_dinero):
    global saldo
    if montou<=saldo:
        saldo=saldo-montou
        print("Retiro exitoso ")
        print(f"Saldo restante: {saldo}")
        pass
    else:
        print("Error en el monto")
print("Bienvenido al banco Copati Hughe y de la Grasa Barrigona! ")
try:
        input_pint=int(input("Ingrese el PIN numérico: "))
        while verificar_pin(input_pint):
            if True:    
                print(f"Acceso Concedido. Saldo actual: {saldo}") 
                try:
                    montou=int(input("Ingrese el monto que desea retirar "))
                except ValueError:
                    print("Error; ingrese un monto numérico ")
                retirar(montou)
                break
except ValueError:
    print("Error; PIN numérico. No estan permitidas las letras ")