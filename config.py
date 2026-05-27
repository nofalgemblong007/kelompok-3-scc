"""
Konfigurasi untuk program ingestion data saham IDX
Kelompok 3 Orang - Tugas Pemrograman Python
"""

# Konfigurasi Database MariaDB (XAMPP)
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'db_idx'
}

# Konfigurasi API IDX
# Menggunakan API idx-data.co.id untuk mengambil data saham harian
API_CONFIG = {
    'base_url': 'https://idx.co.id/api/',
    'endpoint': 'stockSummary',
    'headers': {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
}

# Konfigurasi tabel
TABLE_NAME = 'transaksi_harian'

# Nama anggota kelompok
ANGGOTA_KELOMPOK = [
    'Anggota 1',
    'Anggota 2', 
    'Anggota 3'
]