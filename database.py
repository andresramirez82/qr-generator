import sqlite3
from datetime import datetime
import os

class QRDatabase:
    """Gestiona la base de datos SQLite para almacenar el historial de QR generados"""
    
    def __init__(self, db_path="qr_history.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Inicializa la base de datos y crea las tablas necesarias"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS qr_codes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                logo_path TEXT,
                image_path TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_qr(self, url, image_path, logo_path=None, notes=""):
        """Agrega un nuevo registro de QR generado"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO qr_codes (url, logo_path, image_path, notes)
            VALUES (?, ?, ?, ?)
        ''', (url, logo_path, image_path, notes))
        
        qr_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return qr_id
    
    def get_all_qrs(self, limit=100):
        """Obtiene todos los QR generados, ordenados por fecha (más recientes primero)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, url, logo_path, image_path, created_at, notes
            FROM qr_codes
            ORDER BY created_at DESC
            LIMIT ?
        ''', (limit,))
        
        results = cursor.fetchall()
        conn.close()
        
        return results
    
    def search_qrs(self, search_term):
        """Busca QRs por URL o notas"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, url, logo_path, image_path, created_at, notes
            FROM qr_codes
            WHERE url LIKE ? OR notes LIKE ?
            ORDER BY created_at DESC
        ''', (f'%{search_term}%', f'%{search_term}%'))
        
        results = cursor.fetchall()
        conn.close()
        
        return results
    
    def delete_qr(self, qr_id):
        """Elimina un QR del historial"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Primero obtener la ruta de la imagen para eliminarla
        cursor.execute('SELECT image_path FROM qr_codes WHERE id = ?', (qr_id,))
        result = cursor.fetchone()
        
        if result:
            image_path = result[0]
            if os.path.exists(image_path):
                os.remove(image_path)
        
        cursor.execute('DELETE FROM qr_codes WHERE id = ?', (qr_id,))
        conn.commit()
        conn.close()
    
    def get_stats(self):
        """Obtiene estadísticas de uso"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM qr_codes')
        total = cursor.fetchone()[0]
        
        cursor.execute('''
            SELECT COUNT(DISTINCT url) FROM qr_codes
        ''')
        unique_urls = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total': total,
            'unique_urls': unique_urls
        }
