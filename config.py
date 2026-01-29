# Configuración de QR Generator Pro
# Edita este archivo para personalizar la aplicación

APP_VERSION = "1.1.0"

# === CONFIGURACIÓN DE QR ===

# Tamaño del QR (1-40, donde mayor es más grande)
QR_SIZE = 10

# Grosor del borde (mínimo 4)
QR_BORDER = 2

# Nivel de corrección de errores
# L = 7% de corrección
# M = 15% de corrección
# Q = 25% de corrección
# H = 30% de corrección (recomendado si usas logo)
ERROR_CORRECTION = "H"

# === COLORES POR DEFECTO ===

# Color del QR (negro por defecto)
QR_FILL_COLOR = "black"

# Color de fondo (blanco por defecto)
QR_BACK_COLOR = "white"

# === CONFIGURACIÓN DE LOGO ===

# Tamaño del logo como fracción del QR (0.1 = 10%, 0.2 = 20%, etc.)
LOGO_SIZE_RATIO = 0.2

# Margen alrededor del logo (1.0 = sin margen, 1.2 = 20% de margen)
LOGO_MARGIN_RATIO = 1.2

# === CONFIGURACIÓN DE INTERFAZ ===

# Tema de la aplicación ("System", "Dark", "Light")
APPEARANCE_MODE = "System"

# Esquema de color ("blue", "green", "dark-blue")
COLOR_THEME = "blue"

# Tamaño de ventana por defecto (ancho x alto)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# === CONFIGURACIÓN DE BASE DE DATOS ===

# Nombre del archivo de base de datos
DB_NAME = "qr_history.db"

# Límite de registros a mostrar en historial
HISTORY_LIMIT = 100

# === CONFIGURACIÓN DE ARCHIVOS ===

# Carpeta donde se guardan los QRs
OUTPUT_DIR = "qr_images"

# Formato de nombre de archivo (usa strftime)
# %Y = año, %m = mes, %d = día, %H = hora, %M = minuto, %S = segundo
FILENAME_FORMAT = "qr_%Y%m%d_%H%M%S.png"

# === CONFIGURACIÓN AVANZADA ===

# Habilitar logs de depuración
DEBUG_MODE = False

# Calidad de compresión para JPEG (1-100)
JPEG_QUALITY = 95

# === COLORES PREDEFINIDOS ===
# Puedes usar estos en lugar de los colores por defecto

PRESET_COLORS = {
    "classic": {
        "fill": "black",
        "back": "white"
    },
    "blue": {
        "fill": "#1E40AF",
        "back": "#EFF6FF"
    },
    "green": {
        "fill": "#166534",
        "back": "#F0FDF4"
    },
    "red": {
        "fill": "#991B1B",
        "back": "#FEF2F2"
    },
    "purple": {
        "fill": "#6B21A8",
        "back": "#FAF5FF"
    },
    "gradient": {
        "fill": "#1E3A8A",
        "back": "#DBEAFE"
    }
}

# === URLS DE EJEMPLO ===
# URLs comunes para pruebas rápidas

EXAMPLE_URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
]

# === NOTAS ===
# - Reinicia la aplicación después de cambiar la configuración
# - Los colores pueden ser nombres ("red", "blue") o códigos hex ("#FF0000")
# - El tamaño del logo se ajusta automáticamente para no interferir con el QR
