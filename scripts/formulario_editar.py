import tkinter as tk
from tkinter import ttk, messagebox
from scripts.consultas_datos import ConsultasDatos
from scripts.modern_styles import ModernStyles  # Asegúrate de que la clase ModernStyles esté en un archivo 'estilos.py'

class FormularioEditar:
    def __init__(self, master):
        self.master = master
        self.master.title("Editar Datos")
        self.master.geometry("400x200")  # Ventana inicial para introducir ID
        
        # Aplicar estilos
        ModernStyles.apply_styles(self.master)
        
        # Inicializar la consulta
        self.consultas = ConsultasDatos()
        
        # Frame principal para el ID
        self.frame_id = ttk.Frame(self.master, padding="20", style="Modern.TFrame")
        self.frame_id.pack(fill=tk.BOTH, expand=True)
        
        # Campo para introducir el ID
        self.label_id = ttk.Label(self.frame_id, text="Introduce el ID de la encuesta a editar:", style="Modern.TLabel")
        self.label_id.pack(pady=10)
        
        self.entry_id = ttk.Entry(self.frame_id, style="Modern.TEntry")
        self.entry_id.pack(pady=10)
        
        # Botón para buscar
        self.boton_buscar = ttk.Button(self.frame_id, text="Buscar", command=self.buscar_datos, style="Modern.TButton")
        self.boton_buscar.pack(pady=10)

    def buscar_datos(self):
        """Busca los datos del ID introducido y abre el formulario de edición si existe."""
        try:
            id_encuesta = int(self.entry_id.get())
            datos = self.consultas.obtener_datos_por_id(id_encuesta)
            
            if datos is not None:
                # Cerrar la ventana de búsqueda
                self.master.destroy()
                # Abrir el formulario de edición
                ventana_edicion = tk.Toplevel()
                FormularioEdicionCompleta(ventana_edicion, datos)
            else:
                messagebox.showerror("Error", "No se encontró una encuesta con ese ID.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un ID válido.")

