import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea a la lista
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Escribe una tarea.")

# Función para marcar una tarea como completada
def marcar_completada(event=None):
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, f"[Completada] {tarea}")
        lista_tareas.itemconfig(tarea_seleccionada, {'fg': 'gray'})  # Cambia el color de la tarea
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "Selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea seleccionada
def eliminar_tarea(event=None):
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "Por favor, selecciona una tarea para eliminar.")

# Función para cerrar la aplicación
def cerrar_aplicacion(event=None):
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas Pendientes")
ventana.geometry("400x400")

# Crear el campo de entrada para añadir nuevas tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

# Botones de interacción
boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Marcar Como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, height=10, width=50, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Vincular atajos de teclado
ventana.bind("<Return>", agregar_tarea)  # Añadir tarea con Enter
ventana.bind("<c>", marcar_completada)  # Marcar tarea como completada con 'C'
ventana.bind("<Delete>", eliminar_tarea)  # Eliminar tarea con Delete
ventana.bind("<d>", eliminar_tarea)  # Eliminar tarea con 'D'
ventana.bind("<Escape>", cerrar_aplicacion)  # Cerrar aplicación con Escape

# Iniciar el bucle de eventos
ventana.mainloop()
