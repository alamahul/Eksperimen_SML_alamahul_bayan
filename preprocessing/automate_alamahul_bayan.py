import pandas as pd
import os

def run_preprocessing(input_path, output_path):
    print("Mulai proses otomatisasi preprocessing data...")

    # ---------------------------------------------------------
    # 1. DATA LOADING
    # ---------------------------------------------------------
    try:
        df = pd.read_csv(input_path)
        print(f"[INFO] Berhasil memuat data dari '{input_path}' dengan dimensi {df.shape}")
    except FileNotFoundError:
        print(f"[ERROR] File mentah di '{input_path}' tidak ditemukan!")
        return

    # ---------------------------------------------------------
    # 2. PREPROCESSING DATA
    # ---------------------------------------------------------
    
    df_clean = df.dropna()
    print("[INFO] Nilai kosong (missing values) berhasil dihapus.")

    # Hapus atau ubah nama kolom 'id' sesuai dengan dataset Anda
    if 'id' in df_clean.columns:
        df_clean = df_clean.drop(columns=['id'])
        print("[INFO] Kolom 'id' berhasil dihapus.")


    # ---------------------------------------------------------
    # 3. MENYIMPAN DATA BERSIH
    # ---------------------------------------------------------
    # Memastikan folder tujuan (preprocessing) ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Menyimpan file dataset yang sudah bersih
    df_clean.to_csv(output_path, index=False)
    print(f"[SUKSES] Data bersih berhasil disimpan di '{output_path}' dengan dimensi {df_clean.shape}")

if __name__ == "__main__":
    FILE_MENTAH = "../movie_genre_classification_final.csv" 
    
    # Tentukan path/lokasi penyimpanan hasil pembersihan
    FILE_BERSIH = "./movie_genre_classification_final_clean.csv" 
    
    # Jalankan fungsi utama
    run_preprocessing(FILE_MENTAH, FILE_BERSIH)