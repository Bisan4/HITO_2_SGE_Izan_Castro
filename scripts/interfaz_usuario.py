import tkinter as tk
from tkinter import ttk
from scripts.consultas_datos import ConsultasDatos  # Actualizado con la ruta correcta
from scripts.tabla_datos import TablaDatos  # Cambié la importación para usar 'scripts'
from scripts.formulario_datos import FormularioDatos  # Actualizada la importación
from scripts.formulario_eliminar import FormularioEliminar  # Actualizada la importación
from scripts.formulario_editar import FormularioEditar  # Actualizada la importación
from scripts.grafico_datos import GraficoDatos  # Actualizada la importación
import matplotlib.pyplot as plt
from scripts.modern_styles import ModernStyles  # Actualizada la importación


class InterfazUsuario:
    def __init__(self, master, conexion_base_datos):
        self.master = master
        self.master.title("Interfaz de Salud y Consumo de Alcohol-Clínica del Dr. Fernando")
        self.master.geometry("1300x700")
        ModernStyles.apply_styles(self.master)  # Aplicar los estilos definidos en ModernStyles

        self.conexion_base_datos = conexion_base_datos

        # Menú principal
        self.menu = tk.Menu(master, bg=ModernStyles.BACKGROUND_COLOR, fg=ModernStyles.TEXT_COLOR, tearoff=0)
        master.config(menu=self.menu)
        self.menu_archivo = tk.Menu(self.menu, bg=ModernStyles.SECONDARY_BACKGROUND, fg=ModernStyles.TEXT_COLOR, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menu_archivo.add_command(label="Exportar a Excel", command=self.exportar_datos)
        self.menu_archivo.add_command(label="Salir", command=master.quit)

        # Etiqueta principal
        self.label = ttk.Label(master, text="Consumo de Alcohol y Salud", style="ModernTitle.TLabel")
        self.label.pack(pady=20)

        # Frame para los botones
        self.frame_botones = tk.Frame(master, bg=ModernStyles.BACKGROUND_COLOR)
        self.frame_botones.pack(pady=20, expand=True)  # Expandir para que ocupe el espacio disponible

        # Usamos grid con 2 columnas para los botones centrados
        self.boton_consultar = ttk.Button(self.frame_botones, text="Consultar Datos", style="Modern.TButton", command=self.consultar_datos)
        self.boton_consultar.grid(row=0, column=0, padx=15, pady=10, sticky='ew')

        self.boton_agregar = ttk.Button(self.frame_botones, text="Añadir Datos", style="Modern.TButton", command=self.abrir_formulario_agregar)
        self.boton_agregar.grid(row=0, column=1, padx=15, pady=10, sticky='ew')

        self.boton_editar = ttk.Button(self.frame_botones, text="Editar Datos", style="Modern.TButton", command=self.abrir_formulario_editar)
        self.boton_editar.grid(row=1, column=0, padx=15, pady=10, sticky='ew')

        self.boton_eliminar = ttk.Button(self.frame_botones, text="Eliminar Datos", style="Modern.TButton", command=self.abrir_formulario_eliminar)
        self.boton_eliminar.grid(row=1, column=1, padx=15, pady=10, sticky='ew')

        # Frame para separar el botón "Generar Gráfico"
        self.frame_grafico = tk.Frame(master, bg=ModernStyles.BACKGROUND_COLOR)
        self.frame_grafico.pack(pady=20)

        # Botón "Generar Gráfico" en su propio frame
        self.boton_graficar = ttk.Button(self.frame_grafico, text="Generar Gráfico", style="Modern.TButton", command=self.abrir_ventana_grafico)
        self.boton_graficar.pack(pady=10)

        # Configuración de la tabla de datos
        self.tabla_datos = TablaDatos(master, callback_eliminar=self.eliminar_dato)

        # Filtros de búsqueda
        self.frame_filtros = tk.Frame(master, bg=ModernStyles.BACKGROUND_COLOR)
        self.frame_filtros.pack(pady=20)

        self.filtro_sexo_label = ttk.Label(self.frame_filtros, text="Sexo:", style="Modern.TLabel")
        self.filtro_sexo_label.grid(row=0, column=0, sticky="w", padx=15)

        self.sexo_var = tk.StringVar(value="")
        self.radio_hombre = ttk.Radiobutton(self.frame_filtros, text="Hombre", variable=self.sexo_var, value="Hombre", style="Modern.TRadiobutton")
        self.radio_mujer = ttk.Radiobutton(self.frame_filtros, text="Mujer", variable=self.sexo_var, value="Mujer", style="Modern.TRadiobutton")
        self.radio_ambos = ttk.Radiobutton(self.frame_filtros, text="Ambos Géneros", variable=self.sexo_var, value="Ambos", style="Modern.TRadiobutton")

        self.radio_hombre.grid(row=1, column=0, padx=15, pady=5)
        self.radio_mujer.grid(row=1, column=1, padx=15, pady=5)
        self.radio_ambos.grid(row=1, column=2, padx=15, pady=5)

        self.filtro_edad_label = ttk.Label(self.frame_filtros, text="Edad (Mayor que):", style="Modern.TLabel")
        self.filtro_edad_label.grid(row=2, column=0, sticky="w", padx=15)

        self.filtro_edad = ttk.Entry(self.frame_filtros, style="Modern.TEntry")
        self.filtro_edad.grid(row=2, column=1, padx=15, pady=5)

    def consultar_datos(self):
        consultas = ConsultasDatos()
        sexo = self.sexo_var.get()
        edad = self.filtro_edad.get()
        try:
            edad = int(edad) if edad else None
        except ValueError:
            edad = None
        
        query = "SELECT * FROM ENCUESTA WHERE 1=1"
        params = [] 

        if sexo == "Hombre":
            query += " AND Sexo = %s"
            params.append("Hombre")
        elif sexo == "Mujer":
            query += " AND Sexo = %s"
            params.append("Mujer")
        
        if edad is not None:
            query += " AND edad > %s"
            params.append(edad)

        self.master.after(0, self.cargar_datos, consultas, query, tuple(params))

    def cargar_datos(self, consultas, query, params):
        datos = consultas.obtener_datos(query, params)
        if datos is None or datos.empty:
            print("No se encontraron datos.")
        else:
            self.tabla_datos.actualizar_datos(datos)

    def abrir_ventana_grafico(self):
        ventana_grafico = tk.Toplevel(self.master)
        ventana_grafico.title("Seleccionar Gráfico")
        ventana_grafico.geometry("400x300")  # Ajusta el tamaño según sea necesario
        ventana_grafico.config(bg=ModernStyles.BACKGROUND_COLOR)
        
        # Estilo de Gráfico
        estilo_label = ttk.Label(ventana_grafico, text="Estilo de Gráfico:", style="Modern.TLabel")
        estilo_label.pack(pady=10)
        
        self.estilo_var = tk.StringVar(value='dark_background')
        opciones_estilo = ['dark_background', 'ggplot']
        self.estilo_menu = ttk.Combobox(ventana_grafico, textvariable=self.estilo_var, values=opciones_estilo, state="readonly", style="Modern.TCombobox")
        self.estilo_menu.pack(pady=5)

        # Color
        color_label = ttk.Label(ventana_grafico, text="Color:", style="Modern.TLabel")
        color_label.pack(pady=10)
        
        self.color_var = tk.StringVar(value='blue')
        opciones_colores = ['blue', 'green', 'red', 'orange', 'purple']
        self.color_menu = ttk.Combobox(ventana_grafico, textvariable=self.color_var, values=opciones_colores, state="readonly", style="Modern.TCombobox")
        self.color_menu.pack(pady=5)
        
        # Botón "Generar Gráfico"
        boton_generar = ttk.Button(ventana_grafico, text="Generar Gráfico", style="Modern.TButton", command=self.generar_grafico)
        boton_generar.pack(pady=20)  # Asegúrate de que este pack esté aquí

        # Asegúrate de que el botón se empaquete después de los otros elementos   

    def generar_grafico(self):
        sexo = self.sexo_var.get()
        edad = self.filtro_edad.get()
        try:
            edad = int(edad) if edad else None
        except ValueError:
            edad = None
        
        color = self.color_var.get()
        estilo = self.estilo_var.get()
        
        grafico = GraficoDatos()
        grafico.generar_grafico(sexo=sexo, edad=edad, color=color, estilo=estilo)

    def abrir_formulario_agregar(self):
        formulario = FormularioDatos(tk.Toplevel(self.master))

    def eliminar_dato(self, dato_id):
        consultas = ConsultasDatos()
        query = f"DELETE FROM ENCUESTA WHERE idEncuesta = {dato_id}"
        consultas.ejecutar_query(query)
        self.tabla_datos.eliminar_fila(dato_id)

    def abrir_formulario_eliminar(self):
        formulario = FormularioEliminar(tk.Toplevel(self.master), self.tabla_datos)

    def abrir_formulario_editar(self):
        formulario = FormularioEditar(tk.Toplevel(self.master))

    def exportar_datos(self):
        consultas = ConsultasDatos()
        datos = consultas.obtener_datos("SELECT * FROM ENCUESTA")
        if datos is not None:
            consultas.exportar_a_excel(datos, "resources/data/datos_encuesta.xlsx")