import qrcode
from PIL import Image, ImageDraw
import os
from datetime import datetime

class QRGenerator:
    """Genera códigos QR con opciones de personalización"""
    
    def __init__(self, output_dir="qr_images"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_qr(self, url, logo_path=None, size=10, border=2):
        """
        Genera un código QR para la URL proporcionada
        
        Args:
            url: URL a codificar en el QR
            logo_path: Ruta opcional al logo a insertar en el centro del QR
            size: Tamaño del QR (1-40, donde mayor es más grande)
            border: Grosor del borde (mínimo 4)
        
        Returns:
            Ruta al archivo de imagen generado
        """
        # Crear el código QR
        qr = qrcode.QRCode(
            version=None,  # Auto-ajustar el tamaño
            error_correction=qrcode.constants.ERROR_CORRECT_H if logo_path else qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=border,
        )
        
        qr.add_data(url)
        qr.make(fit=True)
        
        # Crear la imagen del QR
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        # Si hay un logo, insertarlo en el centro
        if logo_path and os.path.exists(logo_path):
            qr_img = self._add_logo(qr_img, logo_path)
        
        # Generar nombre de archivo único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        
        # Guardar la imagen
        qr_img.save(filepath)
        
        return filepath
    
    def _add_logo(self, qr_img, logo_path):
        """Agrega un logo en el centro del código QR"""
        try:
            # Abrir el logo
            logo = Image.open(logo_path)
            
            # Calcular el tamaño del logo (aproximadamente 1/5 del QR)
            qr_width, qr_height = qr_img.size
            logo_size = min(qr_width, qr_height) // 5
            
            # Redimensionar el logo manteniendo la proporción
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Crear un fondo blanco para el logo (para mejor contraste)
            logo_bg_size = int(logo_size * 1.2)
            logo_bg = Image.new('RGB', (logo_bg_size, logo_bg_size), 'white')
            
            # Calcular posición para centrar el logo en el fondo
            logo_pos = ((logo_bg_size - logo.size[0]) // 2, (logo_bg_size - logo.size[1]) // 2)
            
            # Pegar el logo en el fondo blanco
            if logo.mode == 'RGBA':
                logo_bg.paste(logo, logo_pos, logo)
            else:
                logo_bg.paste(logo, logo_pos)
            
            # Calcular posición para centrar en el QR
            qr_pos = ((qr_width - logo_bg_size) // 2, (qr_height - logo_bg_size) // 2)
            
            # Pegar el logo con fondo en el QR
            qr_img.paste(logo_bg, qr_pos)
            
        except Exception as e:
            print(f"Error al agregar logo: {e}")
        
        return qr_img
    
    def generate_qr_with_custom_colors(self, url, fill_color="black", back_color="white", logo_path=None):
        """Genera un QR con colores personalizados"""
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H if logo_path else qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        
        qr.add_data(url)
        qr.make(fit=True)
        
        qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
        
        if logo_path and os.path.exists(logo_path):
            qr_img = self._add_logo(qr_img, logo_path)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        
        qr_img.save(filepath)
        
        return filepath
