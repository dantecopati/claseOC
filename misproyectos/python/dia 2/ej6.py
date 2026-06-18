ag={
    "barrigordo":91156747467,
    "copagoat":91167676767,
    "ayutono":91156767667
}
usur=input("ingrese el nombre de usuario (barrigordo; copagoat; ayutono) :")
if usur=="barrigordo":
 print(ag.get('barrigordo'))
elif usur=="copagoat":
 print(ag.get('copagoat'))
else:
 print(ag.get('ayutono'))