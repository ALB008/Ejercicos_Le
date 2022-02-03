total1=0
total2=0
p1=0
p2=0
n1=1
n2=1
nh=0
nm=0
n=1
print("Teniendo en cuenta que hombre=1 y mujer=2")
while n<=20:
    gen=int(input("Ingrese el género del estudiante\n"))
    if gen==1:
        nh=int(input("Ingrese la nota del estudiante\n"))
        if 1<=nh<=5:
            n1=n1+1
            n=n+1
            total1=total1+nh
        else:
            print("El dato ingresado no es válido\n")
            continue
    elif gen==2:
        nm=int(input("Ingrese la nota del estudiante\n"))
        if 1<=nm<=5:
            n2=n2+1
            n=n+1
            total2=total2+nm
        else:
            print("El dato ingresado no es válido\n")
            continue
    else:
        print("El dato ingresado no es válido")
        continue
        
p1=total1/n1
p2=total2/n2
if p1>p2:
    g="hombres"
elif p2>p1:
    g="mujeres"
else:
    g="No hay un promedio más elevado"
print("El promedio más elevado lo obtuvieron: \n"+g)
print("Fin del sistema")
