s1=0
s2=0
x=1
salario=0
a=0
n=int(input("Ingrese el número de trabajadores\n"))
while x<=n:
    hora=int(input("\nIngrese las horas trabajadas por el trabajador "+str(x)+"\n"))
    if hora<=40:
        salario=hora*11000
    if hora>40:
        a=hora-40
        s1=40*16000
        s2=a*20000
        salario=s1+s2
    print("El salario mensual del trabajador "+str(x)+" es: "+str(salario))
    print("---------------------------------------------------")
    x=x+1
print("\nFin del sistema")
