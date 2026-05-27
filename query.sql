-- Query SQL untuk Project Ingestion Data Saham IDX
-- Kelompok 3 Orang - Tugas Pemrograman Python
-- Database: MariaDB (XAMPP)

-- ============================================
-- BUAT DATABASE
-- ============================================

CREATE DATABASE IF NOT EXISTS db_idx;

USE db_idx;

-- ============================================
-- BUAT TABEL
-- ============================================

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

-- ============================================
-- QUERY MELIHAT DATA
-- ============================================

-- Lihat semua data
SELECT * FROM transaksi_harian;

-- Lihat 10 data terakhir
SELECT * FROM transaksi_harian ORDER BY id DESC LIMIT 10;

-- Lihat data berdasarkan tanggal
SELECT * FROM transaksi_harian WHERE tanggal = '2026-05-27';

-- Lihat data berdasarkan kode saham
SELECT * FROM transaksi_harian WHERE kode = 'AADI';

-- Lihat total data
SELECT COUNT(*) AS total_data FROM transaksi_harian;

-- Lihat data dengan volume tertinggi
SELECT * FROM transaksi_harian ORDER BY volume DESC LIMIT 10;

-- Lihat statistik harian
SELECT 
    tanggal,
    COUNT(*) AS jumlah_saham,
    SUM(volume) AS total_volume,
    SUM(frekuensi) AS total_frekuensi,
    AVG(close_price) AS rata_harga_tutup
FROM transaksi_harian
GROUP BY tanggal;

-- ============================================
-- QUERY HAPUS DATA
-- ============================================

-- Hapus semua data
DELETE FROM transaksi_harian;

-- Hapus data berdasarkan tanggal
DELETE FROM transaksi_harian WHERE tanggal = '2026-05-27';

-- Hapus data berdasarkan kode
DELETE FROM transaksi_harian WHERE kode = 'AADI';

-- Reset auto increment
ALTER TABLE transaksi_harian AUTO_INCREMENT = 1;

-- ============================================
-- QUERY UPDATE DATA
-- ============================================

-- Update harga close
UPDATE transaksi_harian 
SET close_price = 165.0 
WHERE kode = 'AADI' AND tanggal = '2026-05-27';

-- ============================================
-- CONTOH DATA SAHAM
-- ============================================

INSERT INTO transaksi_harian 
(tanggal, kode, prev_price, open_price, close_price, high_price, low_price, volume, frekuensi)
VALUES 
('2026-05-27', 'AADI', 150, 155, 160, 165, 150, 1000000, 500),
('2026-05-27', 'AALI', 2500, 2550, 2600, 2650, 2500, 500000, 300),
('2026-05-27', 'ACES', 980, 990, 1000, 1010, 980, 800000, 400),
('2026-05-27', 'ADHI', 850, 860, 870, 880, 850, 600000, 350),
('2026-05-27', 'ADRO', 2800, 2850, 2900, 2950, 2800, 1200000, 600),
('2026-05-27', 'AGRO', 350, 355, 360, 365, 350, 400000, 250),
('2026-05-27', 'AIMS', 210, 215, 220, 225, 210, 300000, 200),
('2026-05-27', 'AKPI', 450, 455, 460, 465, 450, 350000, 220),
('2026-05-27', 'ANTM', 1800, 1820, 1850, 1870, 1800, 900000, 450),
('2026-05-27', 'APEX', 520, 525, 530, 535, 520, 250000, 180);