#Práctico 6: Estructuras de datos complejas 
#Objetivo: 
#Dominar el uso de estructuras de datos complejas en Python para 
#almacenar, organizar y manipular datos de manera eficiente, aplicando 
#buenas prácticas y optimizando el rendimiento de las aplicaciones.
#Resultados de aprendizaje: 
#1. Comprensión y aplicación de iterables: listas, tuplas y sets.
#2. Introducción a estructuras de datos complejas: diccionarios.
#Actividades 

#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

#
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir nuevas frutas y precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300   
print("Precios de frutas actualizados:", precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

# Actualizar precios de frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700    
precios_frutas['Melón'] = 2800
print("Precios de frutas actualizados:", precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

#
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
#Ejemplo:
#Teléfonos: {'Juan': 123456, 'Ana': 987654}

#
telefonos = {}
# Cargar 5 contactos
for i in range(5):  
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    telefonos[nombre] = numero  
# Pedir nombre para consultar
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
# Consultar número telefónico
if nombre_consulta in telefonos:
    print(f"El número de {nombre_consulta} es: {telefonos[nombre_consulta]}")
else:
    print("El contacto no existe.")   

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
#Ejemplo:
#Frase: "hola mundo hola"
#Palabras únicas: {'hola', 'mundo'}
#Cantidad de veces: {'hola': 2, 'mundo': 1}

#
frase = input("Ingrese una frase: ")
# Dividir la frase en palabras
palabras = frase.split()      
# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
# Contar la cantidad de veces que aparece cada palabra
contador_palabras = {}
#
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
#Ejemplo:
#alumnos = {
#    'Juan': (7, 8, 9),
#    'Ana': (6, 9, 10),
#    'Luis': (8, 7, 9)
#}


alumnos = {}
# Ingresar nombres y notas de 3 alumnos
for i in range(3):  
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    # Ingresar 3 notas para cada alumno
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107, 108}    
# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial1.intersection(parcial2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
# Estudiantes que aprobaron solo uno de los dos parciales
aprobados_solo_uno = parcial1.symmetric_difference(parcial2)    
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
# Estudiantes que aprobaron al menos un parcial
aprobados_al_menos_uno = parcial1.union(parcial2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
stock_productos = {}
#
while True:
    accion = input("Ingrese 'consultar', 'agregar' o 'salir': ").lower()
    if accion == 'salir':
        break
# Consultar stock de un producto
    elif accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]}")
        else:
            print("El producto no existe en el stock.")
# Agregar unidades al stock o nuevo producto
    elif accion == 'agregar':
        producto = input("Ingrese el nombre del producto a agregar o actualizar: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if producto in stock_productos:
            stock_productos[producto] += cantidad
        else:
            stock_productos[producto] = cantidad
        print(f"Stock actualizado de {producto}: {stock_productos[producto]}")
    else:
        print("Acción no válida. Intente nuevamente.")  
    

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Ejemplo:
#agenda = {
#    ('Lunes', '10:00'): 'Reunión con el equipo',
#    ('Martes', '14:00'): 'Cita con el médico'
#}
agenda = {}
# Ingresar 2 eventos en la agenda
for i in range(2):
    dia = input("Ingrese el día del evento: ")
    hora = input("Ingrese la hora del evento (HH:MM): ")
    evento = input("Ingrese la descripción del evento: ")
    agenda[(dia, hora)] = evento
# Consultar un evento por día y hora
dia_consulta = input("Ingrese el día a consultar: ")
hora_consulta = input("Ingrese la hora a consultar (HH:MM): ")
clave_consulta = (dia_consulta, hora_consulta)
# Mostrar el evento si existe
if clave_consulta in agenda:
    print(f"Evento en {dia_consulta} a las {hora_consulta}: {agenda[clave_consulta]}")
else:
    print("No hay eventos programados en esa fecha y hora.")    

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores
#Ejemplo:
#paises_capitales = {   
#    'Argentina': 'Buenos Aires',
#    'Brasil': 'Brasilia',
#    'Chile': 'Santiago'
#}
# capitales_paises = {
#    'Buenos Aires': 'Argentina',   
#    'Brasilia': 'Brasil',
#    'Santiago': 'Chile'
#}


paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}
capitales_paises = {}
# Invertir claves y valores del diccionario
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais    
print("Diccionario de capitales y países:", capitales_paises)
print("Diccionario de países y capitales:", paises_capitales)
print("-" * 40)

