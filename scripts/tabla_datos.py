import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class TablaDatos:
    def __init__(self, master, callback_eliminar):
        self.master = master
        self.callback_eliminar = callback_eliminar  # Función para manejar la eliminación

        # Configurar estilo para ttk
        style = ttk.Style()
        style.configure(
            "Treeview",
            background="#ffffff",
            foreground="#000000",
            fieldbackground="#ffffff",
            bordercolor="#cccccc",
            relief="flat",
        )
        style.map(
            "Treeview",
            background=[("selected", "#e6e6e6")],
            foreground=[("selected", "#000000")],
        )
        style.configure(
            "Treeview.Heading",
            background="#f0f0f0",
            foreground="#000000",
            bordercolor="#cccccc",
            relief="raised",
            font=("Helvetica", 10, "bold"),
        )

        # Crear Treeview
        self.treeview = ttk.Treeview(master, show="headings")
        self.treeview["columns"] = tuple(range(1, 14))  # 13 columnas
        for i in range(1, 14):
            self.treeview.heading(f"#{i}", text=f"Columna {i}")
            self.treeview.column(f"#{i}", width=100, anchor="center")

        # Scrollbars
        self.v_scroll = ttk.Scrollbar(
            master, orient="vertical", command=self.treeview.yview
        )
        self.h_scroll = ttk.Scrollbar(
            master, orient="horizontal", command=self.treeview.xview
        )
        self.treeview.configure(
            yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set
        )

        # Empaquetar Treeview y Scrollbars
        self.treeview.pack(fill="both", expand=True)
        self.v_scroll.pack(side="right", fill="y")
        self.h_scroll.pack(side="bottom", fill="x")

        
    def actualizar_datos(self, datos):
        """Llena el Treeview con los datos proporcionados."""
        # Limpiar el Treeview antes de agregar nuevos datos
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Insertar los datos en el Treeview
        for index, row in datos.iterrows():
            # Asegurar que las columnas sean adecuadas
            self.treeview.insert("", "end", values=row.tolist())

    def eliminar_fila(self):
        """Elimina la fila seleccionada del Treeview."""
        selected_item = self.treeview.focus()
        if selected_item:
            dato_id = self.treeview.item(selected_item)["values"][0]  # Asume que el ID es la primera columna
            confirmacion = messagebox.askyesno(
                "Confirmación", f"¿Estás seguro de eliminar el registro con ID {dato_id}?"
            )
            if confirmacion:
                self.treeview.delete(selected_item)
                self.callback_eliminar(dato_id)
                print(f"Eliminado registro con ID: {dato_id}")
            else:
                print("Eliminación cancelada.")
    
    def obtener_nombres_columnas(self):
        # Usamos el cursor ya definido en ConexionBaseDatos
        cursor = self.conexion_base_datos.cursor  # Usamos el cursor de ConexionBaseDatos
        
        # Ahora puedes realizar la consulta para obtener los nombres de las columnas
        cursor.execute("DESCRIBE ENCUESTA")
        columnas = [desc[0] for desc in cursor.fetchall()]
        
        return columnas