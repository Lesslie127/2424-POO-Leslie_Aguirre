# Programa que se desarrolla un sistema de gestión de inventarios simple para una tienda
# Definición de la clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor que inicializa los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getter para obtener el valor de cada atributo
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setter para actualizar la cantidad y el precio
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método especial para representar el objeto como una cadena de texto
    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}'

# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        # Constructor que inicializa una lista vacía para almacenar productos
        self.productos = []

    # Método para añadir un producto al inventario
    def añadir_producto(self, producto):
        # Comprobar si ya existe un producto con el mismo ID
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            # Si no existe, se añade el producto a la lista
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' añadido al inventario.")

    # Método para eliminar un producto del inventario por ID
    def eliminar_producto(self, id):
        producto = self.buscar_por_id(id)
        if producto:
            # Si se encuentra el producto, se elimina de la lista
            self.productos.remove(producto)
            print(f"Producto con ID {id} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    # Método para actualizar la cantidad o el precio de un producto por ID
    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_por_id(id)
        if producto:
            # Actualiza la cantidad si se proporciona un valor nuevo
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            # Actualiza el precio si se proporciona un valor nuevo
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    # Método para buscar un producto por ID
    def buscar_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    # Método para buscar productos por nombre
    def buscar_por_nombre(self, nombre):
        # Se utiliza una lista por comprensión para filtrar productos por nombre
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    # Método para mostrar todos los productos en el inventario
    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

# Función para mostrar el menú de opciones en la consola
def mostrar_menu():
    print("\nGestión de Inventarios")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")

# Función principal que gestiona el flujo del programa
def main():
    # Se crea una instancia de la clase Inventario
    inventario = Inventario()
    while True:
        # Mostrar el menú y capturar la opción seleccionada por el usuario
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Capturar los datos del nuevo producto
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            # Crear un nuevo objeto Producto y añadirlo al inventario
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            # Capturar el ID del producto a eliminar
            id = input("ID del producto a eliminar: ")
            # Llamar al método para eliminar el producto del inventario
            inventario.eliminar_producto(id)

        elif opcion == "3":
            # Capturar el ID del producto a actualizar
            id = input("ID del producto a actualizar: ")
            # Capturar los nuevos valores de cantidad y precio, si se proporcionan
            cantidad = input("Nueva cantidad (presiona Enter para omitir): ")
            precio = input("Nuevo precio (presiona Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            # Llamar al método para actualizar el producto
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            # Capturar el nombre del producto a buscar
            nombre = input("Nombre del producto a buscar: ")
            # Buscar productos que coincidan con el nombre
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Mostrar todos los productos en el inventario
            inventario.mostrar_todos()

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema...")
            break

        else:
            # Manejar la selección de una opción no válida
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
