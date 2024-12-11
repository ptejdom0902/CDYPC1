mas300=0
entre100Y300=0
n=int(input("¿Cuántos empleados tiene la empresa?"))
for x in range(n):
    sueldo=int(input("Introduce sueldo:"))
    if (sueldo>300):
        mas300=mas300+1
    else:
        if(sueldo>=100):
            entre100Y300=entre100Y300+1
print("Empleados que ganan más de 300:",mas300)
print("Empleados que ganan entre 100 y 300:",entre100Y300)
