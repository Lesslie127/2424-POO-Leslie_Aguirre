import os

def ejecutar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Ejecutando {ruta_script} ---\n")
            exec(codigo, globals())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra este script
    ruta_base = os.path.dirname(__file__)

    # Define las rutas de los scripts
    opciones = {
        '1': 'EjemplosMundoReal_POO/Ejemplo01 Sistema de Gestión de Empleados.py',
        '2': 'EjemplosMundoReal_POO/Ejemplo02 Sistema de Gestión de Pedidos en una Cafetería.py',
        '3': 'EjemplosMundoReal_POO/Ejemplo03 Sistema de Gestión de Cursos en una Universidad.py',
        '4': 'Semana 02/Ejemplo de Tecnicas de Programacion.py',
        '5': 'Semana 02/Constructores y Destructores.py',
        '6': 'Semana 02/Dashboard.py',
        '7': 'Semana 02/Ejemplo gestionar información sobre diferentes tipos de ropa.py',
        '8': 'Semana 02/Ejemplo Usando Tipos de datos, Identificadores.py',
        '9': 'Semana 02/Programación Orientada a Objetos (POO).py',
        '10': 'Semana 02/Programación Tradicional.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ejecutar su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            ejecutar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
