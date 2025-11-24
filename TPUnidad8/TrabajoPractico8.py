#Archivos - Práctica
#Objetivo:
#Comprender y aplicar el uso de archivos de texto en Python, desarrollando un
#pequeño programa que lea, procese y almacene información sobre productos de
#manera persistente. Se busca que el estudiante manipule datos a través de
#estructuras como listas y diccionarios, integrando lectura, escritura y buenas prácticas
#con archivos.
#Resultados de aprendizaje:
#Lectura y escritura de archivos:
#El estudiante desarrollará la habilidad de leer y escribir información en archivos de
#texto mediante ejemplos prácticos, reconociendo los modos 'r', 'w' y 'a'.
#Manejo de estructuras de datos: Será capaz de convertir líneas de texto en listas y
#diccionarios, y manipular esta información en memoria de forma eficiente.
#Persistencia y reutilización de datos: Entenderá el concepto de persistencia de
#datos y será capaz de actualizar archivos sin borrar la información previa, reutilizando
#y modificando registros.
#Buenas prácticas al trabajar con archivos: Aplicará el uso de with open() para el
#manejo correcto de archivos y validará situaciones comunes como evitar sobrescritura
#accidental o errores de apertura.
#Actividades:
#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,250.0,50\n")
    archivo.write("Mochila,1500.0,20\n")    

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

#
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    #
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad) separado por comas: ")
# Agregar al archivo
with open("productos.txt", "a") as archivo:
    archivo.write(nuevo_producto + "\n")


#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

# Crear lista de productos
productos = []
#
with open("productos.txt", "r") as archivo: 
    lineas = archivo.readlines()
    # Procesa cada línea y agregar a la lista como diccionario
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
# Mostrar la lista de productos como diccionarios
print("Lista de productos como diccionarios:")  
for producto in productos:
    print(producto)


#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

#Pide el nombre del producto a buscar
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
# Buscar en la lista de productos
for producto in productos:
    # Compara ignorando mayúsculas/minúsculas
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")    


#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

# Sobrescribe el archivo con los productos actualizados
with open("productos.txt", "w") as archivo:
    # Sobrescribir con los productos actualizados
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)
