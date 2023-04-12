"""
Crear un algoritmo en Python (*.py) que solicite al usuario cuatro datos:

Nombre

Apellido

Ubicación

Edad

Crear un párrafo con los datos ingresados por el usuario, debe crear un ejemplo de uso de los datos.
"""
cliente={"nombre":"",
             "apellido":"",
             "ubicacion":"",
             "edad":""
}
print("Datos de cliente")
#pedir el nombre

cliente["nombre"]=input("Ingresa tu nombre:")
#print(cliente)
cliente["apellido"]=input("Ingresa tu apellido:")
#print(cliente)
cliente["ubicacion"]=input("Ingresa tu ubicacion:")
cliente["edad"]=input("Ingresa tu edad:")
#print(cliente)

print("los datos ingresados por el cliente son: nombre:{}, apellido:{}, ubicación:{} y la edad:{}".format(cliente["nombre"],cliente["apellido"],cliente["ubicacion"],cliente["edad"]))
if int(cliente["edad"]) > 40:
    print("Como la edad es mayor a 40 SI aplica al préstamo hipotecario a una tasa de 8.99%")
else:
    print("Como la edad es menor o igual a 40 NO aplica al préstamo hipotecario. Favor espere a ser mayor de edad ;)")


"""
output:
 - Escuela Politécnica Nacional/Documentos/EPN/capacitación/python essentials 2023 10 abril/tasks/ejemplo input python.py"        
Datos de cliente
Ingresa tu nombre:julix
Ingresa tu apellido:galindo
Ingresa tu ubicacion:quito s32
Ingresa tu edad:41
los datos ingresados por el cliente son: nombre:julix, apellido:galindo, ubicación:quito s32 y la edad:41
Como la edad es mayor a 40 SI aplica al préstamo hipotecario a una tasa de 8.99%
PS C:\webscrapping>
"""