class FormularioEdicionCompleta:
    def __init__(self, master, datos):
        self.master = master
        self.master.title("Editar Encuesta")
        self.master.geometry("700x700")
        
        # Aplicar estilos
        ModernStyles.apply_styles(self.master)
        
        # Guardar los datos originales
        self.datos = datos
        self.consultas = ConsultasDatos()
        
        # Crear widgets
        self.crear_widgets()
        # Cargar los datos en los campos
        self.cargar_datos()

    def crear_widgets(self):
        """Crea todos los widgets del formulario."""
        frame = ttk.Frame(self.master, padding="20", style="Modern.TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        # Campos personales
        self.label_id = ttk.Label(frame, text="ID:", style="Modern.TLabel")
        self.entry_id = ttk.Entry(frame, state='readonly', style="Modern.TEntry")  # ID no editable
        
        self.label_edad = ttk.Label(frame, text="Edad:", style="Modern.TLabel")
        self.entry_edad = ttk.Entry(frame, style="Modern.TEntry")
        
        self.label_sexo = ttk.Label(frame, text="Sexo:", style="Modern.TLabel")
        self.combobox_sexo = ttk.Combobox(frame, values=["Hombre", "Mujer"], style="Modern.TCombobox")

        # Campos de consumo
        self.label_bebidas_semana = ttk.Label(frame, text="Bebidas a la semana:", style="Modern.TLabel")
        self.entry_bebidas_semana = ttk.Entry(frame, style="Modern.TEntry")
        
        self.label_cervezas_semana = ttk.Label(frame, text="Cervezas a la semana:", style="Modern.TLabel")
        self.entry_cervezas_semana = ttk.Entry(frame, style="Modern.TEntry")
        
        self.label_bebidas_fin_semana = ttk.Label(frame, text="Bebidas fin de semana:", style="Modern.TLabel")
        self.entry_bebidas_fin_semana = ttk.Entry(frame, style="Modern.TEntry")
        
        self.label_bebidas_destiladas_semana = ttk.Label(frame, text="Bebidas destiladas a la semana:", style="Modern.TLabel")
        self.entry_bebidas_destiladas_semana = ttk.Entry(frame, style="Modern.TEntry")
        
        self.label_vinos_semana = ttk.Label(frame, text="Vinos a la semana:", style="Modern.TLabel")
        self.entry_vinos_semana = ttk.Entry(frame, style="Modern.TEntry")

        # Campos de salud
        self.label_perdidas_control = ttk.Label(frame, text="¿Ha tenido pérdidas de control?:", style="Modern.TLabel")
        self.combobox_perdidas_control = ttk.Combobox(frame, values=["Sí", "No"], style="Modern.TCombobox")
        
        self.label_diversion_dependencia_alcohol = ttk.Label(frame, text="¿Diversión o dependencia del alcohol?:", style="Modern.TLabel")
        self.combobox_diversion_dependencia_alcohol = ttk.Combobox(frame, values=["Sí", "No"], style="Modern.TCombobox")
        
        self.label_problemas_digestivos = ttk.Label(frame, text="¿Problemas digestivos?:", style="Modern.TLabel")
        self.combobox_problemas_digestivos = ttk.Combobox(frame, values=["Sí", "No"], style="Modern.TCombobox")
        
        self.label_tension_alta = ttk.Label(frame, text="¿Tensión alta?:", style="Modern.TLabel")
        self.combobox_tension_alta = ttk.Combobox(frame, values=["Sí", "No"], style="Modern.TCombobox")
        
        self.label_dolor_cabeza = ttk.Label(frame, text="¿Dolor de cabeza frecuente?:", style="Modern.TLabel")
        self.combobox_dolor_cabeza = ttk.Combobox(frame, values=["Sí", "No"], style="Modern.TCombobox")

        # Organizar widgets en la ventana
        widgets = [
            (self.label_id, self.entry_id),
            (self.label_edad, self.entry_edad),
            (self.label_sexo, self.combobox_sexo),
            (self.label_bebidas_semana, self.entry_bebidas_semana),
            (self.label_cervezas_semana, self.entry_cervezas_semana),
            (self.label_bebidas_fin_semana, self.entry_bebidas_fin_semana),
            (self.label_bebidas_destiladas_semana, self.entry_bebidas_destiladas_semana),
            (self.label_vinos_semana, self.entry_vinos_semana),
            (self.label_perdidas_control, self.combobox_perdidas_control),
            (self.label_diversion_dependencia_alcohol, self.combobox_diversion_dependencia_alcohol),
            (self.label_problemas_digestivos, self.combobox_problemas_digestivos),
            (self.label_tension_alta, self.combobox_tension_alta),
            (self.label_dolor_cabeza, self.combobox_dolor_cabeza)
        ]

        for i, (label, widget) in enumerate(widgets):
            label.grid(row=i, column=0, sticky="w", pady=5)
            widget.grid(row=i, column=1, pady=5)

        # Botón guardar
        self.boton_guardar = ttk.Button(frame, text="Guardar cambios", command=self.guardar_cambios, style="Modern.TButton")
        self.boton_guardar.grid(row=len(widgets), column=0, columnspan=2, pady=20)

    def cargar_datos(self):
        """Carga los datos existentes en los campos del formulario."""
        self.entry_id.configure(state='normal')
        self.entry_id.delete(0, tk.END)
        self.entry_id.insert(0, str(self.datos['idEncuesta']))
        self.entry_id.configure(state='readonly')
        
        self.entry_edad.insert(0, str(self.datos['edad']))
        self.combobox_sexo.set(self.datos['Sexo'])
        self.entry_bebidas_semana.insert(0, str(self.datos['BebidasSemana']))
        self.entry_cervezas_semana.insert(0, str(self.datos['CervezasSemana']))
        self.entry_bebidas_fin_semana.insert(0, str(self.datos['BebidasFinSemana']))
        self.entry_bebidas_destiladas_semana.insert(0, str(self.datos['BebidasDestiladasSemana']))
        self.entry_vinos_semana.insert(0, str(self.datos['VinosSemana']))
        
        # Convertir booleanos a "Sí"/"No"
        self.combobox_perdidas_control.set("Sí" if self.datos['PerdidasControl'] else "No")
        self.combobox_diversion_dependencia_alcohol.set("Sí" if self.datos['DiversionDependenciaAlcohol'] else "No")
        self.combobox_problemas_digestivos.set("Sí" if self.datos['ProblemasDigestivos'] else "No")
        self.combobox_tension_alta.set("Sí" if self.datos['TensionAlta'] else "No")
        self.combobox_dolor_cabeza.set("Sí" if self.datos['DolorCabeza'] else "No")

    def guardar_cambios(self):
        """Valida y guarda los cambios en la base de datos."""
        try:
            # Obtener todos los valores
            id_encuesta = self.entry_id.get()
            edad = int(self.entry_edad.get())
            sexo = self.combobox_sexo.get()
            bebidas_semana = int(self.entry_bebidas_semana.get())
            cervezas_semana = int(self.entry_cervezas_semana.get())
            bebidas_fin_semana = int(self.entry_bebidas_fin_semana.get())
            bebidas_destiladas_semana = int(self.entry_bebidas_destiladas_semana.get())
            vinos_semana = int(self.entry_vinos_semana.get())
            
            # Convertir "Sí"/"No" a 1/0
            perdidas_control = 1 if self.combobox_perdidas_control.get() == "Sí" else 0
            diversion_dependencia_alcohol = 1 if self.combobox_diversion_dependencia_alcohol.get() == "Sí" else 0
            problemas_digestivos = 1 if self.combobox_problemas_digestivos.get() == "Sí" else 0
            tension_alta = 1 if self.combobox_tension_alta.get() == "Sí" else 0
            dolor_cabeza = 1 if self.combobox_dolor_cabeza.get() == "Sí" else 0

            # Construir la consulta de actualización
            query = """
            UPDATE ENCUESTA 
            SET edad = %s, Sexo = %s, BebidasSemana = %s, CervezasSemana = %s, 
                BebidasFinSemana = %s, BebidasDestiladasSemana = %s, VinosSemana = %s,
                PerdidasControl = %s, DiversionDependenciaAlcohol = %s, ProblemasDigestivos = %s,
                TensionAlta = %s, DolorCabeza = %s
            WHERE idEncuesta = %s
            """

            perdidas_control = 1 if perdidas_control == 'Sí' else 0
            diversion_dependencia_alcohol = 'S' if diversion_dependencia_alcohol == 'Sí' else 'N'
            problemas_digestivos = 'S' if problemas_digestivos == 'Sí' else 'N'
            tension_alta = 'S' if tension_alta == 'Sí' else 'N'
            dolor_cabeza = 'S' if dolor_cabeza == 'Sí' else 'N'
            
            params = (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                     bebidas_destiladas_semana, vinos_semana, perdidas_control,
                     diversion_dependencia_alcohol, problemas_digestivos, tension_alta,
                     dolor_cabeza, id_encuesta)

            # Ejecutar la actualización
            if self.consultas.actualizar_datos(query, params):
                messagebox.showinfo("Éxito", "Los datos se han actualizado correctamente.")
                self.master.destroy()
            else:
                messagebox.showerror("Error", "No se pudieron actualizar los datos.")

        except ValueError as e:
            messagebox.showerror("Error", "Por favor, verifica que todos los campos numéricos contengan números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
