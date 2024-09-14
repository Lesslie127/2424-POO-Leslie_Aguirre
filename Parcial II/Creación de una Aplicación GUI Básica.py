import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")

# Etiqueta para el campo de texto
label = tk.Label(root, text="Ingresa información:")
label.pack(pady=10)

# Campo de texto
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

# Lista para mostrar los datos
listbox = tk.Listbox(root, width=40, height=8)
listbox.pack(pady=10)

# Función para agregar información
def agregar():
    data = text_entry.get()
    if data:
        listbox.insert(tk.END, data)
        text_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar la lista
def limpiar():
    listbox.delete(0, tk.END)

# Botón para agregar
add_button = tk.Button(root, text="Agregar", command=agregar)
add_button.pack(pady=5)

# Botón para limpiar
clear_button = tk.Button(root, text="Limpiar", command=limpiar)
clear_button.pack(pady=5)

# Iniciar la aplicación
root.mainloop()
