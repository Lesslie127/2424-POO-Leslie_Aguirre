import tkinter as tk
from tkinter import ttk, messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = task_entry.get()  # Obtener la tarea del campo de entrada
    if task != "":  # Verificar que no esté vacía
        task_tree.insert("", "end", values=(task, "Pendiente"))  # Añadir la tarea con estado "Pendiente"
        task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce una tarea válida.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_item = task_tree.selection()[0]  # Obtener el ítem seleccionado
        task_tree.item(selected_item, values=(task_tree.item(selected_item, 'values')[0], "Completada"))  # Cambiar el estado a "Completada"
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Función para eliminar una tarea seleccionada
def delete_task():
    try:
        selected_item = task_tree.selection()[0]  # Obtener el ítem seleccionado
        task_tree.delete(selected_item)  # Eliminar la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Configuración de la ventana principal
window = tk.Tk()
window.title("Gestor de Tareas")
window.geometry("450x400")

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(window, width=35)
task_entry.pack(pady=10)

# Botón para añadir una nueva tarea
add_button = tk.Button(window, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

# Crear el Treeview para mostrar las tareas con dos columnas: tarea y estado
task_tree = ttk.Treeview(window, columns=("Tarea", "Estado"), show='headings')
task_tree.heading("Tarea", text="Tarea")  # Encabezado para la columna de tareas
task_tree.heading("Estado", text="Estado")  # Encabezado para la columna de estado
task_tree.column("Tarea", width=250)  # Ajustar el ancho de la columna de tareas
task_tree.column("Estado", width=100)  # Ajustar el ancho de la columna de estado
task_tree.pack(pady=10)

# Botón para marcar una tarea como completada
complete_button = tk.Button(window, text="Marcar como Completada", command=mark_completed)
complete_button.pack(pady=5)

# Botón para eliminar una tarea
delete_button = tk.Button(window, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Evento para añadir tareas con la tecla Enter
window.bind('<Return>', add_task)

# Iniciar el bucle principal de la aplicación
window.mainloop()
