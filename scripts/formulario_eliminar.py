import tkinter as tk
from tkinter import ttk, messagebox
from scripts.consultas_datos import ConsultasDatos

class FormularioEliminar:
    def __init__(self, master, tabla_datos=None):
        self.master = master
        self.master.title("Eliminar Encuesta")
        self.master.geometry("500x300")
        self.master.config(bg="#ffffff")  # Fondo blanco (modo claro)

        # Estilo de botones
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10, relief="flat", background="#f0f0f0", foreground="black")
        style.map("TButton", background=[('active', '#dcdcdc')])

        # Instancia de ConsultasDatos
        self.consultas = ConsultasDatos()

        # Etiqueta y campo de entrada para el ID
        self.label_id = ttk.Label(master, text="ID de la encuesta a eliminar:", background="#ffffff", foreground="black")
        self.label_id.pack(pady=5)
        
        self.entry_id = ttk.Entry(master)
        self.entry_id.pack(pady=5)

        # Botón para eliminar
        self.boton_eliminar = ttk.Button(master, text="Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.pack(pady=10)

        # Label para mostrar mensajes en la interfaz (opcional)
        self.label_mensaje = ttk.Label(master, text="", background="#ffffff", foreground="black")
        self.label_mensaje.pack(pady=5)

    def eliminar_datos(self):
        id_encuesta = self.entry_id.get()

        if not id_encuesta.isdigit():
            messagebox.showerror("Error", "El ID de encuesta debe ser un número.")
            return

        if not self.consultas.verificar_id_existente(id_encuesta):
            messagebox.showwarning("Advertencia", "El ID de encuesta no existe.")
            return

        if self.consultas.eliminar_datos(id_encuesta):
            messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
            self.entry_id.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showerror("Error", "No se pudo eliminar la encuesta.")

