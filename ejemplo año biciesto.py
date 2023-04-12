"""
LABORATORIO Listas y return
Hora prevista
10-15 minutos
Nivel de dificultad
Fácil
Objetivos
Familiarizar al alumno con:
• proyectar y escribir funciones parametrizadas;
• utilizando la declaración de devolución;
• probar las funciones.
Guión
Su tarea es escribir y probar una función que toma un argumento (un año) y devuelve Verdadero si el año es bisiesto o Falso de lo contrario.
La semilla de la función está en el código adjunto.
Nota: también hemos preparado un breve código de prueba, que puede usar para probar su función.
El código usa dos listas: una con los datos de prueba y la otra con los resultados esperados. El código le dirá si alguno de sus resultados no es válido.

Es decir, se determinan dos grupos de años: los 
no seculares y los seculares. Los primeros han 
de ser múltiplos de 4, mientras que los segundos habrán de
 serlo de 400.n. 2​ De esta manera se eliminan como bisiestos
   a 3 de cada 4 años seculares. De esta forma, los años 1800 y 1900 pese a ser divisibles por 4, no lo son por 400, por lo que fueron años comunes. Por su parte, el año 2000 es divisible tanto por 4 como por 400, por lo tanto sí fue un año bisiesto.

siguiendo las reglas establecidas en el calendario gregoriano:

Si el año es divisible por 4 pero no por 100, o es divisible por 400, entonces es bisiesto.
De lo contrario, no es bisiesto.

def isYearLeap(year):
#
# Su codigo AQUI
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


"""

def isYearLeap(year):
    siBiciesto=False
 

    if (year % 4 ==0) and (year % 100 !=0 or year % 400==0):
        siBiciesto=True
        
    print("year=",year)    
    print("biciesto=",siBiciesto)
    return siBiciesto

""" 
year1=4
year2=5

if isYearLeap(year2):
    print("sip")
else:
    print("nop")
"""

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
