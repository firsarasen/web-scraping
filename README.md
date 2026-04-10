# News Data Extractor

Script ini adalah alat otomatisasi berbasis Python yang dirancang untuk mengambil data berita secara lokal. Program ini bekerja dengan cara memindai struktur HTML situs dan mengonversinya menjadi format data yang siap digunakan untuk analisis lebih lanjut.

## Alur Kerja Program
1. **Request**: Mengambil kode HTML mentah dari `website berita pilihan`.
2. **Parsing**: Mencari elemen berita utama menggunakan tag `h1` dengan class `hlTitle`.
3. **Cleaning**: Membersihkan teks judul dari spasi atau karakter yang tidak diperlukan.
4. **Export**: Menyimpan kumpulan data secara simultan ke dalam dua format file berbeda (.csv dan .json).

## Persiapan Lingkungan

Ikuti langkah-langkah di bawah ini untuk memastikan script berjalan tanpa kendala:

### 1. Inisialisasi Project & Virtual Env
Buka terminal/CMD di folder proyek Anda, lalu jalankan perintah berikut sesuai sistem operasi Anda:

**Windows:**
```bash
# Membuat environment
python -m venv venv

# Mengaktifkan environment
venv\Scripts\activate
```
macOS/Linux:
```bash
# Membuat environment
python3 -m venv venv

# Mengaktifkan environment
source venv/bin/activate
```
### 2. Instalasi Dependensi
Script ini memerlukan dua library eksternal utama:
```bash
pip install requests beautifulsoup4
```
### 3. Eksekusi Script
Jalankan program di terminal dengan perintah:
```bash
python main.py
```
