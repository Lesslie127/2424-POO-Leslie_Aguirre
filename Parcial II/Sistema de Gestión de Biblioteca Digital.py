# Definición de la clase Libro
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        self.informacion = (titulo, autor)  # Tupla con título y autor (inmutables)
        self.categoria = categoria

    def get_isbn(self):
        return self.isbn

    def get_titulo(self):
        return self.informacion[0]

    def get_autor(self):
        return self.informacion[1]

    def get_categoria(self):
        return self.categoria

    def __str__(self):
        return f'ISBN: {self.isbn}, Título: {self.get_titulo()}, Autor: {self.get_autor()}, Categoría: {self.categoria}'


# Definición de la clase Usuario
class Usuario:
    def __init__(self, user_id, nombre):
        self.user_id = user_id
        self.nombre = nombre
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def get_user_id(self):
        return self.user_id

    def get_nombre(self):
        return self.nombre

    def get_libros_prestados(self):
        return self.libros_prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.get_isbn() == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f'ID: {self.user_id}, Nombre: {self.nombre}, Libros Prestados: {[libro.get_titulo() for libro in self.libros_prestados]}'


# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self, archivo):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    isbn, titulo, autor, categoria = linea.strip().split(',')
                    libro = Libro(isbn, titulo, autor, categoria)
                    self.libros[isbn] = libro
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo archivo al guardar.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                for libro in self.libros.values():
                    f.write(f"{libro.get_isbn()},{libro.get_titulo()},{libro.get_autor()},{libro.get_categoria()}\n")
        except PermissionError:
            print(f"No se tiene permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def añadir_libro(self, libro):
        if libro.get_isbn() in self.libros:
            print("Error: Ya existe un libro con ese ISBN.")
        else:
            self.libros[libro.get_isbn()] = libro
            self.guardar_en_archivo()
            print(f"Libro '{libro.get_titulo()}' añadido a la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_en_archivo()
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("Error: Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.get_user_id() in self.usuarios:
            print(f"Error: Ya existe un usuario con ID {usuario.get_user_id()}.")
        else:
            self.usuarios.add(usuario.get_user_id())
            print(f"Usuario '{usuario.get_nombre()}' registrado con éxito.")

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            self.guardar_en_archivo()
            print(f"Libro '{libro.get_titulo()}' prestado a {usuario.get_nombre()}.")
        else:
            print(f"Error: Libro con ISBN {isbn} no disponible o ya prestado.")

    def devolver_libro(self, usuario, isbn):
        libro = usuario.devolver_libro(isbn)
        if libro:
            self.libros[isbn] = libro
            self.guardar_en_archivo()
            print(f"Libro '{libro.get_titulo()}' devuelto por {usuario.get_nombre()}.")
        else:
            print(f"Error: El usuario no tiene prestado el libro con ISBN {isbn}.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        if criterio == "titulo":
            resultados = [libro for libro in self.libros.values() if valor.lower() in libro.get_titulo().lower()]
        elif criterio == "autor":
            resultados = [libro for libro in self.libros.values() if valor.lower() in libro.get_autor().lower()]
        elif criterio == "categoria":
            resultados = [libro for libro in self.libros.values() if valor.lower() in libro.get_categoria().lower()]

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio}: {valor}.")

    def listar_libros_prestados(self, usuario):
        if usuario.get_libros_prestados():
            print(f"Libros prestados a {usuario.get_nombre()}:")
            for libro in usuario.get_libros_prestados():
                print(libro)
        else:
            print(f"{usuario.get_nombre()} no tiene libros prestados actualmente.")

    def mostrar_todos(self):
        if not self.libros:
            print("No hay libros disponibles en la biblioteca.")
        else:
            for libro in self.libros.values():
                print(libro)


# Función para mostrar el menú de opciones en la consola
def mostrar_menu():
    print("\nGestión de Biblioteca Digital")
    print("1. Añadir Libro")
    print("2. Eliminar Libro")
    print("3. Registrar Usuario")
    print("4. Prestar Libro")
    print("5. Devolver Libro")
    print("6. Buscar Libro")
    print("7. Listar Libros Prestados")
    print("8. Mostrar Todos los Libros")
    print("9. Salir")


# Función principal que gestiona el flujo del programa
def main():
    biblioteca = Biblioteca('biblioteca.txt')

    usuarios = {}  # Diccionario para almacenar los usuarios por ID

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            isbn = input("ISBN del libro: ")
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            user_id = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(user_id, nombre)
            usuarios[user_id] = usuario
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            user_id = input("ID del usuario: ")
            if user_id in usuarios:
                isbn = input("ISBN del libro a prestar: ")
                biblioteca.prestar_libro(usuarios[user_id], isbn)
            else:
                print("Error: Usuario no encontrado.")

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            if user_id in usuarios:
                isbn = input("ISBN del libro a devolver: ")
                biblioteca.devolver_libro(usuarios[user_id], isbn)
            else:
                print("Error: Usuario no encontrado.")

        elif opcion == "6":
            criterio = input("Buscar por (titulo, autor, categoria): ").lower()
            valor = input(f"Introduce el valor de {criterio}: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == "7":
            user_id = input("ID del usuario: ")
            if user_id in usuarios:
                biblioteca.listar_libros_prestados(usuarios[user_id])
            else:
                print("Error: Usuario no encontrado.")

        elif opcion == "8":
            biblioteca.mostrar_todos()

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 9.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
