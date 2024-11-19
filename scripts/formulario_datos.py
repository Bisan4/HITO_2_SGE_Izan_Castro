import tkinter as tk
from tkinter import ttk, messagebox
from scripts.consultas_datos import ConsultasDatos

class FormularioDatos:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulario de Datos")
        self.master.geometry("700x700")

        # Inicializar la consulta
        self.consultas = ConsultasDatos()

        # Crear un estilo para los widgets
        self.style = ttk.Style()
        self.style.configure("Error.TEntry", fieldbackground="red")
        self.style.configure("Normal.TEntry", fieldbackground="white")

        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
            frame = ttk.Frame(self.master, padding="20")
            frame.pack(fill=tk.BOTH, expand=True)

            self.crear_campos_personales(frame)
            self.crear_campos_consumo(frame)
            self.crear_campos_salud(frame)

            self.label_instrucciones = ttk.Label(frame, text="*Campos obligatorios", foreground="red")
            self.label_instrucciones.grid(row=15, column=0, columnspan=2, pady=5)

            self.boton_guardar = ttk.Button(frame, text="Guardar", command=self.guardar_datos)
            self.boton_guardar.grid(row=16, column=0, columnspan=2, pady=10)

    def crear_campos_personales(self, frame):
            self.label_id = ttk.Label(frame, text="ID*:")  
            self.entry_id = ttk.Entry(frame)

            self.label_edad = ttk.Label(frame, text="Edad*: ")
            self.entry_edad = ttk.Entry(frame)

            self.label_sexo = ttk.Label(frame, text="Sexo*: ")
            self.combobox_sexo = ttk.Combobox(frame, values=["Hombre", "Mujer"])

            self.label_id.grid(row=0, column=0, sticky="w", pady=5)
            self.entry_id.grid(row=0, column=1, pady=5)

            self.label_edad.grid(row=1, column=0, sticky="w", pady=5)
            self.entry_edad.grid(row=1, column=1, pady=5)

            self.label_sexo.grid(row=2, column=0, sticky="w", pady=5)
            self.combobox_sexo.grid(row=2, column=1, pady=5)
    def crear_campos_consumo(self, frame):
        """Crea los campos relacionados con el consumo de bebidas."""
        self.label_bebidas_semana = ttk.Label(frame, text="Bebidas a la semana*: ")
        self.entry_bebidas_semana = ttk.Entry(frame)

        self.label_cervezas_semana = ttk.Label(frame, text="Cervezas a la semana*: ")
        self.entry_cervezas_semana = ttk.Entry(frame)

        self.label_bebidas_fin_semana = ttk.Label(frame, text="Bebidas fin de semana*: ")
        self.entry_bebidas_fin_semana = ttk.Entry(frame)

        self.label_bebidas_destiladas_semana = ttk.Label(frame, text="Bebidas destiladas a la semana*: ")
        self.entry_bebidas_destiladas_semana = ttk.Entry(frame)

        self.label_vinos_semana = ttk.Label(frame, text="Vinos a la semana*: ")
        self.entry_vinos_semana = ttk.Entry(frame)

        # Organizar los widgets
        self.label_bebidas_semana.grid(row=3, column=0, sticky="w", pady=5)
        self.entry_bebidas_semana.grid(row=3, column=1, pady=5)

        self.label_cervezas_semana.grid(row=4, column=0, sticky="w", pady=5)
        self.entry_cervezas_semana.grid(row=4, column=1, pady=5)

        self.label_bebidas_fin_semana.grid(row=5, column=0, sticky="w", pady=5)
        self.entry_bebidas_fin_semana.grid(row=5, column=1, pady=5)

        self.label_bebidas_destiladas_semana.grid(row=6, column=0, sticky="w", pady=5)
        self.entry_bebidas_destiladas_semana.grid(row=6, column=1, pady=5)

        self.label_vinos_semana.grid(row=7, column=0, sticky="w", pady=5)
        self.entry_vinos_semana.grid(row=7, column=1, pady=5)

    def crear_campos_salud(self, frame):
        """Crea los campos relacionados con la salud."""
        self.label_perdidas_control = ttk.Label(frame, text="¿Ha tenido pérdidas de control?*: ")
        self.combobox_perdidas_control = ttk.Combobox(frame, values=["Sí", "No"])

        self.label_diversion_dependencia_alcohol = ttk.Label(frame, text="¿Diversión o dependencia del alcohol?*: ")
        self.combobox_diversion_dependencia_alcohol = ttk.Combobox(frame, values=["Sí", "No"])

        self.label_problemas_digestivos = ttk.Label(frame, text="¿Problemas digestivos?*: ")
        self.combobox_problemas_digestivos = ttk.Combobox(frame, values=["Sí", "No"])

        self.label_tension_alta = ttk.Label(frame, text="¿Tensión alta?*: ")
        self.combobox_tension_alta = ttk.Combobox(frame, values=["Sí", "No"])

        self.label_dolor_cabeza = ttk.Label(frame, text="¿Dolor de cabeza frecuente?*: ")
        self.combobox_dolor_cabeza = ttk.Combobox(frame, values=["Sí", "No"])

        # Organizar los widgets
        self.label_perdidas_control.grid(row=8, column=0, sticky="w", pady=5)
        self.combobox_perdidas_control.grid(row=8, column=1, pady=5)

        self.label_diversion_dependencia_alcohol.grid(row=9, column=0, sticky="w", pady=5)
        self.combobox_diversion_dependencia_alcohol.grid(row=9, column=1, pady=5)

        self.label_problemas_digestivos.grid(row=10, column=0, sticky="w", pady=5)
        self.combobox_problemas_digestivos.grid(row=10, column=1, pady=5)

        self.label_tension_alta.grid(row=11, column=0, sticky="w", pady=5)
        self.combobox_tension_alta.grid(row=11, column=1, pady=5)

        self.label_dolor_cabeza.grid(row=12, column=0, sticky="w", pady=5)
        self.combobox_dolor_cabeza.grid(row=12, column=1, pady=5)

    def guardar_datos(self):
        """Valida y guarda los datos ingresados en el formulario."""
        # Obtener los datos
        id_encuesta = self.entry_id.get()
        edad = self.entry_edad.get()
        sexo = self.combobox_sexo.get()
        bebidas_semana = self.entry_bebidas_semana.get()
        cervezas_semana = self.entry_cervezas_semana.get()
        bebidas_fin_semana = self.entry_bebidas_fin_semana.get()
        bebidas_destiladas_semana = self.entry_bebidas_destiladas_semana.get()
        vinos_semana = self.entry_vinos_semana.get()
        perdidas_control = self.combobox_perdidas_control.get()
        diversion_dependencia_alcohol = self.combobox_diversion_dependencia_alcohol.get()
        problemas_digestivos = self.combobox_problemas_digestivos.get()
        tension_alta = self.combobox_tension_alta.get()
        dolor_cabeza = self.combobox_dolor_cabeza.get()

        # Validar campos obligatorios
        if not self.validar_campos_obligatorios(id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                                                bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                                                problemas_digestivos, tension_alta, dolor_cabeza):
            return

        # Validaciones adicionales
        if not self.validar_formato_edad(edad):
            return
        if not self.validar_formato_consumo(bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana):
            return

        # Insertar los datos
        self.insertar_datos(id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                            bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                            problemas_digestivos, tension_alta, dolor_cabeza)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Los datos se han guardado correctamente.")
        self.limpiar_formulario()

    def validar_campos_obligatorios(self, id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                                     bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                                     problemas_digestivos, tension_alta, dolor_cabeza):
        """Verifica si los campos obligatorios están completos."""
        campos = [id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                  bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                  problemas_digestivos, tension_alta, dolor_cabeza]

        for campo in campos:
            if not campo:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return False
        return True

    def validar_formato_edad(self, edad):
            try:
                edad = int(edad)
                if edad <= 0:
                    self.entry_edad.config(style="Error.TEntry")
                    raise ValueError("La edad debe ser un número mayor a 0.")
                self.entry_edad.config(style="Normal.TEntry")
                return True
            except ValueError:
                self.entry_edad.config(style="Error.TEntry")
                messagebox.showerror("Error", "La edad debe ser un número entero positivo.")
                return False

    def validar_formato_consumo(self, *args):
        """Valida que los campos de consumo sean números enteros positivos."""
        for campo in args:
            try:
                if int(campo) < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Los valores de consumo deben ser números enteros positivos.")
                return False
        return True

    def insertar_datos(self, id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                       bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                       problemas_digestivos, tension_alta, dolor_cabeza):
        """Inserta los datos en la base de datos."""
        try:
            self.consultas.insertar_datos(id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                                          bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                                          problemas_digestivos, tension_alta, dolor_cabeza)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {str(e)}")

    def limpiar_formulario(self):
        """Limpia todos los campos del formulario."""
        self.entry_id.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.combobox_sexo.set('')
        self.entry_bebidas_semana.delete(0, tk.END)
        self.entry_cervezas_semana.delete(0, tk.END)
        self.entry_bebidas_fin_semana.delete(0, tk.END)
        self.entry_bebidas_destiladas_semana.delete(0, tk.END)
        self.entry_vinos_semana.delete(0, tk.END)
        self.combobox_perdidas_control.set('')
        self.combobox_diversion_dependencia_alcohol.set('')
        self.combobox_problemas_digestivos.set('')
        self.combobox_tension_alta.set('')
        self.combobox_dolor_cabeza.set('')

