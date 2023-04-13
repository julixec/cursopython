"""
LABORATORIO

Hora prevista
15-20 minutos
Nivel de dificultad
Medio
Prerrequisitos
LAB Listas y return
Objetivos
Familiarizar al alumno con:
•	proyectar y escribir funciones parametrizadas;
•	utilizando la declaración de return;
•	utilizando las funciones propias del alumno.
Guión
Su tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días para el par mes / año dado (aunque solo febrero es sensible al valor del año, su función debería ser universal).
La parte inicial de la función está lista. Ahora, modifique a la función para que use la opción de return  None si sus argumentos no tienen sentido.
Por supuesto, puede (y debe) usar la función previamente escrita y probada (LAB Listas y return). Puede ser de mucha ayuda. Lo alentamos a que use una lista con los meses. Puede crearlo dentro de la función: este truco acortará significativamente el código.
Hemos preparado un código de prueba. 
 

def isYearLeap(year):
#
# Codigo from LAB Listas y return

#

def daysInMonth(year, month):
#
# put your new code here
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

            Número	Mes	Duración
1	Enero	31 días
2	Febrero	28 días o 29 en año bisiesto
3	Marzo	31 días
4	Abril	30 días
5	Mayo	31 días
6	Junio	30 días
7	Julio	31 días
8	Agosto	31 días
9	Septiembre	30 días
10	Octubre	31 días
11	Noviembre	30 días
12	Diciembre	31 días

output:
PS C:\webscrapping>  c:; cd 'c:\webscrapping'; & 'C:\Users\julian.galindo\AppData\Local\Programs\Python\Python311\python.exe' 'c:\Users\julian.galindo\.vscode\extensions\ms-python.python-2023.4.1\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '59870' '--' 'c:\Users\julian.galindo\OneDrive - Escuela Politécnica Nacional\Documentos\EPN\capacitación\python essentials 2023 10 abril\tasks\ejemplo calculo num dias mes año.py' 
1900 2 ->year= 1900
biciesto= False
OK
2000 2 ->year= 2000
biciesto= True
si año biciesto
OK
2016 1 ->year= 2016
biciesto= True
OK
1987 11 ->year= 1987
biciesto= False
OK
PS C:\webscrapping>

"""
diasNormales= {1:31,
              2:28,
              3:31,
              4:30,
              5:31,
              6:30,
              7:31,
              8:31,
              9:30,
              10:31,
              11:30,
              12:31
              }

def isYearLeap(year):
    siBiciesto=False
 
    if (year % 4 ==0) and (year % 100 !=0 or year % 400==0):
        siBiciesto=True
        
    print("year=",year)    
    print("biciesto=",siBiciesto)
    return siBiciesto



def daysInMonth(year, month):
    diasMes=0
# si no año biciesto entonces dias normales
# si es año biciesto entonces chequear febrero = 28 dias
# put your new code here

    if isYearLeap(year) and month==2:
        print("si año biciesto")
        diasMes=29
    else:
        diasMes=diasNormales[month]

    return diasMes


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")