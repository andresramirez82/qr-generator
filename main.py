import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from qr_generator import QRGenerator
from database import QRDatabase
import webbrowser

class QRGeneratorApp:
    """Aplicación principal de generación de códigos QR con diseño responsive"""
    
    def __init__(self):
        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("QR Generator Pro")
        self.root.geometry("1000x700")
        self.root.minsize(350, 500)  # Tamaño mínimo para pantallas pequeñas
        
        # Inicializar componentes
        self.qr_gen = QRGenerator()
        self.db = QRDatabase()
        self.current_logo_path = None
        self.current_qr_image = None
        
        # Variables para responsive
        self.is_small_screen = False
        self.current_tab = 0  # 0 = Generador, 1 = Historial
        
        # Crear interfaz
        self.create_widgets()
        
        # Cargar historial inicial
        self.load_history()
        
        # Bind para detectar cambios de tamaño
        self.root.bind("<Configure>", self.on_window_resize)
    
    def on_window_resize(self, event=None):
        """Detecta cambios de tamaño y ajusta el layout"""
        if event and event.widget == self.root:
            width = self.root.winfo_width()
            
            # Determinar si es pantalla pequeña (menos de 700px)
            new_is_small = width < 700
            
            if new_is_small != self.is_small_screen:
                self.is_small_screen = new_is_small
                self.adjust_layout()
    
    def adjust_layout(self):
        """Ajusta el layout según el tamaño de pantalla"""
        if self.is_small_screen:
            # Layout de 1 columna con pestañas
            self.left_frame.grid_forget()
            self.right_frame.grid_forget()
            
            # Crear tabview si no existe
            if not hasattr(self, 'tabview'):
                self.tabview = ctk.CTkTabview(self.main_frame)
                self.tabview.pack(fill="both", expand=True)
                
                # Crear pestañas
                self.tab_generator = self.tabview.add("🔲 Generar")
                self.tab_history = self.tabview.add("📚 Historial")
                
                # Mover frames a las pestañas
                self.left_frame.pack_forget()
                self.right_frame.pack_forget()
            
            # Reempaquetar en pestañas
            self.left_frame.pack(in_=self.tab_generator, fill="both", expand=True)
            self.right_frame.pack(in_=self.tab_history, fill="both", expand=True)
            self.tabview.pack(fill="both", expand=True)
            
        else:
            # Layout de 2 columnas
            if hasattr(self, 'tabview'):
                self.tabview.pack_forget()
            
            self.left_frame.pack_forget()
            self.right_frame.pack_forget()
            
            self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
            self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
    
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Columna izquierda - Generación de QR
        self.left_frame = ctk.CTkFrame(self.main_frame)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        # Columna derecha - Historial
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        
        # Configurar grid
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Crear widgets de la columna izquierda
        self.create_generator_widgets()
        
        # Crear widgets de la columna derecha
        self.create_history_widgets()
    
    def get_responsive_font_size(self, base_size):
        """Calcula tamaño de fuente responsive"""
        if self.is_small_screen:
            return max(10, int(base_size * 0.85))
        return base_size
    
    def get_responsive_padding(self, base_padding):
        """Calcula padding responsive"""
        if self.is_small_screen:
            return max(5, int(base_padding * 0.6))
        return base_padding
    
    def create_generator_widgets(self):
        """Crea los widgets para generar QR"""
        
        # Scrollable frame para contenido
        scroll_frame = ctk.CTkScrollableFrame(self.left_frame)
        scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Título
        title = ctk.CTkLabel(
            scroll_frame,
            text="🔲 Generar Código QR",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=(15, 10))
        
        # Frame para URL
        url_frame = ctk.CTkFrame(scroll_frame)
        url_frame.pack(fill="x", padx=15, pady=8)
        
        url_label = ctk.CTkLabel(url_frame, text="URL:", font=ctk.CTkFont(size=13))
        url_label.pack(anchor="w", padx=10, pady=(8, 3))
        
        self.url_entry = ctk.CTkEntry(
            url_frame,
            placeholder_text="https://ejemplo.com",
            height=38,
            font=ctk.CTkFont(size=12)
        )
        self.url_entry.pack(fill="x", padx=10, pady=(0, 8))
        
        # Frame para logo
        logo_frame = ctk.CTkFrame(scroll_frame)
        logo_frame.pack(fill="x", padx=15, pady=8)
        
        logo_label = ctk.CTkLabel(logo_frame, text="Logo (opcional):", font=ctk.CTkFont(size=13))
        logo_label.pack(anchor="w", padx=10, pady=(8, 3))
        
        logo_btn_frame = ctk.CTkFrame(logo_frame, fg_color="transparent")
        logo_btn_frame.pack(fill="x", padx=10, pady=(0, 8))
        
        self.logo_btn = ctk.CTkButton(
            logo_btn_frame,
            text="📁 Logo",
            command=self.select_logo,
            height=32
        )
        self.logo_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        self.clear_logo_btn = ctk.CTkButton(
            logo_btn_frame,
            text="✖",
            command=self.clear_logo,
            width=35,
            height=32,
            fg_color="red",
            hover_color="darkred"
        )
        self.clear_logo_btn.pack(side="left")
        
        self.logo_path_label = ctk.CTkLabel(
            logo_frame,
            text="Sin logo",
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        self.logo_path_label.pack(padx=10, pady=(0, 8))
        
        # Frame para notas
        notes_frame = ctk.CTkFrame(scroll_frame)
        notes_frame.pack(fill="x", padx=15, pady=8)
        
        notes_label = ctk.CTkLabel(notes_frame, text="Notas (opcional):", font=ctk.CTkFont(size=13))
        notes_label.pack(anchor="w", padx=10, pady=(8, 3))
        
        self.notes_entry = ctk.CTkTextbox(
            notes_frame,
            height=50,
            font=ctk.CTkFont(size=11)
        )
        self.notes_entry.pack(fill="x", padx=10, pady=(0, 8))
        
        # Botón generar
        self.generate_btn = ctk.CTkButton(
            scroll_frame,
            text="✨ Generar QR",
            command=self.generate_qr,
            height=45,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )
        self.generate_btn.pack(fill="x", padx=15, pady=15)
        
        # Frame para preview del QR
        preview_frame = ctk.CTkFrame(scroll_frame)
        preview_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        preview_label = ctk.CTkLabel(
            preview_frame,
            text="Vista Previa",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        preview_label.pack(pady=(8, 3))
        
        self.preview_label = ctk.CTkLabel(
            preview_frame,
            text="El QR generado aparecerá aquí",
            text_color="gray",
            font=ctk.CTkFont(size=11)
        )
        self.preview_label.pack(pady=15)
        
        # Botones de acción para el QR generado
        self.action_frame = ctk.CTkFrame(preview_frame, fg_color="transparent")
        
        self.save_btn = ctk.CTkButton(
            self.action_frame,
            text="💾 Guardar",
            command=self.save_qr_as,
            state="disabled",
            height=32
        )
        self.save_btn.pack(side="left", expand=True, fill="x", padx=3)
        
        self.open_folder_btn = ctk.CTkButton(
            self.action_frame,
            text="📂 Carpeta",
            command=self.open_qr_folder,
            state="disabled",
            height=32
        )
        self.open_folder_btn.pack(side="left", expand=True, fill="x", padx=3)
    
    def create_history_widgets(self):
        """Crea los widgets para el historial"""
        
        # Título y estadísticas
        header_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=15, pady=(15, 8))
        
        title = ctk.CTkLabel(
            header_frame,
            text="📚 Historial",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(side="left")
        
        # Estadísticas
        stats = self.db.get_stats()
        self.stats_label = ctk.CTkLabel(
            header_frame,
            text=f"{stats['total']} | {stats['unique_urls']} únicas",
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        self.stats_label.pack(side="right")
        
        # Búsqueda
        search_frame = ctk.CTkFrame(self.right_frame)
        search_frame.pack(fill="x", padx=15, pady=(0, 8))
        
        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="🔍 Buscar...",
            height=32
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(8, 3), pady=8)
        self.search_entry.bind("<KeyRelease>", lambda e: self.search_history())
        
        search_clear_btn = ctk.CTkButton(
            search_frame,
            text="✖",
            command=self.clear_search,
            width=32,
            height=32
        )
        search_clear_btn.pack(side="left", padx=(0, 8), pady=8)
        
        # Lista de historial con scrollbar
        self.history_frame = ctk.CTkScrollableFrame(self.right_frame)
        self.history_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
    
    def select_logo(self):
        """Abre un diálogo para seleccionar un logo"""
        filepath = filedialog.askopenfilename(
            title="Seleccionar Logo",
            filetypes=[
                ("Imágenes", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if filepath:
            self.current_logo_path = filepath
            filename = os.path.basename(filepath)
            self.logo_path_label.configure(
                text=f"✓ {filename}",
                text_color="green"
            )
    
    def clear_logo(self):
        """Limpia el logo seleccionado"""
        self.current_logo_path = None
        self.logo_path_label.configure(
            text="Sin logo seleccionado",
            text_color="gray"
        )
    
    def generate_qr(self):
        """Genera el código QR"""
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL")
            return
        
        try:
            # Generar QR
            image_path = self.qr_gen.generate_qr(url, self.current_logo_path)
            self.current_qr_image = image_path
            
            # Obtener notas
            notes = self.notes_entry.get("1.0", "end-1c").strip()
            
            # Guardar en base de datos
            self.db.add_qr(url, image_path, self.current_logo_path, notes)
            
            # Mostrar preview
            self.show_qr_preview(image_path)
            
            # Habilitar botones de acción
            self.save_btn.configure(state="normal")
            self.open_folder_btn.configure(state="normal")
            
            # Actualizar historial
            self.load_history()
            
            messagebox.showinfo("Éxito", "¡Código QR generado correctamente!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar QR: {str(e)}")
    
    def show_qr_preview(self, image_path):
        """Muestra el preview del QR generado"""
        try:
            # Cargar imagen
            img = Image.open(image_path)
            
            # Redimensionar para preview (máximo 300x300)
            img.thumbnail((300, 300), Image.Resampling.LANCZOS)
            
            # Convertir a PhotoImage
            photo = ImageTk.PhotoImage(img)
            
            # Actualizar label
            self.preview_label.configure(image=photo, text="")
            self.preview_label.image = photo  # Mantener referencia
            
            # Mostrar botones de acción
            self.action_frame.pack(fill="x", pady=(10, 10), padx=10)
            
        except Exception as e:
            print(f"Error al mostrar preview: {e}")
    
    def save_qr_as(self):
        """Guarda el QR en una ubicación personalizada"""
        if not self.current_qr_image:
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("Todos los archivos", "*.*")]
        )
        
        if filepath:
            try:
                img = Image.open(self.current_qr_image)
                img.save(filepath)
                messagebox.showinfo("Éxito", f"QR guardado en:\n{filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def open_qr_folder(self):
        """Abre la carpeta donde se guardan los QR"""
        import platform
        import subprocess
        
        folder_path = os.path.abspath(self.qr_gen.output_dir)
        if os.path.exists(folder_path):
            system = platform.system()
            try:
                if system == "Windows":
                    os.startfile(folder_path)
                elif system == "Darwin":  # macOS
                    subprocess.run(["open", folder_path])
                else:  # Linux y otros
                    subprocess.run(["xdg-open", folder_path])
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir la carpeta: {str(e)}")
    
    def load_history(self):
        """Carga el historial de QR generados"""
        # Limpiar historial actual
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        
        # Obtener registros
        records = self.db.get_all_qrs()
        
        if not records:
            no_data_label = ctk.CTkLabel(
                self.history_frame,
                text="No hay QR generados aún",
                text_color="gray",
                font=ctk.CTkFont(size=11)
            )
            no_data_label.pack(pady=20)
            return
        
        # Crear tarjetas para cada registro
        for record in records:
            self.create_history_card(record)
        
        # Actualizar estadísticas
        stats = self.db.get_stats()
        self.stats_label.configure(
            text=f"{stats['total']} | {stats['unique_urls']} únicas"
        )
    
    def create_history_card(self, record):
        """Crea una tarjeta para un registro del historial"""
        qr_id, url, logo_path, image_path, created_at, notes = record
        
        # Frame de la tarjeta
        card = ctk.CTkFrame(self.history_frame)
        card.pack(fill="x", pady=4)
        
        # Frame superior con info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(fill="x", padx=8, pady=8)
        
        # URL - más corta en pantallas pequeñas
        max_url_len = 35 if self.is_small_screen else 50
        url_label = ctk.CTkLabel(
            info_frame,
            text=url if len(url) <= max_url_len else url[:max_url_len-3] + "...",
            font=ctk.CTkFont(size=11, weight="bold"),
            anchor="w"
        )
        url_label.pack(anchor="w")
        
        # Fecha y logo en la misma línea si es pantalla pequeña
        meta_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        meta_frame.pack(fill="x", anchor="w")
        
        # Fecha
        date_label = ctk.CTkLabel(
            meta_frame,
            text=f"📅 {created_at}",
            font=ctk.CTkFont(size=9),
            text_color="gray",
            anchor="w"
        )
        date_label.pack(side="left", padx=(0, 8))
        
        # Logo indicator
        if logo_path:
            logo_indicator = ctk.CTkLabel(
                meta_frame,
                text="🖼️",
                font=ctk.CTkFont(size=9),
                text_color="green",
                anchor="w"
            )
            logo_indicator.pack(side="left")
        
        # Notas
        if notes:
            max_notes_len = 30 if self.is_small_screen else 50
            notes_label = ctk.CTkLabel(
                info_frame,
                text=f"📝 {notes[:max_notes_len]}..." if len(notes) > max_notes_len else f"📝 {notes}",
                font=ctk.CTkFont(size=9),
                text_color="lightblue",
                anchor="w"
            )
            notes_label.pack(anchor="w")
        
        # Botones de acción - más compactos
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(fill="x", padx=8, pady=(0, 8))
        
        btn_size = 32 if self.is_small_screen else 35
        
        view_btn = ctk.CTkButton(
            btn_frame,
            text="👁️",
            command=lambda: self.view_qr(image_path),
            width=btn_size,
            height=28
        )
        view_btn.pack(side="left", padx=2)
        
        copy_btn = ctk.CTkButton(
            btn_frame,
            text="📋",
            command=lambda: self.copy_url(url),
            width=btn_size,
            height=28
        )
        copy_btn.pack(side="left", padx=2)
        
        open_btn = ctk.CTkButton(
            btn_frame,
            text="🌐",
            command=lambda: webbrowser.open(url),
            width=btn_size,
            height=28
        )
        open_btn.pack(side="left", padx=2)
        
        delete_btn = ctk.CTkButton(
            btn_frame,
            text="🗑️",
            command=lambda: self.delete_qr(qr_id),
            width=btn_size,
            height=28,
            fg_color="red",
            hover_color="darkred"
        )
        delete_btn.pack(side="right", padx=2)
    
    def view_qr(self, image_path):
        """Muestra el QR en una ventana nueva"""
        if not os.path.exists(image_path):
            messagebox.showerror("Error", "La imagen no existe")
            return
        
        # Crear ventana nueva
        viewer = ctk.CTkToplevel(self.root)
        viewer.title("Visualizar QR")
        viewer.geometry("500x500")
        
        # Configurar para que siempre esté al frente
        viewer.transient(self.root)  # Asociar con la ventana principal
        viewer.lift()  # Traer al frente
        viewer.focus_force()  # Forzar el foco
        viewer.grab_set()  # Hacer modal (bloquea interacción con ventana principal)
        
        # Centrar la ventana en la pantalla
        viewer.update_idletasks()
        width = viewer.winfo_width()
        height = viewer.winfo_height()
        x = (viewer.winfo_screenwidth() // 2) - (width // 2)
        y = (viewer.winfo_screenheight() // 2) - (height // 2)
        viewer.geometry(f'{width}x{height}+{x}+{y}')
        
        # Cargar y mostrar imagen
        img = Image.open(image_path)
        img.thumbnail((450, 450), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        label = ctk.CTkLabel(viewer, image=photo, text="")
        label.image = photo
        label.pack(expand=True, pady=20)
        
        # Botón para cerrar
        close_btn = ctk.CTkButton(
            viewer,
            text="Cerrar",
            command=viewer.destroy,
            width=120,
            height=35
        )
        close_btn.pack(pady=(0, 20))
    
    def copy_url(self, url):
        """Copia la URL al portapapeles"""
        self.root.clipboard_clear()
        self.root.clipboard_append(url)
        messagebox.showinfo("Copiado", "URL copiada al portapapeles")
    
    def delete_qr(self, qr_id):
        """Elimina un QR del historial"""
        if messagebox.askyesno("Confirmar", "¿Eliminar este QR del historial?"):
            self.db.delete_qr(qr_id)
            self.load_history()
            messagebox.showinfo("Eliminado", "QR eliminado correctamente")
    
    def search_history(self):
        """Busca en el historial"""
        search_term = self.search_entry.get().strip()
        
        # Limpiar historial actual
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        
        if not search_term:
            self.load_history()
            return
        
        # Buscar
        results = self.db.search_qrs(search_term)
        
        if not results:
            no_results = ctk.CTkLabel(
                self.history_frame,
                text="No se encontraron resultados",
                text_color="gray"
            )
            no_results.pack(pady=20)
            return
        
        # Mostrar resultados
        for record in results:
            self.create_history_card(record)
    
    def clear_search(self):
        """Limpia la búsqueda"""
        self.search_entry.delete(0, "end")
        self.load_history()
    
    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()


if __name__ == "__main__":
    app = QRGeneratorApp()
    app.run()
