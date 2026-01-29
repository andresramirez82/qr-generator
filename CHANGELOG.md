# Changelog - QR Generator Pro

Todos los cambios notables de este proyecto serán documentados en este archivo.

## [1.1.0] - 2026-01-29

### ✨ Nuevas Características
- **Selector de Tema Dinámico**: Se añadió un menú desplegable en la interfaz para cambiar entre los modos Claro, Oscuro y Sistema.
- **Tema del Sistema por Defecto**: La aplicación ahora detecta y utiliza automáticamente la configuración de apariencia del sistema operativo.
- **Versionado Interno**: Implementación de un sistema de versiones centralizado en la configuración.

### 🎨 Mejoras de Interfaz
- Iconos descriptivos en el selector de tema (🖥️, ☀️, 🌙).
- Título de la ventana dinámico que muestra la versión actual.
- Etiqueta de versión visible en el panel de generación.

---

## [1.0.0] - 2026-01-23

### 🎉 Lanzamiento Inicial

#### ✨ Características Agregadas
- **Generación de QR**: Genera códigos QR a partir de URLs
- **Logo personalizable**: Inserta logos en el centro del QR
- **Base de datos local**: SQLite para almacenar historial
- **Búsqueda**: Filtra QRs por URL o notas
- **Interfaz moderna**: Tema oscuro con CustomTkinter
- **Vista previa**: Muestra el QR generado inmediatamente
- **Historial completo**: Lista todos los QRs generados
- **Estadísticas**: Muestra total de QRs y URLs únicas
- **Acciones rápidas**: Ver, copiar, abrir, eliminar QRs
- **Notas**: Agrega descripciones a cada QR
- **Exportar**: Guarda QRs en ubicación personalizada
- **Abrir carpeta**: Acceso rápido a carpeta de QRs

#### 📄 Archivos Principales
- `main.py` - Interfaz gráfica principal
- `qr_generator.py` - Lógica de generación de QR
- `database.py` - Gestión de base de datos
- `config.py` - Configuración personalizable
- `ejemplos.py` - Scripts de ejemplo

#### 📚 Documentación
- `README.md` - Documentación principal
- `GUIA_USO.md` - Guía detallada de uso
- `CARACTERISTICAS.md` - Documentación técnica
- `INICIO_RAPIDO.md` - Guía de inicio rápido

#### 🛠️ Scripts de Instalación
- `install.bat` - Instalador automático para Windows
- `run.bat` - Ejecutor rápido para Windows
- `requirements.txt` - Dependencias Python

#### 🎨 Características de Diseño
- Tema oscuro profesional
- Paleta de colores azul (#2563eb)
- Interfaz de dos paneles
- Botones con iconos emoji
- Vista previa en tiempo real
- Scrollable history panel

#### 🔧 Características Técnicas
- Corrección de errores alta (30%) para QRs con logo
- Redimensionamiento automático de logos
- Nombres de archivo únicos con timestamp
- Búsqueda en tiempo real
- Validación de URLs
- Manejo de errores robusto

#### 📦 Dependencias
- `qrcode[pil]` - Generación de códigos QR
- `Pillow` - Procesamiento de imágenes
- `customtkinter` - Interfaz gráfica moderna

---

## [Futuro] - Mejoras Planificadas

### Versión 1.2.0
- [ ] Exportar historial a CSV/Excel
- [ ] Importar URLs desde archivo TXT
- [ ] Selector de colores en la UI
- [ ] Plantillas de colores predefinidas
- [ ] Atajos de teclado
- [ ] Drag & drop para logos
- [ ] Copiar QR al portapapeles
- [ ] Imprimir QR directamente
- [ ] Generación masiva (batch) desde CSV
- [ ] Editor de QR (modificar después de generar)
- [ ] Múltiples tamaños de exportación
- [ ] Formatos adicionales (SVG, PDF)
- [ ] Temas personalizables

### Versión 2.0.0
- [ ] QR dinámicos con analytics
- [ ] Estadísticas avanzadas con gráficos
- [ ] Categorías y etiquetas
- [ ] Favoritos
- [ ] Compartir QRs por email
- [ ] Integración con servicios en la nube
- [ ] Sincronización entre dispositivos

### Versión 3.0.0
- [ ] API REST para integración
- [ ] Aplicación web complementaria
- [ ] Aplicación móvil (Android/iOS)
- [ ] Colaboración en equipo
- [ ] Plantillas de diseño avanzadas
- [ ] Animaciones en QRs
- [ ] Realidad aumentada

---

## Formato del Changelog

Este changelog sigue el formato de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

### Tipos de Cambios
- **Agregado** (Added): Para nuevas características
- **Cambiado** (Changed): Para cambios en funcionalidad existente
- **Obsoleto** (Deprecated): Para características que serán removidas
- **Removido** (Removed): Para características removidas
- **Corregido** (Fixed): Para corrección de bugs
- **Seguridad** (Security): Para vulnerabilidades de seguridad

---

## Contribuciones

Si deseas contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## Agradecimientos

- **qrcode** - Por la excelente librería de generación de QR
- **CustomTkinter** - Por la moderna interfaz gráfica
- **Pillow** - Por el procesamiento de imágenes
- **SQLite** - Por la base de datos ligera y eficiente

---

**Última actualización**: 2026-01-29
