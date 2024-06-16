# Programa que calcula el promedio de las temperaturas de la semana
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    for dia in dias_semana:
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

print("Registro de temperaturas diarias")
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio_semanal(temperaturas)
print(f"La temperatura promedio semanal es: {promedio:.2f}°C")  # Imprime el promedio semanal
