class Empleado:
    def __init__(self, nombre, puesto, salario):
        #Inicializa un nuevo objeto Empleado con nombre, puesto y salario
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def promocionar(self,nuevo_puesto,incremento_salario):
        #Promociona al empledo a un nuevo puesto y con incremento de salario
        self.puesto = nuevo_puesto
        self.salario += incremento_salario
        print(f'{self.nombre} ha sido promovido a {self.puesto} con un salario de ${self.salario}.')

    def trabajar(self): #Se muestra el trabajo del empleado
            print(f'{self.nombre} esta trabajando como {self.puesto}.')

#Ejemplo de la creacion y el uso de un objeto "Empleado"
empleado1 = Empleado('Lucas Wong', 'Analista', 5000)
empleado1.trabajar() #Actualmente Lucas Wong esta trabajando como Analista
empleado1.promocionar('Gerente', 3000) #Lucas ha sido promovido a Gerente con un salario de $8000
