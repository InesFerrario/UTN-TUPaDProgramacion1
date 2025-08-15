#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print ("Hola Mundo!")
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre2= input("Ingrese su nombre:")
print(f"Hola {nombre2}!")
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”,“Pérez”,"30” y “Argentina", el programa debe imprimir “Soy Marcos Pérez, tengo 30años y vivo en Argentina”
#Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre3= input("Ingrese su nombre:")
apellido3= input("Ingrese su apellido:")
edad3= input("Ingrese su edad:")
residencia3= input("Ingrese su lugar de residencia:")
print(f"soy {nombre3} {apellido3}, tengo {edad3} años y vivo en {residencia3}")
#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio= float(input("Ingrese el radio de un círculo"))
area= 3.14159 * radio ** 2
perimetro= 2 * 3.14159 * radio
print(f"El area del círculo es {area} y el perímentro es {perimetro}")
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos= int(input("Ingrese una cantidad de segundos"))
horas= segundos/3600
print(f"La cantidad {segundos} equivale a {horas} horas.")
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero= int(input("Ingrese un número entero"))
tabla1= 1*numero
tabla2= 2*numero
tabla3= 3*numero
tabla4= 4*numero
tabla5= 5*numero
tabla6= 6*numero
tabla7= 7*numero
tabla8= 8*numero
tabla9=9*numero
tabla10= 10*numero
print(f"Su tabla de multiplicar es {tabla1} - {tabla2} - {tabla3} - {tabla4} - {tabla5} - {tabla6} - {tabla7} - {tabla8} - {tabla9} - {tabla10}")
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero7= int(input("Ingrese un número entero distinto de 0"))
numero77= int (input("Ingrese otro número entero distinto a 0"))
suma = numero7+ numero77
division= numero7/numero77
multiplicacion= numero7*numero77
resta= numero7- numero77
print(f"El resultado de su suma es {suma}, de su división {division}, de su multiplicación {multiplicacion}, de su resta {resta}.")
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
altura= float(input("Ingrese su altura"))
peso= float(input("Ingrese su peso"))
IMC= peso/ (altura**2)
print(f"Su índice de masa corporal es {IMC}.")
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
tempC= float(input("Ingrese una temperatura en grados Celsius"))
tempF= tempC* 9/5 + 32
print(f"Su equivalencia en Fahrenheit es {tempF}.")
#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num10= int(input("Ingrese un número"))
num100= int(input("Ingrese un número"))
num1000= int(input("Ingrese un número"))
promedio= (num10+num100+num1000) / 3
print(f"Su promedio es {promedio}.")




