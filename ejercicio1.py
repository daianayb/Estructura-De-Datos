print("Ingrese sus datos")

nombre=input("ingrese su nombre:")
edad=input("Ingrese su edad:")
fecha_Nac=input("Ingrese su fecha de nacimiento:")
montoMatricula=float(input("Ingrese monto de la matricula:"))

tituloSec=True

montoCuota=montoMatricula+1000.00

arancelPython=12000.0
arancelPythonDesc=arancelPython-(arancelPython*0.15)

print("==========================================================")
print("========= Universidad de Python - Inscripciones ========")
print("=========================================================")

print("DATOS DE INGRESO:")
print("Nombre Completo:",nombre)
print("Fecha de nacimiento y edad :",fecha_Nac,"(",edad,")")
print("Posee titulo?:",tituloSec)
print("Matricula:",montoMatricula)
print("Cuota Mensual:",montoCuota)
print("Arancel mensual materia 'Python I'",arancelPython)
print("Arancel mensual materia 'Python I'",arancelPythonDesc)