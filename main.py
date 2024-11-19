from tkinter import Tk
from scripts.interfaz_usuario import InterfazUsuario
from scripts.conexion_bd import ConexionBaseDatos




# Crear la conexión a la base de datos
conexion = ConexionBaseDatos()

# Crear la ventana de Tkinter (root)
root = Tk()

# Crear la interfaz de usuario y pasarle la conexión como argumento
app = InterfazUsuario(root, conexion)

# Ejecutar el loop de la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos cuando se cierre la aplicación
conexion.cerrar_conexion()
