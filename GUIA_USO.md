# Guía de Uso - QR Generator Pro

## 🎯 Inicio Rápido

### Instalación en 3 pasos:

1. **Doble clic en `install.bat`** - Instala todas las dependencias automáticamente
2. **Doble clic en `run.bat`** - Ejecuta la aplicación
3. **¡Listo!** - Ya puedes generar códigos QR

## 📖 Guía Detallada

### Generar tu Primer QR

1. **Ingresa una URL**
   - Escribe o pega la URL en el campo "URL"
   - Ejemplo: `https://www.google.com`

2. **Agrega un Logo (Opcional)**
   - Haz clic en "📁 Seleccionar Logo"
   - Elige una imagen (PNG, JPG, etc.)
   - El logo aparecerá en el centro del QR
   - Para quitar el logo, haz clic en "✖"

3. **Agrega Notas (Opcional)**
   - Escribe una descripción o nota
   - Ejemplo: "QR para sitio web principal"
   - Útil para organizar tu historial

4. **Genera el QR**
   - Haz clic en "✨ Generar QR"
   - El QR aparecerá en la vista previa
   - Se guardará automáticamente en tu historial

### Gestionar el Historial

#### Buscar QRs
- Usa la barra de búsqueda en el panel derecho
- Busca por URL o por notas
- Los resultados se filtran en tiempo real

#### Acciones Disponibles

Cada QR en el historial tiene botones de acción:

- **👁️ Ver**: Abre el QR en una ventana nueva
- **📋 Copiar**: Copia la URL al portapapeles
- **🌐 Abrir**: Abre la URL en tu navegador
- **🗑️ Eliminar**: Elimina el QR del historial

### Guardar y Exportar

#### Guardar QR Generado
1. Después de generar un QR, haz clic en "💾 Guardar Como"
2. Elige la ubicación y nombre del archivo
3. Selecciona el formato (PNG o JPG)

#### Abrir Carpeta de QRs
- Haz clic en "📂 Abrir Carpeta"
- Se abrirá la carpeta `qr_images/` con todos tus QRs

## 💡 Consejos y Trucos

### Logos Recomendados
- **Formato**: PNG con fondo transparente funciona mejor
- **Tamaño**: Cualquier tamaño (se redimensiona automáticamente)
- **Proporción**: El logo ocupará ~20% del QR
- **Contraste**: Usa logos con buen contraste para mejor legibilidad

### URLs Válidas
- Incluye siempre `http://` o `https://`
- Ejemplos válidos:
  - `https://www.ejemplo.com`
  - `https://wa.me/1234567890`
  - `mailto:correo@ejemplo.com`
  - `tel:+1234567890`

### Organización
- Usa las **notas** para categorizar tus QRs
- Ejemplos de notas útiles:
  - "Redes sociales - Instagram"
  - "Menú restaurante - Enero 2026"
  - "Evento - Conferencia Tech"

## 🔧 Solución de Problemas

### La aplicación no inicia
1. Verifica que Python esté instalado: `python --version`
2. Ejecuta `install.bat` nuevamente
3. Revisa que todas las dependencias se instalaron correctamente

### Error al generar QR
- Verifica que la URL sea válida
- Si usas logo, asegúrate que el archivo existe
- Verifica que tengas permisos de escritura en la carpeta

### El logo no se ve bien
- Usa imágenes con buena resolución
- Evita logos muy complejos o con detalles pequeños
- Prueba con fondo blanco o transparente

### No puedo ver el historial
- Verifica que el archivo `qr_history.db` exista
- Intenta generar un nuevo QR
- Reinicia la aplicación

## 📊 Estadísticas

En el panel de historial puedes ver:
- **Total**: Cantidad total de QRs generados
- **URLs únicas**: Cantidad de URLs diferentes

## 🎨 Personalización Avanzada

### Modificar el Código

Si sabes Python, puedes personalizar:

1. **Colores del QR** (`qr_generator.py`):
   - Modifica `fill_color` y `back_color`
   - Usa la función `generate_qr_with_custom_colors()`

2. **Tamaño del QR** (`qr_generator.py`):
   - Cambia el parámetro `box_size` (default: 10)
   - Cambia el parámetro `border` (default: 2)

3. **Tema de la Interfaz** (`main.py`):
   - Cambia `ctk.set_appearance_mode("dark")` a `"light"`
   - Modifica `ctk.set_default_color_theme("blue")` a otros colores

## 📁 Estructura de Archivos

```
qr-generator-app/
├── main.py              # Aplicación principal
├── qr_generator.py      # Generador de QR
├── database.py          # Base de datos
├── requirements.txt     # Dependencias
├── install.bat          # Instalador
├── run.bat             # Ejecutor
├── README.md           # Documentación
├── GUIA_USO.md         # Esta guía
├── qr_images/          # QRs generados (auto-creada)
└── qr_history.db       # Base de datos (auto-creada)
```

## 🚀 Casos de Uso

### 1. Restaurante - Menú Digital
- Genera QR con logo del restaurante
- URL: Link a menú en PDF o sitio web
- Nota: "Menú Principal - 2026"

### 2. Eventos - Registro
- QR para formulario de registro
- URL: Google Forms o similar
- Nota: "Conferencia Tech - Registro"

### 3. Redes Sociales
- QR para perfil de Instagram/Facebook
- URL: Link directo al perfil
- Nota: "Instagram - Empresa"

### 4. WiFi
- QR para conectar a WiFi (formato especial)
- URL: `WIFI:T:WPA;S:NombreRed;P:Contraseña;;`
- Nota: "WiFi Oficina"

### 5. Contacto
- QR con vCard
- URL: Archivo vCard en línea
- Nota: "Tarjeta de presentación"

## 🔐 Privacidad y Seguridad

- **Datos locales**: Todo se almacena en tu computadora
- **Sin internet**: La app funciona 100% offline
- **Sin telemetría**: No enviamos ningún dato
- **Base de datos local**: SQLite en tu disco

## 📞 Soporte

Si tienes problemas o sugerencias:
1. Revisa esta guía
2. Verifica los requisitos del sistema
3. Consulta el README.md para más detalles

---

**¡Disfruta generando códigos QR profesionales! 🎉**
