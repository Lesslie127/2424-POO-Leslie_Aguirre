# Programa para gestionar información sobre diferentes tipos de ropa usando POO en Python.

# Clase base (Ropa)
class Ropa:
    def __init__(self, marca, precio):
        self.marca = marca
        self.__precio = precio  # Encapsulación: atributo privado

    def mostrar_info(self):
        return f"Marca: {self.marca}, Precio: ${self.__precio}"

    def tipo_de_ropa(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases derivadas")


# Clase derivada (Camisa)
class Camisa(Ropa):
    def __init__(self, marca, precio, talla):
        super().__init__(marca, precio)
        self.talla = talla

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Talla: {self.talla}"

    def tipo_de_ropa(self):
        return "Camisa"


# Clase derivada (Pantalon)
class Pantalon(Ropa):
    def __init__(self, marca, precio, estilo):
        super().__init__(marca, precio)
        self.estilo = estilo

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Estilo: {self.estilo}"

    def tipo_de_ropa(self):
        return "Pantalón"


# Función para demostrar polimorfismo
def imprimir_tipos_ropa(ropas):
    for ropa in ropas:
        print(f"{ropa.mostrar_info()} es una {ropa.tipo_de_ropa()}")


# Creación de instancias de las clases
camisa = Camisa("Nike", 89.99, "M")
pantalon = Pantalon("Adidas", 69.99, "Joggers")

# Uso de métodos para demostrar funcionalidad
print(camisa.mostrar_info())
print(pantalon.mostrar_info())

# Polimorfismo: llamada al mismo método en diferentes objetos
ropas = [camisa, pantalon]
imprimir_tipos_ropa(ropas)
