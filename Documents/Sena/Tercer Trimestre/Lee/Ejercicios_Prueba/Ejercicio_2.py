p=0
total=0
v1=0
v2=0
v3=0
pg=0
voto="si"
g="Ninguno"

print(">Candidato 1: Jose\n>Candidato 2: Pedro\n>Candidato 3: Andres\n")
while voto=="si":
    n=int(input("Ingrese el número del candidato al que desea votar\n"))
    if n==1:
        v1=v1+1
        total=total+1
    elif n==2:
        v2=v2+1
        total=total+1
    elif n==3:
        v3=v3+1
        total=total+1
    else:
        print("El número ingresado no corresponde al de un candidato")
    voto=input("Si desea ingresar un nuevo voto escriba 'si'\n")
if v1>v2 and v1>v3:
    g="Jose"
    pg=v1
elif v2>v1 and v2>v3:
    g="Pedro"
    pg=v2
elif v3>v2 and v3>v1:
    g="Andres"
    pg=v3
else:
    g="Hay un empate"
p=(pg*100)/total
print("El ganador de la votación es:\n"+g+" con un porcentaje de: "+str(p)+"%")
print("Fin del sistema")
