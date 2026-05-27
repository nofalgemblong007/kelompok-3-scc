"""
Program Utama - Ingestion Data Saham IDX
Kelompok 3 Orang - Tugas Pemrograman Python

Program ini untuk mengambil data saham dari API IDX
dan menyimpannya ke database MariaDB (XAMPP)
"""

import sys
import database
import ingestion
import config


def tampilkan_header():
    """Menampilkan header program"""
    print("=" * 40)
    print(" SISTEM INGESTION DATA SAHAM IDX")
    print("=" * 40)
    print()


def jalankan_ingestion():
    """
    Menjalankan proses ingestion data saham
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Langkah 1: Ambil data dari API
    print("Mengambil data saham...")
    data_saham = ingestion.ambil_data_saham(use_api=True)
    
    if not data_saham:
        print("Gagal mengambil data dari API!")
        return False
    
    total_data = len(data_saham)
    print(f"Total data diterima : {total_data} data")
    print()
    
    # Langkah 2: Buat koneksi ke MariaDB
    print("Membuat koneksi MariaDB...")
    koneksi = database.buat_koneksi()
    
    if not koneksi:
        print("Gagal membuat koneksi database!")
        return False
    
    print("Koneksi database berhasil")
    print()
    
    # Langkah 3: Buat tabel jika belum ada
    print("Membuat tabel transaksi_harian...")
    database.buat_tabel(koneksi)
    print()
    
    # Langkah 4: Simpan data ke database
    print("Menyimpan data ke tabel transaksi_harian...")
    jumlah_simpan = database.simpan_data(koneksi, data_saham)
    
    if jumlah_simpan > 0:
        print(f"Data berhasil disimpan: {jumlah_simpan} record")
    else:
        print("Tidak ada data yang disimpan")
    print()
    
    # Langkah 5: Tampilkan data terakhir
    print("Data terakhir yang tersimpan:")
    print("-" * 80)
    data_terakhir = database.cek_data_terakhir(koneksi)
    
    if data_terakhir:
        print(f"{'Tanggal':<12} {'Kode':<8} {'Prev':<10} {'Open':<10} {'Close':<10} {'High':<10} {'Low':<10} {'Volume':<12} {'Freq':<8}")
        print("-" * 80)
        for row in data_terakhir:
            print(f"{row['tanggal']:<12} {row['kode']:<8} {row['prev_price']:<10.0f} {row['open_price']:<10.0f} {row['close_price']:<10.0f} {row['high_price']:<10.0f} {row['low_price']:<10.0f} {row['volume']:<12} {row['frekuensi']:<8}")
    print("-" * 80)
    print()
    
    # Langkah 6: Tutup koneksi
    database.tutup_koneksi(koneksi)
    
    return True


def main():
    """Fungsi utama program"""
    try:
        # Tampilkan header
        tampilkan_header()
        
        # Jalankan proses ingestion
        berhasil = jalankan_ingestion()
        
        if berhasil:
            print("=" * 40)
            print(" INGESTION DATA SELESAI")
            print("=" * 40)
            return 0
        else:
            print("=" * 40)
            print(" INGESTION DATA GAGAL")
            print("=" * 40)
            return 1
            
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user")
        return 1
    except Exception as e:
        print(f"\nError: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())