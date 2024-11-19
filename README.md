# Aplicación de Seguimiento de Consumo de Alcohol

## Descripción del Proyecto
Esta aplicación de escritorio, desarrollada para la Clínica del Dr. Fernando, permite gestionar y analizar encuestas sobre el consumo de alcohol y su impacto en la salud. Utiliza una interfaz moderna con Tkinter, procesamiento de datos con pandas y visualizaciones con matplotlib.

## Características Principales

### Interfaz de Usuario
La aplicación cuenta con una interfaz moderna y intuitiva dividida en secciones principales:


Elementos de la interfaz:
- **Título Principal**: "Consumo de Alcohol y Salud"
- **Botones de Acción**:
  1. Consultar Datos
  2. Añadir Datos
  3. Editar Datos
  4. Eliminar Datos
  5. Generar Gráfico

#### Área de Filtros
Permite refinar la visualización y consulta de datos:
- **Filtro de Sexo**:
  - Hombre
  - Mujer
  - Ambos Géneros
- **Filtro de Edad**: Selección de edad mínima

### Operaciones CRUD

#### 1. Consulta de Datos
- Vista de tabla con todos los registros
- Filtrado por sexo y edad
- Exportación a Excel

#### 2. Añadir Datos
Formulario completo para registro de nueva encuesta:
- Datos personales (edad, sexo)
- Consumo de alcohol:
  - Bebidas por semana
  - Cervezas por semana
  - Bebidas en fin de semana
  - Bebidas destiladas
  - Vinos

#### 3. Editar Datos
- Búsqueda por ID de encuesta
- Modificación de todos los campos
- Validación de datos

#### 4. Eliminar Datos
- Eliminación por ID de encuesta
- Confirmación de eliminación

### Generación de Gráficos
Características avanzadas de visualización:
- Selección de estilo de gráfico
- Personalización de colores
- Filtros de datos
- Tipos de gráficos:
  - Relación edad-consumo
  - Distribución por género
  - Tendencias de consumo

### Configuración de Conexión
En el archivo `conexion_bd.py`, ajustar los parámetros de conexión:
```python
self.conexion = mysql.connector.connect(
    host="localhost", 
    user="tu_usuario", 
    password="tu_contraseña", 
    database="encuestas", 
    auth_plugin="mysql_native_password"
)
```

## Requisitos Técnicos Detallados

### Dependencias
- Python 3.8+
- Tkinter
- mysql-connector-python
- matplotlib
- pandas

```bash
pip install tkinter
pip install mysql-connector-python
pip install matplotlib
pip install pandas
```

### Instalación Detallada

#### Windows
1. Descargar Python desde sitio oficial
2. Marcar opción "Añadir Python al PATH"
3. Abrir CMD y ejecutar:
   ```
   pip install tkinter mysql-connector-python matplotlib pandas
   ```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3-tk python3-pip
pip3 install mysql-connector-python matplotlib pandas
```

#### macOS
```bash
brew install python
pip3 install tkinter mysql-connector-python matplotlib pandas
```

## Configuración Avanzada

### Estructura de Archivos
```
proyecto/
│
├── main.py                 # Punto de entrada
├── scripts/
│   ├── conexion_bd.py      # Conexión a MySQL
│   ├── consultas_datos.py  # Consultas SQL
│   ├── formulario_datos.py # Formulario añadir
│   ├── formulario_editar.py# Formulario edición
│   ├── grafico_datos.py    # Generación gráficos
│   └── modern_styles.py    # Estilos de interfaz
│
├── resources/
│   └── data/               # Archivos exportados
│
└── README.md
```

### Configuración de MySQL
1. Crear usuario específico
```sql
CREATE USER 'usuario_app'@'localhost' IDENTIFIED BY 'contraseña_segura';
GRANT ALL PRIVILEGES ON encuestas.* TO 'usuario_app'@'localhost';
FLUSH PRIVILEGES;
```

### Configuración de MySQL(Crear BDD)
1. Crear la BDD y introduci rlo datos
```sql

DROP DATABASE IF EXISTS ENCUESTAS;
CREATE DATABASE ENCUESTAS;
USE ENCUESTAS;

CREATE TABLE ENCUESTA (
	idEncuesta int primary key,
    edad int,
    Sexo varchar(7),
	BebidasSemana int,
    CervezasSemana int,
	BebidasFinSemana int, 
    BebidasDestiladasSemana	int,
    VinosSemana	int, 
    PerdidasControl varchar(10), 
    DiversionDependenciaAlcohol	varchar(10),
    ProblemasDigestivos	varchar(10),
    TensionAlta	varchar(10),
    DolorCabeza varchar(10)
);


```

## Seguridad y Mejores Prácticas

### Validación de Datos
- Campos numéricos validados
- Control de rangos de edad
- Manejo de nulos
- Conversión de tipos

### Gestión de Errores
- Mensajes informativos
- Control de excepciones
- Log de errores

## Solución de Problemas

### Errores Comunes
- Verificar conexión MySQL
- Comprobar instalación de dependencias
- Revisar permisos de base de datos

## Posibles Mejoras
- Autenticación de usuarios
- Exportación a más formatos
- Más tipos de gráficos estadísticos
- Análisis predictivo

## Contribuciones
1. Fork del repositorio
2. Crear rama de feature
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request

## Licencia
[Izan]

## Contacto
- Desarrollador: [Izan]
- Correo: [izan.castroromero.23@campusfp.es]
- Clínica: Dr. Fernando


