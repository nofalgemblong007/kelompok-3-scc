"""
Modul untuk mengambil data dari API IDX
Menggunakan library requests dan json
"""

import requests
import json
import config
from datetime import datetime


def ambil_data_dari_api():
    """
    Mengambil data saham harian dari API IDX
    
    Returns:
        list: List dictionary berisi data saham
    """
    try:
        # Konfigurasi URL API
        url = config.API_CONFIG['base_url'] + config.API_CONFIG['endpoint']
        headers = config.API_CONFIG['headers']
        
        # Request ke API
        print(f"Menghubungi API: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        
        # Cek status response
        if response.status_code == 200:
            print("API berhasil diakses")
            data = response.json()
            return data
        else:
            print(f"Gagal mengakses API. Status: {response.status_code}")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Error saat request ke API: {e}")
        return []


def proses_data(data_raw):
    """
    Memproses data dari API menjadi format yang sesuai untuk database
    
    Args:
        data_raw: Data mentah dari API
    
    Returns:
        list: List dictionary data yang sudah diproses
    """
    data_proses = []
    
    try:
        # Parse data dari response
        if isinstance(data_raw, str):
            data_json = json.loads(data_raw)
        else:
            data_json = data_raw
            
        # Ambil data dari key yang sesuai
        # Sesuaikan dengan struktur API IDX yang sebenarnya
        if 'data' in data_json:
            daftar_saham = data_json['data']
        elif 'stock' in data_json:
            daftar_saham = data_json['stock']
        else:
            daftar_saham = data_json
            
        # Ambil tanggal hari ini
        tanggal_hari_ini = datetime.now().strftime('%Y-%m-%d')
        
        # Proses setiap saham
        for item in daftar_saham:
            # Validasi data tidak kosong
            if not item:
                continue
                
            # Ekstrak field yang diperlukan
            # Sesuaikan dengan struktur API IDX
            try:
                data_saham = {
                    'tanggal': tanggal_hari_ini,
                    'kode': item.get('code', item.get('kode', item.get('stock_code', ''))),
                    'prev_price': konversi_angka(item.get('prev_price', item.get('prevPrice', 0))),
                    'open_price': konversi_angka(item.get('open_price', item.get('openPrice', 0))),
                    'close_price': konversi_angka(item.get('close_price', item.get('closePrice', 0))),
                    'high_price': konversi_angka(item.get('high_price', item.get('highPrice', 0))),
                    'low_price': konversi_angka(item.get('low_price', item.get('lowPrice', 0))),
                    'volume': konversi_angka(item.get('volume', 0)),
                    'frekuensi': konversi_angka(item.get('frequency', item.get('frekuensi', 0)))
                }
                
                # Validasi kode tidak kosong
                if data_saham['kode']:
                    data_proses.append(data_saham)
                    
            except Exception as e:
                print(f"Error memproses item: {e}")
                continue
                
    except Exception as e:
        print(f"Error saat memproses data: {e}")
        
    return data_proses


def konversi_angka(nilai):
    """
    Mengkonversi nilai string ke angka numerik
    
    Args:
        nilai: Nilai dalam bentuk string atau angka
    
    Returns:
        float: Nilai dalam bentuk numerik
    """
    try:
        # Jika sudah numerik, langsung return
        if isinstance(nilai, (int, float)):
            return float(nilai)
            
        # Jika string, bersihkan dan konversi
        if isinstance(nilai, str):
            # Hapus koma dan spasi
            nilai_bersih = nilai.replace(',', '').replace(' ', '')
            return float(nilai_bersih)
            
        return 0.0
        
    except (ValueError, TypeError):
        return 0.0


def generate_data_contoh():
    """
    Menghasilkan data contoh untuk testing
    Karena API IDX mungkin tidak accessible
    
    Returns:
        list: List dictionary data contoh
    """
    # Data contoh saham IDX
    data_contoh = [
        {'code': 'AADI', 'prevPrice': 150, 'openPrice': 155, 'closePrice': 160, 
         'highPrice': 165, 'lowPrice': 150, 'volume': 1000000, 'frequency': 500},
        {'code': 'AALI', 'prevPrice': 2500, 'openPrice': 2550, 'closePrice': 2600, 
         'highPrice': 2650, 'lowPrice': 2500, 'volume': 500000, 'frequency': 300},
        {'code': 'ACES', 'prevPrice': 980, 'openPrice': 990, 'closePrice': 1000, 
         'highPrice': 1010, 'lowPrice': 980, 'volume': 800000, 'frequency': 400},
        {'code': 'ADHI', 'prevPrice': 850, 'openPrice': 860, 'closePrice': 870, 
         'highPrice': 880, 'lowPrice': 850, 'volume': 600000, 'frequency': 350},
        {'code': 'ADRO', 'prevPrice': 2800, 'openPrice': 2850, 'closePrice': 2900, 
         'highPrice': 2950, 'lowPrice': 2800, 'volume': 1200000, 'frequency': 600},
        {'code': 'AGRO', 'prevPrice': 350, 'openPrice': 355, 'closePrice': 360, 
         'highPrice': 365, 'lowPrice': 350, 'volume': 400000, 'frequency': 250},
        {'code': 'AIMS', 'prevPrice': 210, 'openPrice': 215, 'closePrice': 220, 
         'highPrice': 225, 'lowPrice': 210, 'volume': 300000, 'frequency': 200},
        {'code': 'AKPI', 'prevPrice': 450, 'openPrice': 455, 'closePrice': 460, 
         'highPrice': 465, 'lowPrice': 450, 'volume': 350000, 'frequency': 220},
        {'code': 'ANTM', 'prevPrice': 1800, 'openPrice': 1820, 'closePrice': 1850, 
         'highPrice': 1870, 'lowPrice': 1800, 'volume': 900000, 'frequency': 450},
        {'code': 'APEX', 'prevPrice': 520, 'openPrice': 525, 'closePrice': 530, 
         'highPrice': 535, 'lowPrice': 520, 'volume': 250000, 'frequency': 180}
    ]
    
    # Tambahkan lebih banyak data untuk testing
    kode_saham = ['ASII', 'BBCA', 'BBNI', 'BBRI', 'BBTN', 'BFIN', 'BKGI', 'BMRI', 
                  'BNGA', 'BNLI', 'BRAM', 'BSIM', 'BTPN', 'BUMI', 'CPIN', 'CTRA',
                  'DMAS', 'DOID', 'ELSA', 'EMTK', 'ENRG', 'ERAA', 'EXCL', 'GAMA',
                  'GGRM', 'GIAA', 'GMFI', 'GOLD', 'HEAL', 'HIMI', 'HRUM', 'ICBP',
                  'INCO', 'INDF', 'INDY', 'INKP', 'INTP', 'ITMG', 'JPFA', 'KAEF',
                  'KLBF', 'LPKR', 'LPPB', 'LSIP', 'MAPI', 'MEDC', 'MEGA', 'MIKA',
                  'MNCN', 'MPPA', 'MRAT', 'MSIN', 'MTDL', 'MTFN', 'MYOR', 'NIKL',
                  'NISP', 'OMRE', 'PALM', 'PGAS', 'PGLI', 'PKPK', 'PLMN', 'PNBN',
                  'PNLF', 'POOL', 'PTBA', 'PTPP', 'PUDP', 'PWON', 'RAJA', 'RALS',
                  'RCCX', 'RELI', 'RIMO', 'ROTI', 'RSMH', 'RUIS', 'SAME', 'SCMA',
                  'SDMU', 'SHID', 'SILO', 'SMCB', 'SMGR', 'SMRA', 'SPMA', 'SQMI',
                  'SRIL', 'SSMS', 'SSTM', 'STTP', 'SUGI', 'TAHU', 'TARA', 'TBLA',
                  'TINS', 'TKIM', 'TLKM', 'TMAS', 'TOTO', 'TPIA', 'TRIM', 'TRIS',
                  'UNTR', 'UNVR', 'VICO', 'WIKA', 'WINS', 'WIT', 'WSKT', 'WTON']
    
    import random
    from datetime import datetime, timedelta
    
    tanggal_hari_ini = datetime.now().strftime('%Y-%m-%d')
    
    # Generate data untuk setiap kode
    for kode in kode_saham:
        harga_dasar = random.randint(100, 5000)
        harga_buka = harga_dasar + random.randint(-50, 50)
        harga_tutup = harga_buka + random.randint(-30, 30)
        harga_tinggi = max(harga_buka, harga_tutup) + random.randint(0, 20)
        harga_rendah = min(harga_buka, harga_tutup) - random.randint(0, 20)
        volume = random.randint(100000, 5000000)
        frekuensi = random.randint(100, 1000)
        
        data_contoh.append({
            'code': kode,
            'prevPrice': harga_dasar,
            'openPrice': harga_buka,
            'closePrice': harga_tutup,
            'highPrice': harga_tinggi,
            'lowPrice': harga_rendah,
            'volume': volume,
            'frequency': frekuensi
        })
    
    return {'data': data_contoh}


def ambil_data_saham(use_api=True):
    """
    Mengambil data saham, bisa dari API atau data contoh
    
    Args:
        use_api: True jika ingin mengambil dari API, False untuk data contoh
    
    Returns:
        list: List dictionary data saham
    """
    if use_api:
        # Coba ambil dari API
        data_raw = ambil_data_dari_api()
        
        if data_raw:
            return proses_data(data_raw)
        else:
            print("API tidak dapat diakses, menggunakan data contoh...")
            return proses_data(generate_data_contoh())
    else:
        # Gunakan data contoh
        return proses_data(generate_data_contoh())