ag={
    "banana":50,
    "manzana":100,
    "naranja":80
}
f=str(input("elige una fruta que quieras comprar: "))
k=float(input("decime cuantos kilos queres: "))
if f=="banana":
  sfb=k*(ag.get('banana'))
  print(f"El valor de su compra es de: {sfb}")
elif f=="naranja":
  sfn=k*(ag.get('naranja'))
  print(f"El valor de su compra es de: {sfn}")
else:
  sfm=k*(ag.get('manzana'))
  print(f"El valor de su compra es de: {sfm}")