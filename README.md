# Indo Weather Pipeline

Project ini merupakan pipeline cuaca sederhana yang menggunakan mock API sebagai sumber data. Pipeline ini mengambil data cuaca dan menyimpannya ke file JSON.

## Struktur File
- `fetch_weather.py`: Skrip untuk mengambil data cuaca dari API dan menyimpannya ke JSON.
- `docker-compose.yaml`: Konfigurasi Docker Compose untuk menjalankan pipeline.
- `requirements.txt`: Daftar dependensi yang dibutuhkan.
- `.gitignore`: File yang perlu diabaikan oleh Git.
- `LICENSE`: Informasi lisensi proyek.
- `README.md`: Dokumentasi proyek.

## Cara Menggunakan
1. Clone repositori ini.
2. Set nilai `API_URL` dan `API_KEY` dalam file `docker-compose.yaml`.
3. Jalankan perintah:
4. Data cuaca akan disimpan sebagai file JSON di direktori proyek.

## License
Proyek ini dilisensikan di bawah MIT License.

