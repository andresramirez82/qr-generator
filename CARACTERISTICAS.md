# Características Detalladas - QR Generator Pro

## 🎨 Interfaz de Usuario

### Diseño de Dos Paneles

La aplicación está dividida en dos secciones principales:

#### Panel Izquierdo - Generación
- **Campo URL**: Entrada principal para la URL a codificar
- **Selector de Logo**: Botón para elegir imagen de logo
- **Campo de Notas**: Área de texto para agregar descripciones
- **Botón Generar**: Botón principal para crear el QR
- **Vista Previa**: Muestra el QR generado inmediatamente
- **Acciones Rápidas**: Guardar y abrir carpeta

#### Panel Derecho - Historial
- **Estadísticas**: Muestra total de QRs y URLs únicas
- **Barra de Búsqueda**: Filtrado en tiempo real
- **Lista de QRs**: Tarjetas con información de cada QR
- **Acciones por QR**: Ver, copiar, abrir, eliminar

## 🔧 Funcionalidades Técnicas

### Generación de QR

#### Algoritmo de Generación
1. **Validación de URL**: Verifica que la URL sea válida
2. **Creación del QR**: Usa la librería `qrcode` con corrección de errores alta
3. **Inserción de Logo**: 
   - Redimensiona el logo al 20% del tamaño del QR
   - Crea un fondo blanco para mejor contraste
   - Centra el logo perfectamente
4. **Guardado**: Genera nombre único con timestamp
5. **Registro en BD**: Almacena toda la información

#### Niveles de Corrección de Errores
- **Sin logo**: ERROR_CORRECT_L (7% de corrección)
- **Con logo**: ERROR_CORRECT_H (30% de corrección)

Esto permite que el QR funcione incluso con el logo en el centro.

### Base de Datos

#### Esquema de la Tabla `qr_codes`

```sql
CREATE TABLE qr_codes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    logo_path TEXT,
    image_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
)
```

#### Operaciones Disponibles
- **Insertar**: `add_qr()` - Agrega nuevo registro
- **Consultar**: `get_all_qrs()` - Obtiene todos los registros
- **Buscar**: `search_qrs()` - Búsqueda por URL o notas
- **Eliminar**: `delete_qr()` - Elimina registro y archivo
- **Estadísticas**: `get_stats()` - Calcula totales

### Procesamiento de Imágenes

#### Manejo de Logos
```python
# Proceso de inserción de logo:
1. Abrir imagen del logo
2. Calcular tamaño óptimo (1/5 del QR)
3. Redimensionar manteniendo proporción
4. Crear fondo blanco (20% más grande)
5. Centrar logo en el fondo
6. Pegar en el centro del QR
```

#### Formatos Soportados
- **Entrada**: PNG, JPG, JPEG, GIF, BMP
- **Salida**: PNG (por defecto), JPG (opcional)
- **Transparencia**: Soportada en logos PNG

## 📊 Características Avanzadas

### 1. Búsqueda Inteligente
- Búsqueda en tiempo real mientras escribes
- Busca en URLs y notas simultáneamente
- No distingue mayúsculas/minúsculas
- Resultados instantáneos

### 2. Gestión de Archivos
- **Nombres únicos**: Usa timestamp para evitar duplicados
- **Organización**: Todos los QRs en carpeta `qr_images/`
- **Limpieza**: Al eliminar de BD, también elimina archivo

### 3. Interfaz Responsiva
- **Tema oscuro**: Reduce fatiga visual
- **Colores modernos**: Paleta azul profesional
- **Botones intuitivos**: Iconos emoji para fácil identificación
- **Scrollable**: Historial con scroll infinito

### 4. Validaciones
- **URL vacía**: Alerta si no hay URL
- **Logo inexistente**: Genera sin logo si el archivo no existe
- **Errores de generación**: Mensajes de error descriptivos

## 🎯 Casos de Uso Especiales

### WiFi QR Codes
Formato especial para conectar a WiFi:
```
WIFI:T:WPA;S:NombreRed;P:Contraseña;;
```

Donde:
- `T`: Tipo de seguridad (WPA, WEP, nopass)
- `S`: Nombre de la red (SSID)
- `P`: Contraseña

