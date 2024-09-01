import json

# Clase Producto que representa un ítem en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre            # Nombre del producto
        self.cantidad = cantidad        # Cantidad disponible en el inventario
        self.precio = precio            # Precio del producto

    def __str__(self):
        # Método para representar el producto en forma de cadena
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase Inventario que gestiona una colección de productos
class Inventario:
    def __init__(self):
        # Utilizamos un diccionario para almacenar los productos, donde la clave es el ID del producto
        self.productos = {}

    def cargar_inventario(self, archivo='inventario.json'):
        # Cargar los datos del inventario desde un archivo JSON
        try:
            with open(archivo, 'r') as f:
                self.productos = json.load(f)  # Deserializar los datos en el diccionario de productos
        except FileNotFoundError:
            # Manejar el caso en que el archivo no existe
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            self.productos = {}
        except json.JSONDecodeError:
            # Manejar errores de formato en el archivo JSON
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")
            self.productos = {}

    def guardar_inventario(self, archivo='inventario.json'):
        # Guardar el inventario en un archivo JSON
        try:
            with open(archivo, 'w') as f:
                json.dump(self.productos, f, indent=4)  # Serializar los datos del diccionario en JSON
        except Exception as e:
            # Capturar cualquier otro tipo de error al guardar
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        # Añadir un nuevo producto al inventario
        if producto.id_producto in self.productos:
            print("Producto ya existe.")  # Evitar duplicados
        else:
            # Convertir el objeto Producto a un diccionario y añadirlo al inventario
            self.productos[producto.id_producto] = producto.__dict__

    def eliminar_producto(self, id_producto):
        # Eliminar un producto del inventario por su ID
        if id_producto in self.productos:
            del self.productos[id_producto]  # Eliminar el producto del diccionario
            print(f"Producto {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualizar la cantidad o el precio de un producto
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto]['cantidad'] = cantidad  # Actualizar cantidad
            if precio is not None:
                self.productos[id_producto]['precio'] = precio  # Actualizar precio
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        # Buscar y mostrar productos por nombre
        productos_encontrados = [p for p in self.productos.values() if p['nombre'].lower() == nombre.lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(Producto(producto['id_producto'], producto['nombre'], producto['cantidad'], producto['precio']))
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        # Mostrar todos los productos en el inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for id_producto, info in self.productos.items():
                try:
                    # Crear un objeto Producto temporal para mostrarlo
                    producto = Producto(id_producto, info['nombre'], info['cantidad'], info['precio'])
                    print(producto)
                except KeyError as e:
                    print(f"Error al mostrar el producto {id_producto}: falta el campo {e}.")

def menu():
    # Función que gestiona la interacción del usuario con el sistema de inventario
    inventario = Inventario()
    inventario.cargar_inventario()

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto por Nombre\n5. Mostrar Inventario\n6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Añadir un nuevo producto al inventario
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            inventario.guardar_inventario()
        elif opcion == '2':
            # Eliminar un producto existente del inventario
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            inventario.guardar_inventario()
        elif opcion == '3':
            # Actualizar un producto existente
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
            inventario.guardar_inventario()
        elif opcion == '4':
            # Buscar y mostrar productos por nombre
            nombre = input("Nombre del Producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            # Mostrar todos los productos en el inventario
            inventario.mostrar_inventario()
        elif opcion == '6':
            # Guardar cambios y salir del programa
            inventario.guardar_inventario()
            print("Inventario guardado. Saliendo...")
            break

if __name__ == "__main__":
    menu()
