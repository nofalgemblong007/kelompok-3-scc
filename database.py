"""
Modul untuk koneksi dan setup database MariaDB
Menggunakan mysql-connector-python
"""

import mysql.connector
from mysql.connector import Error
import config


def buat_koneksi():
    """
    Membuat koneksi ke database MariaDB
    
    Returns:
        connection: Objek koneksi MySQL/MariaDB
    """
    try:
        # Pertama koneksi tanpa database untuk membuat jika belum ada
        koneksi_awal = mysql.connector.connect(
            host=config.DB_CONFIG['host'],
            port=config.DB_CONFIG['port'],
            user=config.DB_CONFIG['user'],
            password=config.DB_CONFIG['password']
        )
        
        # Buat database jika belum ada
        cursor = koneksi_awal.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_CONFIG['database']}")
        cursor.close()
        koneksi_awal.close()
        
        # Sekarang koneksi dengan database yang sudah dibuat
        koneksi = mysql.connector.connect(
            host=config.DB_CONFIG['host'],
            port=config.DB_CONFIG['port'],
            user=config.DB_CONFIG['user'],
            password=config.DB_CONFIG['password'],
            database=config.DB_CONFIG['database']
        )
        
        return koneksi
        
    except Error as e:
        print(f"Error saat membuat koneksi: {e}")
        return None


def buat_tabel(koneksi):
    """
    Membuat tabel transaksi_harian jika belum ada
    
    Args:
        koneksi: Objek koneksi database
    """
    try:
        cursor = koneksi.cursor()
        
        # Query untuk membuat tabel
        query_tabel = f"""
        CREATE TABLE IF NOT EXISTS {config.TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tanggal DATE,
            kode VARCHAR(10),
            prev_price DOUBLE,
            open_price DOUBLE,
            close_price DOUBLE,
            high_price DOUBLE,
            low_price DOUBLE,
            volume BIGINT,
            frekuensi BIGINT
        )
        """
        
        cursor.execute(query_tabel)
        koneksi.commit()
        cursor.close()
        
        print("Tabel berhasil dibuat/dicek")
        
    except Error as e:
        print(f"Error saat membuat tabel: {e}")


def simpan_data(koneksi, data_saham):
    """
    Menyimpan data saham ke tabel transaksi_harian
    
    Args:
        koneksi: Objek koneksi database
        data_saham: List berisi dictionary data saham
    
    Returns:
        int: Jumlah data yang berhasil disimpan
    """
    try:
        cursor = koneksi.cursor()
        
        # Query insert data
        query_insert = f"""
        INSERT INTO {config.TABLE_NAME} 
        (tanggal, kode, prev_price, open_price, close_price, 
         high_price, low_price, volume, frekuensi)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Siapkan data untuk insert
        values = []
        for data in data_saham:
            values.append((
                data['tanggal'],
                data['kode'],
                data['prev_price'],
                data['open_price'],
                data['close_price'],
                data['high_price'],
                data['low_price'],
                data['volume'],
                data['frekuensi']
            ))
        
        # Insert semua data
        cursor.executemany(query_insert, values)
        koneksi.commit()
        
        jumlah = cursor.rowcount
        cursor.close()
        
        return jumlah
        
    except Error as e:
        print(f"Error saat menyimpan data: {e}")
        return 0


def cek_data_terakhir(koneksi):
    """
    Melihat data terakhir yang tersimpan
    
    Args:
        koneksi: Objek koneksi database
    """
    try:
        cursor = koneksi.cursor(dictionary=True)
        
        query = f"SELECT * FROM {config.TABLE_NAME} ORDER BY id DESC LIMIT 5"
        cursor.execute(query)
        
        hasil = cursor.fetchall()
        cursor.close()
        
        return hasil
        
    except Error as e:
        print(f"Error saat mengambil data: {e}")
        return []


def tutup_koneksi(koneksi):
    """
    Menutup koneksi database
    
    Args:
        koneksi: Objek koneksi database
    """
    if koneksi and koneksi.is_connected():
        koneksi.close()
        print("Koneksi database ditutup")