### vCard (Tarjeta de Contacto)
```
BEGIN:VCARD
VERSION:3.0
FN:Juan Pérez
TEL:+1234567890
EMAIL:juan@ejemplo.com
END:VCARD
```

### Enlaces Especiales
- **WhatsApp**: `https://wa.me/1234567890`
- **Email**: `mailto:correo@ejemplo.com`
- **Teléfono**: `tel:+1234567890`
- **SMS**: `sms:+1234567890`
- **Ubicación**: `geo:40.7128,-74.0060`

## 🔒 Seguridad y Privacidad

### Almacenamiento Local
- **Sin conexión**: No requiere internet
- **Sin telemetría**: No envía datos a servidores
- **Privacidad total**: Todo permanece en tu PC

### Permisos Necesarios
- **Lectura**: Para cargar logos
- **Escritura**: Para guardar QRs y BD
- **Ningún otro permiso requerido**

## ⚡ Rendimiento

### Optimizaciones
- **Generación rápida**: < 1 segundo por QR
- **Base de datos indexada**: Búsquedas instantáneas
- **Imágenes optimizadas**: Compresión PNG eficiente
- **UI responsiva**: No se congela durante operaciones

### Límites Recomendados
- **Historial**: 1000+ QRs sin problemas
- **Tamaño de logo**: Hasta 10MB
- **Longitud de URL**: Hasta 2000 caracteres
- **Notas**: Hasta 1000 caracteres

## 🛠️ Arquitectura del Código

### Separación de Responsabilidades

```
main.py
├── QRGeneratorApp (UI)
│   ├── create_widgets()
│   ├── generate_qr()
│   └── load_history()

qr_generator.py
├── QRGenerator (Lógica de QR)
│   ├── generate_qr()
│   ├── _add_logo()
│   └── generate_qr_with_custom_colors()

database.py
└── QRDatabase (Persistencia)
    ├── add_qr()
    ├── get_all_qrs()
    ├── search_qrs()
    └── delete_qr()
```

### Patrón de Diseño
- **MVC simplificado**: Separación de UI, lógica y datos
- **Single Responsibility**: Cada clase tiene una responsabilidad
- **Dependency Injection**: Componentes desacoplados

## 🎨 Personalización

### Cambiar Colores del QR
Edita `qr_generator.py`:
```python
qr_img = qr.make_image(
    fill_color="blue",      # Color del QR
    back_color="lightyellow" # Color de fondo
)
```

### Cambiar Tema de la UI
Edita `main.py`:
```python
ctk.set_appearance_mode("light")  # "dark" o "light"
ctk.set_default_color_theme("green")  # "blue", "green", "dark-blue"
```

### Cambiar Tamaño del Logo
Edita `qr_generator.py`:
```python
logo_size = min(qr_width, qr_height) // 4  # Cambiar 5 por 4 para logo más grande
```

## 📈 Mejoras Futuras Planificadas

### Versión 2.0
- [ ] Exportar historial a CSV/Excel
- [ ] Importar URLs desde archivo
- [ ] Generación masiva (batch)
- [ ] Plantillas de colores predefinidas
- [ ] Editor de QR (cambiar colores después de generar)

### Versión 3.0
- [ ] Soporte para QR dinámicos
- [ ] Estadísticas avanzadas con gráficos
- [ ] Integración con servicios en la nube
- [ ] API REST para integración
- [ ] Aplicación web complementaria

## 🧪 Testing

### Pruebas Recomendadas
1. **URLs largas**: Probar con URLs de 500+ caracteres
2. **Logos grandes**: Probar con imágenes de 5-10MB
3. **Logos transparentes**: Verificar que se vean bien
4. **Búsqueda**: Probar con caracteres especiales
5. **Eliminación**: Verificar que se elimine archivo y registro

### Casos Extremos
- URL vacía → Debe mostrar alerta
- Logo inexistente → Debe generar sin logo
- BD corrupta → Debe recrear automáticamente
- Carpeta sin permisos → Debe mostrar error claro

---

**Documentación técnica completa para desarrolladores y usuarios avanzados**
