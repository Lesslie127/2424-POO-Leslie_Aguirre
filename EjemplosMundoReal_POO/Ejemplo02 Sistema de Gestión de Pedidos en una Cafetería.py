class Pedido:
    def __init__(self, numero_pedido, cliente, lista_productos):
        #Inicializa un nuevo objetto Pedido con un numero de pedido, cliente y lista
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.lista_productos = lista_productos
        self.total = self.calcular_total()

    def calcular_total(self):
#Calcula el total del pedido sumando los productos
        return sum(producto['precio'] for producto in self.lista_productos)

    def mostrar_pedido(self):
        #Se muestra los detalles del pedido
        print(f'Pedido #{self.numero_pedido} para {self.cliente}:')
        for producto in self.lista_productos:
            print(f"{producto['nombre']}: ${producto['precio']}")
        print(f"Total: {self.total}")
# Ejemplo de creación y uso de un objeto Pedido
productos=[
    {'nombre':'*Americano coffe', 'precio':5},
    {'nombre':'*heesecake>', 'precio':8},
    {'nombre':'*Rice puff', 'precio':6}
]
pedido1=Pedido(1,'Eric Sohn',productos)
pedido1.mostrar_pedido() #Muestra los detalles del pedido