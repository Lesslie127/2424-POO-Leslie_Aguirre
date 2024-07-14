# Programa que simula la apertura y cierre de una conexión de red.
class NetworkConnection:
    def __init__(self, address):

        #Constructor de la clase NetworkConnection.
        #Inicializa la dirección y simula la apertura de una conexión de red.

        self.address = address
        self.connected = False
        self.connect()

    def connect(self):
        #Simula la conexión a una red.
        self.connected = True
        print(f"Conectado a {self.address}")

    def send_data(self, data):
        #Simula el envío de datos a través de la red.
        if self.connected:
            print(f"Enviando datos a {self.address}: {data}")
        else:
            print("No está conectado a la red.")

    def __del__(self):
        #Destructor de la clase NetworkConnection.
        #Cierra la conexión de red si está abierta.

        if self.connected:
            self.connected = False
            print(f"Desconectado de {self.address}")

# Demostración del uso de constructores y destructores

# Creación de un objeto NetworkConnection
network = NetworkConnection("192.168.1.1")
network.send_data("Hola, de nuevo red!")

# Borrado explícito del objeto para demostrar la llamada al destructor
del network

# Se puede observar que el destructor se llama automáticamente al finalizar el programa
