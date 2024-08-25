# Definición de la clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}'

# Definición de la clase Inventario
class Inventario:
    def __init__(self, archivo):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo archivo al guardar.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
        except PermissionError:
            print(f"No se tiene permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print(f"Producto '{producto.get_nombre()}' añadido al inventario.")

    def eliminar_producto(self, id):
        producto = self.buscar_por_id(id)
        if producto:
            self.productos.remove(producto)
            self.guardar_en_archivo()
            print(f"Producto con ID {id} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_en_archivo()
            print(f"Producto con ID {id} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

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
    inventario = Inventario('inventario.txt')
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = input("Precio del producto: ").replace(',', '.')
            precio = float(precio)
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (presiona Enter para omitir): ")
            precio = input("Nuevo precio (presiona Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio.replace(',', '.')) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
