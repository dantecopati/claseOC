while True:
    try:
        print("area de un recxtangulo")
        bdr=int(input("cual es la base del rectangulo : "))
        adr=int(input("cual  es la altura del rectangulo :"))
        res=adr*bdr
        print(f"el area de rectangulo es : {res}")
        break
    except ValueError :
        print("error, escribir  con numeros ")