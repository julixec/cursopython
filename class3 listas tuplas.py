#class3

# Definición de una lista #matrices
lista = [1, 2, 3, 4, 5]

# Definición de una tupla
tupla = (1, 2, 3, 4, 5)

# Acceso a un elemento de la lista
print(lista[0]) # salida: 1

# Acceso a un elemento de la tupla
print(tupla[0]) # salida: 1

# Intento de modificar un elemento de la tupla (esto generará un error)
#tupla[0] = 6 # genera un TypeError

# Modificación de un elemento de la lista
lista[0] = 6
print(lista) # salida: [6, 2, 3, 4, 5]

lista=[9,5.3,"Hola",True]
tupla=(19,5.3,"Hola",True)
#for l in lista:
 #   print(l)

print(lista[0])
print(tupla[0])
#TypeError: 'tuple' object does not support item assignment
#tupla[0]=200
lista[0]=500
print(lista[0])

#eliminar datos
del lista[0]
print(lista)





