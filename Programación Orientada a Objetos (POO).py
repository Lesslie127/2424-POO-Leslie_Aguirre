## Programa que calcula el promedio de las temperaturas de la semana
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Inicializa la lista de temperaturas

    # Método para ingresar la temperatura de un día específico
    def ingresar_temperatura(self, dia, temperatura):
        self.temperaturas.append((dia, temperatura))

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio_semanal(self):
        total_temp = sum(temp for dia, temp in self.temperaturas)
        return total_temp / len(self.temperaturas)

# Registro de temperaturas diarias
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
clima = ClimaDiario()
print("Registro de temperaturas diarias")
for dia in dias_semana:
    # Se solicita la temperatura para cada día de la semana
    temp = float(input(f"Ingrese la temperatura del día {dia}: "))
    clima.ingresar_temperatura(dia, temp)

promedio = clima.calcular_promedio_semanal()  # Calcula el promedio semanal
print(f"La temperatura promedio semanal es: {promedio:.2f}°C")