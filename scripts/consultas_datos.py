from tkinter import messagebox
import pandas as pd
from scripts.conexion_bd import ConexionBaseDatos
import mysql.connector

class ConsultasDatos:
    def __init__(self):
        """Inicializa la conexión con la base de datos a través de ConexionBaseDatos."""
        self.bd = ConexionBaseDatos()  # Esto obtiene la conexión de la clase ConexionBaseDatos

    def obtener_datos(self, query, params=None):
        """Obtiene los datos de la base de datos con la consulta y parámetros proporcionados."""
        if self.bd.conexion is not None:
            try:
                cursor = self.bd.conexion.cursor(dictionary=True)
                
                # Convert params to the correct format
                if params is not None:
                    # If params is a dictionary, convert to a tuple of values
                    if isinstance(params, dict):
                        params = tuple(params.values())
                    # Ensure params is a tuple
                    elif not isinstance(params, tuple):
                        params = (params,)
                    
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                    
                results = cursor.fetchall()
                df = pd.DataFrame(results)
                return df
            except Exception as e:
                print(f"Error al obtener los datos: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("No se pudo obtener los datos debido a un problema de conexión.")
        return None

    def obtener_datos_por_id(self, dato_id):
        """Recupera los datos de la encuesta utilizando el ID proporcionado."""
        query = "SELECT * FROM ENCUESTA WHERE idEncuesta = %s"
        params = (dato_id,)  # Convertimos el ID en una tupla para pasarlo como parámetro
        df = self.obtener_datos(query, params)
        
        if df is not None and not df.empty:
            return df.iloc[0]  # Retorna la primera fila como un objeto Series, que será equivalente a un diccionario
        else:
            return None  # Si no se encuentran datos, retorna None

    def exportar_a_excel(self, df, nombre_archivo):
        """Exporta el DataFrame a un archivo Excel."""
        if df is not None:
            try:
                df.to_excel(nombre_archivo, index=False)
                print(f"Datos exportados exitosamente a {nombre_archivo}.")
            except Exception as e:
                print(f"Error al exportar a Excel: {e}")
        else:
            print("No se pudo exportar a Excel debido a datos vacíos.")

    def insertar_datos(self, id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                    bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                    problemas_digestivos, tension_alta, dolor_cabeza):
        """Inserta los datos en la base de datos."""
        if self.bd.conexion is not None:
            try:
                query = """
                INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, 
                BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, 
                DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                
                # Convertir "Sí" y "No" a 'S' y 'N'
                perdidas_control = 1 if perdidas_control == 'Sí' else 0
                diversion_dependencia_alcohol = 'S' if diversion_dependencia_alcohol == 'Sí' else 'N'
                problemas_digestivos = 'S' if problemas_digestivos == 'Sí' else 'N'
                tension_alta = 'S' if tension_alta == 'Sí' else 'N'
                dolor_cabeza = 'S' if dolor_cabeza == 'Sí' else 'N'

                # Ejecutar la consulta
                cursor = self.bd.conexion.cursor()
                cursor.execute(query, (id_encuesta, edad, sexo, bebidas_semana, cervezas_semana,
                                    bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana,
                                    perdidas_control, diversion_dependencia_alcohol,
                                    problemas_digestivos, tension_alta, dolor_cabeza))
                self.bd.conexion.commit()  # Confirmar cambios en la base de datos
                print("Datos insertados correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {str(e)}")
            finally:
                cursor.close()  # Cerrar el cursor
        else:
            print("No se pudo insertar los datos debido a un problema de conexión.")
            
    def obtener_max_id(self):
        """Obtiene el máximo ID de encuesta en la base de datos."""
        query = "SELECT MAX(idEncuesta) FROM ENCUESTA"
        df = self.obtener_datos(query)
        if df is not None and not df.empty:
            max_id = df.iloc[0, 0]
            return max_id + 1
        return 1  # Si no hay resultados, el próximo ID será 1

    def verificar_id_unico(self, id_encuesta):
        """Verifica si el ID de encuesta es único en la base de datos."""
        query = "SELECT COUNT(*) FROM ENCUESTA WHERE idEncuesta = %s"
        df = self.obtener_datos(query, (id_encuesta,))
        if df is not None and df.iloc[0, 0] == 0:  # Si el resultado es 0, el ID es único
            return True
        return False

    def verificar_id_existente(self, id_encuesta):
        """Verifica si el ID de encuesta existe en la base de datos."""
        query = "SELECT COUNT(*) FROM ENCUESTA WHERE idEncuesta = %s"
        df = self.obtener_datos(query, (id_encuesta,))
        if df is not None and df.iloc[0, 0] > 0:
            return True
        return False

    def actualizar_datos(self, consulta, params):
        """Actualiza los datos en la base de datos según la consulta proporcionada."""
        if self.bd.conexion is not None:
            try:
                cursor = self.bd.conexion.cursor()
                cursor.execute(consulta, params)
                self.bd.conexion.commit()
                print("Datos actualizados correctamente.")
                return True
            except Exception as e:
                print(f"Error al actualizar los datos: {e}")
                return False
            finally:
                cursor.close()  # Cierra el cursor
        else:
            print("No se pudo actualizar los datos debido a un problema de conexión.")
            return False

    def eliminar_datos(self, id_encuesta):
        """Elimina una encuesta de la base de datos según el ID."""
        if self.bd.conexion is not None:
            try:
                if self.verificar_id_existente(id_encuesta):
                    query = "DELETE FROM ENCUESTA WHERE idEncuesta = %s"
                    cursor = self.bd.conexion.cursor()
                    cursor.execute(query, (id_encuesta,))
                    self.bd.conexion.commit()
                    print("Encuesta eliminada correctamente.")
                    return True
                else:
                    print("El ID de encuesta no existe.")
                    return False
            except Exception as e:
                print(f"Error al eliminar los datos: {e}")
                return False
            finally:
                cursor.close()  # Cierra el cursor
        else:
            print("No se pudo eliminar los datos debido a un problema de conexión.")
            return False

