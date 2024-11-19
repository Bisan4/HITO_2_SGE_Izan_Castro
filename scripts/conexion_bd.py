# conexion_base_datos.py
import mysql.connector

class ConexionBaseDatos:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost", user="root", password="curso", database="encuestas", auth_plugin="mysql_native_password"
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
            else:
                print("No se pudo conectar.")
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
            self.conexion = None

    def ejecutar_query(self, query, datos=None):
        if self.conexion is not None:
            try:
                if isinstance(datos, dict):  # Si es un diccionario, lanzamos un error
                    raise TypeError("No se puede pasar un diccionario como parámetro SQL")
                if datos is not None and not isinstance(datos, tuple):
                    datos = tuple(datos)  # Asegurarse de que sea una tupla
                self.cursor.execute(query, datos)
                self.conexion.commit()
            except mysql.connector.Error as e:
                print(f"Error al ejecutar la consulta: {e}")
            except TypeError as te:
                print(f"Error de tipo: {te}")
        else:
            print("No hay conexión a la base de datos.")



    def obtener_datos(self, query):
        if self.conexion is not None:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        return None

    def cerrar_conexion(self):
        if self.conexion is not None and self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("Conexión cerrada.")
