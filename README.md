# Project Ingestion Data Saham IDX

**Kelompok 3 Orang - Tugas Pemrograman Python**

---

## Deskripsi Project

Project ini dibuat untuk mengambil data saham harian dari API Bursa Efek Indonesia (IDX) dan menyimpannya ke database MariaDB menggunakan XAMPP.

---

## Struktur Project

```
project_ingestion_idx/
│
├── main.py           # Program utama
├── database.py       # Modul koneksi dan operasi database
├── ingestion.py     # Modul pengambilan data dari API
├── config.py       # Konfigurasi database dan API
├── requirements.txt # Library yang diperlukan
└── README.md      # Dokumentasi project
```

---

## Anggota Kelompok

1. Anggota 1
2. Anggota 2
3. Anggota 3

---

## Persiapan

### 1. Install XAMPP

- Download XAMPP dari https://www.apachefriends.org/
- Install XAMPP di komputer
- Start Apache dan MySQL dari XAMPP Control Panel

### 2. Install Python

- Pastikan Python 3.8 atau lebih baru terinstall
- Cek versi Python: `python --version`

### 3. Install Library

```bash
pip install -r requirements.txt
```

Atau install satu per satu:

```bash
pip install requests
pip install mysql-connector-python
pip install pandas
```

---

## Konfigurasi Database

Edit file `config.py` untuk menyesuaikan konfigurasi database:

```python
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',  # Kosong jika default XAMPP
    'database': 'db_idx'
}
```

---

## Menjalankan Program

```bash
python main.py
```

---

## Contoh Output Terminal

```
========================================
 SISTEM INGESTION DATA SAHAM IDX
========================================

Menghubungi API IDX...
API berhasil diakses

Mengambil data saham...
Total data diterima : 999 data

Membuat koneksi MariaDB...
Koneksi database berhasil

Membuat tabel transaksi_harian...
Tabel berhasil dibuat/dicek

Menyimpan data ke tabel transaksi_harian...
Data berhasil disimpan: 999 record

Data terakhir yang tersimpan:
--------------------------------------------------------------------------------
Tanggal     Kode     Prev      Open      Close     High      Low       Volume     Freq   
--------------------------------------------------------------------------------
2026-05-27 AADI     150.0     155.0     160.0     165.0     150.0     1000000    500   
2026-05-27 AALI     2500.0    2550.0    2600.0    2650.0    2500.0    500000    300   
2026-05-27 ACES     980.0     990.0     1000.0    1010.0    980.0     800000    400   
2026-05-27 ADHI     850.0     860.0     870.0     880.0    850.0     600000    350   
2026-05-27 ADRO     2800.0    2850.0    2900.0    2950.0    2800.0    1200000   600   
--------------------------------------------------------------------------------

Koneksi database ditutup

========================================
 INGESTION DATA SELESAI
========================================
```

---

## Struktur Database

### Nama Database: `db_idx`

### Nama Tabel: `transaksi_harian`

| Kolom       | Tipe     | Keterangan          |
|------------|----------|--------------------|
| id         | INT      | Primary key         |
| tanggal    | DATE     | Tanggal transaksi  |
| kode       | VARCHAR  | Kode saham         |
| prev_price | DOUBLE   | Harga sebelumnya   |
| open_price | DOUBLE   | Harga buka         |
| close_price| DOUBLE   | Harga tutup        |
| high_price | DOUBLE   | Harga tertinggi    |
| low_price  | DOUBLE   | Harga terendah      |
| volume    | BIGINT   | Volume transaksi   |
| frekuensi  | BIGINT   | Frekuensi transaksi|

### Query SQL

```sql
CREATE DATABASE IF NOT EXISTS db_idx;

USE db_idx;

CREATE TABLE IF NOT EXISTS transaksi_harian (
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
);
```

---

## Melihat Data di phpMyAdmin

1. Buka browser
2. Akses http://localhost/phpmyadmin/
3. Pilih database `db_idx`
4. Klik tabel `transaksi_harian`
5. Klik tab "Browse" untuk melihat data

---

## Penjelasan Tiap File

### config.py
Berisi konfigurasi database MariaDB dan API IDX.

### database.py
Modul untuk:
- Membuat koneksi ke MariaDB
- Membuat database dan tabel otomatis
- Menyimpan data ke tabel
- Mengambil data dari tabel

### ingestion.py
Modul untuk:
- Mengambil data dari API IDX
- Memproses dan membersihkan data
- Konversi tipe data
- Generate data contoh untuk testing

### main.py
Program utama yang menjalankan alur kerja:
1. Ambil data dari API
2. Koneksi ke MariaDB
3. Simpan data ke tabel
4. Tampilkan hasil

---

## Flowchart Sistem

```
┌─────────────────┐
│   START         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Konfigurasi DB   │
│ & API           │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Request ke API  │
│ IDX             │
└────────┬────────┘
         │
    ┌────┴────┐
    │ Berhasil?│
    └────┬────┘
    Ya   │   Tidak
    ┌────┴────┐    ┌─────────────────┐
    ▼        │    │ Generate Data   │
┌────────┐   │    │ Contoh          │
│ Proses │   └───►└────────┬────────┘
│ Data   │                │
└────────┬────────┘         │
         │                │
         ▼                │
┌─────────────────┐      │
│ Koneksi MariaDB  │◄─────┘
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Buat Tabel      │
│ (jika belum ada)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Insert Data ke  │
│ Tabel           │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Tampilkan Hasil│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    END          │
└─────────────────┘
```

---

## Kode Saham Contoh

Berikut beberapa kode saham IDX yang digunakan dalam project:

| Kode | Nama Emiten         |
|------|-------------------|
| AADI | AADI International|
| AALI | Astra Agro Lestari |
| ACES | Ace Hardware     |
| ADHI | Adhi Karya      |
| ADRO | Adaro Energy    |
| AGRO | Bank Agri       |
| AIMS | Akbar Indo     |
| AKPI | Argha Karya    |
| ANTM | Aneka Tambang  |
| APEX | Apexindo      |

Dan 90+ kode saham lainnya...

---

## Catatan

- Jika API IDX tidak dapat diakses, program akan otomatis menggunakan data contoh
- Pastikan MySQL di XAMPP sudah running sebelum menjalankan program
- Database dan tabel akan dibuat secara otomatis jika belum ada

---

## Referensi

- Dokumentasi API IDX: https://idx.co.id/
- MySQL Connector Python: https://dev.mysql.com/doc/connector-python/en/
- XAMPP: https://www.apachefriends.org/

---

**Project dibuat untuk tugas kelompok Pemrograman Python**