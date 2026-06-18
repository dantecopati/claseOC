print("inserte sus 5 notas")
notas=[]
hello=0
for i in range(5):
    nots=int(input())
    notas.append(nots)
    hello=hello+nots

prom=hello/5
print(f"la lista de tus notas es  {notas}  y tu promedio de notas es  {prom}")