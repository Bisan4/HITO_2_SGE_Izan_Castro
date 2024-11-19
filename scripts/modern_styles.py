import tkinter as tk
from tkinter import ttk

class ModernStyles:
    # Colores
    PRIMARY_COLOR = "#2563eb"  # Azul principal
    SECONDARY_COLOR = "#3b82f6"  # Azul secundario
    BACKGROUND_COLOR = "#f8fafc"  # Fondo principal claro
    SECONDARY_BACKGROUND = "#f1f5f9"  # Fondo secundario
    TEXT_COLOR = "#1e293b"  # Color texto principal
    SECONDARY_TEXT = "#64748b"  # Color texto secundario
    SUCCESS_COLOR = "#10b981"  # Verde para éxito
    WARNING_COLOR = "#f59e0b"  # Amarillo para advertencias
    ERROR_COLOR = "#ef4444"  # Rojo para errores
    BORDER_COLOR = "#e2e8f0"  # Color de bordes

    @classmethod
    def apply_styles(cls, root):
        # Configurar estilo general
        style = ttk.Style()
        style.theme_use('clam')  # Usar tema clam como base

        # Configuración de la ventana principal
        root.configure(bg=cls.BACKGROUND_COLOR)

        # Estilo para frames
        style.configure(
            "Modern.TFrame",
            background=cls.BACKGROUND_COLOR
        )

        # Estilo para etiquetas
        style.configure(
            "Modern.TLabel",
            background=cls.BACKGROUND_COLOR,
            foreground=cls.TEXT_COLOR,
            font=("Segoe UI", 10)
        )

        # Estilo para etiquetas de título
        style.configure(
            "ModernTitle.TLabel",
            background=cls.BACKGROUND_COLOR,
            foreground=cls.PRIMARY_COLOR,
            font=("Segoe UI", 16, "bold")
        )

        # Estilo para botones
        style.configure(
            "Modern.TButton",
            background=cls.PRIMARY_COLOR,
            foreground="white",
            font=("Segoe UI", 10),
            padding=(15, 8),
            borderwidth=0
        )
        style.map(
            "Modern.TButton",
            background=[("active", cls.SECONDARY_COLOR)],
            foreground=[("active", "white")]
        )

        # Estilo para botones de acción secundaria
        style.configure(
            "ModernSecondary.TButton",
            background=cls.SECONDARY_BACKGROUND,
            foreground=cls.TEXT_COLOR,
            font=("Segoe UI", 10),
            padding=(15, 8),
            borderwidth=0
        )
        style.map(
            "ModernSecondary.TButton",
            background=[("active", cls.BORDER_COLOR)],
            foreground=[("active", cls.TEXT_COLOR)]
        )

        # Estilo para entradas
        style.configure(
            "Modern.TEntry",
            fieldbackground="white",
            background="white",
            foreground=cls.TEXT_COLOR,
            borderwidth=1,
            padding=(10, 5),
            font=("Segoe UI", 10)
        )

        # Estilo para combobox
        style.configure(
            "Modern.TCombobox",
            fieldbackground="white",
            background="white",
            foreground=cls.TEXT_COLOR,
            borderwidth=1,
            padding=(10, 5),
            font=("Segoe UI", 10)
        )

        # Estilo para radiobuttons
        style.configure(
            "Modern.TRadiobutton",
            background=cls.BACKGROUND_COLOR,
            foreground=cls.TEXT_COLOR,
            font=("Segoe UI", 10)
        )

        # Estilo para el treeview (tabla)
        style.configure(
            "Modern.Treeview",
            background="white",
            foreground=cls.TEXT_COLOR,
            fieldbackground="white",
            font=("Segoe UI", 10),
            rowheight=30
        )
        style.configure(
            "Modern.Treeview.Heading",
            background=cls.SECONDARY_BACKGROUND,
            foreground=cls.TEXT_COLOR,
            font=("Segoe UI", 10, "bold")
        )
        style.map(
            "Modern.Treeview",
            background=[("selected", cls.PRIMARY_COLOR)],
            foreground=[("selected", "white")]
        )

    @classmethod
    def create_rounded_frame(cls, parent, **kwargs):
        """Crea un frame con esquinas redondeadas"""
        frame = tk.Frame(
            parent,
            bg=cls.BACKGROUND_COLOR,
            highlightbackground=cls.BORDER_COLOR,
            highlightthickness=1,
            bd=0,
            **kwargs
        )
        return frame

    @classmethod
    def create_card_frame(cls, parent, **kwargs):
        """Crea un frame tipo tarjeta con sombra y esquinas redondeadas"""
        frame = tk.Frame(
            parent,
            bg="white",
            highlightbackground=cls.BORDER_COLOR,
            highlightthickness=1,
            bd=0,
            relief="solid",
            **kwargs
        )
        # Agregar padding utilizando padx y pady
        frame.grid(padx=20, pady=20)  # Usa grid() para agregar el padding aquí
        return frame
