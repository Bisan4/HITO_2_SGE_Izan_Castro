import matplotlib.pyplot as plt
from scripts.consultas_datos import ConsultasDatos
import tkinter as tk
from tkinter import ttk
from scripts.modern_styles import ModernStyles  # Asegúrate de importar ModernStyles

class GraficoDatos:
    def __init__(self):
        self.consultas = ConsultasDatos()

    def generar_grafico(self, sexo=None, edad=None, color='blue', alpha=0.7, estilo='dark_background', 
                        guardar=False, nombre_archivo='grafico.png', titulo='Relación entre Edad y Bebidas por Semana'):
        # Establecer el estilo de la gráfica
        plt.style.use(estilo)
        
        # Construir la consulta SQL dinámica en base a los filtros
        query = "SELECT edad, BebidasSemana FROM ENCUESTA WHERE 1=1"
        if sexo == "Hombre":
            query += " AND Sexo = 'Hombre'"
        elif sexo == "Mujer":
            query += " AND Sexo = 'Mujer'"

        if edad is not None:
            query += f" AND edad > {edad}"

        # Obtener los datos filtrados
        datos = self.consultas.obtener_datos(query)

        if datos is None or datos.empty:
            print("No se pudo obtener los datos para generar el gráfico.")
            return

        # Crear el gráfico de barras
        plt.figure(figsize=(10, 8))

        # Ajustamos los valores para el gráfico de barras
        edades = datos["edad"].value_counts().sort_index().index
        bebidas_por_semana = datos["edad"].value_counts().sort_index().values
        
        # Crear el gráfico de barras
        plt.bar(edades, bebidas_por_semana, color=color, alpha=alpha)

        # Configuración de títulos y etiquetas
        plt.title(titulo, fontsize=16)
        plt.xlabel("Edad", fontsize=14)
        plt.ylabel("Número de Personas", fontsize=14)

        # Mostrar el gráfico
        if guardar:
            plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        plt.show()

    def crear_interfaz(self):
        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("Generador de Gráficos")
        
        # Aplicar los estilos con ModernStyles
        ModernStyles.apply_styles(ventana)
        
        # Función para actualizar el gráfico
        def actualizar_grafico():
            sexo = sexo_var.get()
            edad = edad_var.get()
            color = color_var.get()
            estilo = estilo_var.get()
            self.generar_grafico(sexo=sexo, edad=edad, color=color, estilo=estilo)

        # Filtros de sexo
        sexo_var = tk.StringVar(value='Todos')
        opciones_sexo = ['Todos', 'Hombre', 'Mujer']
        sexo_label = ttk.Label(ventana, text="Sexo", style="Modern.TLabel")
        sexo_label.grid(row=0, column=0, padx=10, pady=5)  
        sexo_menu = ttk.Combobox(ventana, textvariable=sexo_var, values=opciones_sexo, state="readonly", style="Modern.TCombobox")
        sexo_menu.grid(row=0, column=1, padx=10, pady=5)  

        # Filtro de edad mínima
        edad_var = tk.IntVar(value=0)
        edad_label = ttk.Label(ventana, text="Edad mínima", style="Modern.TLabel")
        edad_label.grid(row=1, column=0, padx=10, pady=5)  
        edad_entrada = ttk.Entry(ventana, textvariable=edad_var, style="Modern.TEntry")
        edad_entrada.grid(row=1, column=1, padx=10, pady=5)  

        # Filtro de color
        color_var = tk.StringVar(value='blue')
        color_label = ttk.Label(ventana, text="Color", style="Modern.TLabel")
        color_label.grid(row=2, column=0, padx=10, pady=5)  
        color_menu = ttk.Combobox(ventana, textvariable=color_var, values=['blue', 'green', 'red', 'orange', 'purple'], state="readonly", style="Modern.TCombobox")
        color_menu.grid(row=2, column=1, padx=10, pady=5)  

        # Filtro de estilo
        estilo_var = tk.StringVar(value='dark_background')
        opciones_estilo = ['dark_background', 'ggplot']
        estilo_label = ttk.Label(ventana, text="Estilo de Gráfico", style="Modern.TLabel")
        estilo_label.grid(row=3, column=0, padx=10, pady=5)  
        estilo_menu = ttk.Combobox(ventana, textvariable=estilo_var, values=opciones_estilo, state="readonly", style="Modern.TCombobox")
        estilo_menu.grid(row=3, column=1, padx=10, pady=5)  

        # Botón para actualizar el gráfico
        btn_actualizar = ttk.Button(ventana, text="Actualizar Gráfico", command=actualizar_grafico, style="Modern.TButton")
        btn_actualizar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)  

        # Ajustar el tamaño de la ventana
        ventana.geometry("400x300")  # Ajusta el tamaño de la ventana según sea necesario

        ventana.mainloop()