print("Ingrese las notas de los parciales")
nota1=float(input("Ingrese la nota del primer parcial:"))
nota2=float(input("Ingrese la nota del segundo parcial:"))

promedio=(nota1+nota2)/2.0

print("El promedio de las notas es:",promedio)

if nota2 >= 7:
    print("Aprobo el segundo parcial")
else:
    print("Desaprobo el segundo parcial")

if nota2 > nota1:
    print("Mejoró su desempeño")
elif nota2 == nota1:
    print("Mantuvo su desempeño")
elif nota2 < nota1:
    print("Empeoró su desempeño")

if promedio >= 7:
    print("Promocionó la materia")
elif promedio >= 4:
    print("Debe rendir final")
else:
    print("Debe recursar")




