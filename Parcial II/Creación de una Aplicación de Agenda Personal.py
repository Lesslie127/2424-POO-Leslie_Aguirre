import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Agenda Personal")

        # Frame principal
        marco_principal = tk.Frame(self.ventana)
        marco_principal.pack(padx=15, pady=15)

        # Etiquetas y campos de entrada
        self.etiqueta_fecha = tk.Label(marco_principal, text="Selecciona la Fecha:")
        self.etiqueta_fecha.grid(row=0, column=0, padx=10, pady=10)
        self.selector_fecha = DateEntry(marco_principal, date_pattern='dd-mm-yyyy')
        self.selector_fecha.grid(row=0, column=1, padx=10, pady=10)

        self.etiqueta_hora = tk.Label(marco_principal, text="Hora (Formato 24h):")
        self.etiqueta_hora.grid(row=1, column=0, padx=10, pady=10)
        self.campo_hora = tk.Entry(marco_principal)
        self.campo_hora.grid(row=1, column=1, padx=10, pady=10)

        self.etiqueta_descripcion = tk.Label(marco_principal, text="Descripción del Evento:")
        self.etiqueta_descripcion.grid(row=2, column=0, padx=10, pady=10)
        self.campo_descripcion = tk.Entry(marco_principal)
        self.campo_descripcion.grid(row=2, column=1, padx=10, pady=10)

        # Botones de acción
        self.boton_añadir = tk.Button(marco_principal, text="Añadir Evento", command=self.añadir_evento)
        self.boton_añadir.grid(row=3, column=0, padx=10, pady=10)
        self.boton_eliminar = tk.Button(marco_principal, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.grid(row=3, column=1, padx=10, pady=10)
        self.boton_cerrar = tk.Button(marco_principal, text="Cerrar", command=self.ventana.quit)
        self.boton_cerrar.grid(row=3, column=2, padx=10, pady=10)

        # TreeView para mostrar los eventos
        self.vista_eventos = ttk.Treeview(self.ventana, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.vista_eventos.heading("Fecha", text="Fecha")
        self.vista_eventos.heading("Hora", text="Hora")
        self.vista_eventos.heading("Descripción", text="Descripción")
        self.vista_eventos.pack(padx=15, pady=15, fill="both", expand=True)

    def añadir_evento(self):
        fecha = self.selector_fecha.get()
        hora = self.campo_hora.get()
        descripcion = self.campo_descripcion.get()

        if fecha and hora and descripcion:
            self.vista_eventos.insert('', 'end', values=(fecha, hora, descripcion))
            self.campo_hora.delete(0, 'end')
            self.campo_descripcion.delete(0, 'end')
        else:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")

    def eliminar_evento(self):
        elemento_seleccionado = self.vista_eventos.selection()
        if elemento_seleccionado:
            confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar el evento?")
            if confirmar:
                self.vista_eventos.delete(elemento_seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

# Inicializar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgendaPersonal(ventana)
    ventana.mainloop()
