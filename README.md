- Repo: https://github.com/Alvino0706/football-shop
- Web: http://alvino-revaldi-footballshop.pbp.cs.ui.ac.id

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    (1) Membuat sebuah proyek Django baru.
        - Membuat direktori baru dan mengaktifkan virtual environment.
        - Menambahkan file-file yang diperlukan seperti .env, .gitignore, dll
        - Menginstall hal-hal yang diperlukan yang ditampung terlebih dahulu dalam requirements.txt
    (2) Membuat aplikasi dengan nama main pada proyek tersebut.
        - Menggunakan perintah python manage.py startapp main
    (3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Menambahkan isi dari urlpatterns:
            from django.urls import include
            urlpatterns = [
            path('', include('main.urls')),
            ]
    (4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
        - Membuat model dengan nama Product dan Menambahkan atribut wajib pada models.py
        - Mengaplikasikan migrasi model untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru. Caranya adalah dengan menggunakan python manage.py makemigrations untuk menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data dan menggunakan python manage.py migrate untuk mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya.
    (5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - Membuat sebuah fungsi dengan nama show_main dengan parameter request (menerima request dari user)
        - Tugas utama view adalah mengubah request menjadi response.
    (6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Membuat file urls.py pada direktori main
        - Mengisi file urls.py dengan:
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
    (7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        -  Membuat project baru di pws sehingga dapat disubmit dan dilihat menggunakan internet dengan menggunakan perintah:
            git remote add pws https://pbp.cs.ui.ac.id/alvino.revaldi/footballshop
            git branch -M master
            git push pws master
    (8) Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.



2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
    - Bagan : https://drive.google.com/file/d/191g1Mo9yxC2ckwGg2QNfu3FM3x0PgKDO/view?usp=sharing
    (1) urls.py (Request)
        Client mengirim request ke path tertentu. urls.py mencocokkan pola URL dan mengarahkan ke view yang tepat.
    (2) views.py
        View menerima request, menjalankan logika aplikasilalu:
        - Jika butuh data, memanggil models.py lewat ORM untuk read/write.
        - Jika ingin menampilkan halaman, view merender template dengan render(request, "<file>.html", context).
    (3) models.py
        Berisi definisi tabel/relasi dan operasi database. View menggunakan model untuk query/CRUD, hasilnya dikirim balik ke view sebagai objek/queryset.
    (4) Template HTML
        File tampilan yang menerima context dari view (data yang akan ditampilkan). Template engine menghasilkan HTML final.
    (5) Response
        HTML yang sudah dirender dikembalikan oleh view sebagai response ke client.
    
3. Jelaskan peran settings.py dalam proyek Django!
    Settings.py berfungsi untuk mengkonfigurasi berbagai aspek proyek Django. File settings.py berisi konfigurasi dan pengaturan untuk aplikasi Django seperti pengaturan basis data, aplikasi yang diinstal, jalur statis dan media, serta banyak lainnya.
    Sumber: https://klc2.kemenkeu.go.id/kms/knowledge/bagaimana-mengelola-settings-pada-sebuah-proyek-berbasis-django-1e465638/detail/

4. Bagaimana cara kerja migrasi database di Django?
    (1) Ubah model di models.py.
    (2) Jalankan makemigrations → Django membandingkan definisi model dengan state terakhir dan membuat berkas migrasi (mis. 0002_add_field.py) berisi daftar operasi: CreateModel, AddField, AlterField, DeleteModel, dll.
    (3) Jalankan migrate → Django menyusun graf dependensi antar migrasi (lintas-app), menjalankan operasi yang belum diterapkan ke DB (eksekusi SQL), dan mencatat yang sudah dijalankan di tabel khusus django_migrations agar tidak diulang.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Konvensi kuat: struktur proyek jelas (settings/urls/views/models/templates) sehingga memudahkan memahami arsitektur web modern.
    - Keamanan bawaan: proteksi CSRF, XSS, SQL injection, password hashing sehingga sejak awal belajar secure by default.
    - Produktif untuk CRUD: ORM dan admin mempercepat eksperimen konsep.
    - Skalabilitas konsep: setelah paham MVT dan middleware, mudah memahami framework lain (Flask/FastAPI, bahkan arsitektur di luar Python).
    - Ekosistem & dokumentasi: contoh dan paket banyak (rest framework, dll.), bagus untuk pemula.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    - Ritme penjelasan runut dari setup → model → view → template.
    - Live-coding membantu melihat kesalahan umum dan solusinya.