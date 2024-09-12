print("***************AULAS******************")
dia=int(input("Ingrese el numero del dia: 1 (Lunes) a 6 (Sabado):  "))

if (dia%2 == 0):
    print("Aula: A-300")

if (dia%2 != 0):
    print("Aula: A-315")

print()
print("********* DESCUENTOS Y ESTACIONAMIENTO *********")

turno=input("Ingrese el turno.. (1)Mañana (2)Tarde (3)Noche : ")
cantMaterias=int(input("Ingrese la cantidad de materias: "))
cuota=35000

if(turno == 2 and cantMaterias >3 ):
    desc=cuota * 0.25 
    cuota=cuota - desc
else :
    desc=cuota * 0.5 
    cuota=cuota - desc

print(f"El valor de la cuota es: {cuota}")

estacionamiento=int(input("Ingrese el vehiculo en el que ingresa: 1) Auto 2) Moto 3) Bicicleta  : "))

if(estacionamiento==1 or estacionamiento ==2):
    print("costo de estacionamiento: $300")
elif(estacionamiento==3):
   print("costo de estacionamiento: $50") 
