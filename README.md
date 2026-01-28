# QR Generator Pro

Aplicación de escritorio multiplataforma (Windows, macOS, Linux) que genera códigos QR con logo personalizable y almacena el historial en una base de datos local.

## 🚀 Características

- ✨ **Generación de QR**: Crea códigos QR a partir de URLs
- 🖼️ **Logo personalizable**: Inserta tu logo en el centro del QR
- 💾 **Base de datos local**: Almacena historial de QRs generados con SQLite
- 🔍 **Búsqueda**: Encuentra QRs por URL o notas
- 📊 **Estadísticas**: Visualiza total de QRs y URLs únicas
- 🎨 **Interfaz moderna**: Diseño oscuro con CustomTkinter
- 📝 **Notas**: Agrega notas a cada QR generado
- 🌐 **Acciones rápidas**: Abre URLs, copia al portapapeles, visualiza QRs

## 📋 Requisitos

- Python 3.8 o superior
- Windows 10/11, macOS 10.14+, o Linux

## 🔧 Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

## 🎮 Uso

1. **Ejecutar la aplicación**:
```bash
python main.py
```

2. **Generar un QR**:
   - Ingresa la URL en el campo correspondiente
   - (Opcional) Selecciona un logo para insertar en el centro
   - (Opcional) Agrega notas descriptivas
   - Haz clic en "Generar QR"

3. **Gestionar historial**:
   - Visualiza todos los QRs generados en el panel derecho
   - Busca por URL o notas
   - Visualiza, copia URL, abre en navegador o elimina QRs

## 📁 Estructura del Proyecto

```
qr-generator-app/
├── main.py              # Interfaz gráfica principal
├── qr_generator.py      # Lógica de generación de QR
├── database.py          # Gestión de base de datos SQLite
├── requirements.txt     # Dependencias del proyecto
├── qr_images/          # Carpeta donde se guardan los QRs (se crea automáticamente)
└── qr_history.db       # Base de datos SQLite (se crea automáticamente)
```

## 🎨 Capturas de Pantalla

La aplicación cuenta con:
- Panel izquierdo para generar QRs con vista previa
- Panel derecho con historial completo y búsqueda
- Tema oscuro moderno
- Botones de acción intuitivos

## 🛠️ Tecnologías Utilizadas

- **Python 3**: Lenguaje principal
- **CustomTkinter**: Interfaz gráfica moderna
- **qrcode**: Generación de códigos QR
- **Pillow (PIL)**: Procesamiento de imágenes
- **SQLite**: Base de datos local

## 📝 Notas

- Los QRs se guardan automáticamente en la carpeta `qr_images/`
- La base de datos se crea automáticamente en `qr_history.db`
- El logo debe ser una imagen (PNG, JPG, GIF, BMP)
- El logo se redimensiona automáticamente al 20% del tamaño del QR

## 🔮 Mejoras Futuras

- Exportar historial a CSV/Excel
- Personalización de colores del QR
- Generación masiva de QRs desde archivo
- Soporte para vCard y WiFi QR
- Temas personalizables
- Exportar QR con diferentes tamaños

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

## 👨‍💻 Autor

Creado con ❤️ para facilitar la generación de códigos QR profesionales.
