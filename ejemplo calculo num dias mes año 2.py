"""
Hora prevista
20-30 minutos
Nivel de dificultad
Medio
Prerrequisitos
LABORATORIO Listas y return
LABORATORIO Listas y return2

Objetivos
Familiarizar al alumno con:
•	proyectar y escribir funciones parametrizadas;
•	utilizando la declaración de return ;
•	construir un conjunto de funciones de utilidad;
•	utilizando las funciones propias del alumno.
Guión
Su tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve los días correspondiente del año, o devuelve None si alguno de los argumentos es inválido.
Use las funciones previamente escritas y probadas. Agregue algunos casos de prueba al código. 
Esta prueba es solo un comienzo.
def isYearLeap(year):
#
# your code from LAB 1
#

def daysInMonth(year, month):
#
# your code from LAB 2
#

def dayOfYear(year, month, day):
#
# put your new code here
#

print(dayOfYear(2000, 12, 31))


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

julix Como se solicita dias del año, mes y dia no se toman en cuenta
pues se suman todos los dias de cada mes tomando en cuenta el año biciesto
output:
61169' '--' 'c:\Users\julian.galindo\OneDrive - Escuela Politécnica Nacional\Documentos\EPN\capacitación\python essentials 2023 10 abril\tasks\ejemplo calculo num dias mes año 2.py' 
year= 2000
biciesto= True
si año biciesto
366
2nd execution
year= 2023
biciesto= False
No año biciesto
365
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

""" 
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
"""

def dayOfYear(year, month, day):
#
# put your new code here
    diasAño=0
    diasFeb=0
    if(type(year)!=int or type(month)!=int or type(day)!=int):
        print("Todas las variables deben ser un entero ;()")
        return "None" 


    if isYearLeap(year) :
            print("si año biciesto")
            diasFeb=29
            diasAño=diasNormales[1]+diasFeb+diasNormales[3]+\
            diasNormales[4]+diasNormales[5]+diasNormales[6]+\
            diasNormales[7]+diasNormales[8]+diasNormales[9]+\
            diasNormales[10]+diasNormales[11]+diasNormales[12]
    else:
            print("No año biciesto")
            diasAño=diasNormales[1]+diasNormales[2]+diasNormales[3]+\
            diasNormales[4]+diasNormales[5]+diasNormales[6]+\
            diasNormales[7]+diasNormales[8]+diasNormales[9]+\
            diasNormales[10]+diasNormales[11]+diasNormales[12]
 
    return diasAño


print(dayOfYear(2000, 12, 31))
print("2nd execution")
print(dayOfYear(2023, 12, 31))