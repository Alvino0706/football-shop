- Repo: https://github.com/Alvino0706/football-shop
- Web: http://alvino-revaldi-footballshop.pbp.cs.ui.ac.id

# Answering in README.MD

## Tugas 2

---

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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
      ]'
(4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
- Membuat model dengan nama Product dan Menambahkan atribut wajib pada models.py
- Mengaplikasikan migrasi model untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru. Caranya adalah dengan menggunakan `python manage.py makemigrations` untuk menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data dan menggunakan `python manage.py migrate` untuk mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya.

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



### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
Bagan : https://drive.google.com/file/d/191g1Mo9yxC2ckwGg2QNfu3FM3x0PgKDO/view?usp=sharing
- urls.py (Request)

  Client mengirim request ke path tertentu. urls.py mencocokkan pola URL dan mengarahkan ke view yang tepat.
- views.py
  
  View menerima request, menjalankan logika aplikasi lalu:
    - Jika butuh data, memanggil models.py lewat ORM untuk read/write.
    - Jika ingin menampilkan halaman, view merender template dengan render(request, "<file>.html", context).
- models.py
  
  Berisi definisi tabel/relasi dan operasi database. View menggunakan model untuk query/CRUD, hasilnya dikirim balik ke view sebagai objek/queryset.
- Template HTML
  
  File tampilan yang menerima context dari view (data yang akan ditampilkan). Template engine menghasilkan HTML final.
- Response
  
  HTML yang sudah dirender dikembalikan oleh view sebagai response ke client.
    
### 3. Jelaskan peran settings.py dalam proyek Django!
Settings.py berfungsi untuk mengkonfigurasi berbagai aspek proyek Django. File settings.py berisi konfigurasi dan pengaturan untuk aplikasi Django seperti pengaturan basis data, aplikasi yang diinstal, jalur statis dan media, serta banyak lainnya.
Sumber: https://klc2.kemenkeu.go.id/kms/knowledge/bagaimana-mengelola-settings-pada-sebuah-proyek-berbasis-django-1e465638/detail/

### 4. Bagaimana cara kerja migrasi database di Django?

(1) Ubah model di models.py.


(2) Jalankan makemigrations → Django membandingkan definisi model dengan state terakhir dan membuat berkas migrasi (mis. 0002_add_field.py) berisi daftar operasi: CreateModel, AddField, AlterField, DeleteModel, dll.


(3) Jalankan migrate → Django menyusun graf dependensi antar migrasi (lintas-app), menjalankan operasi yang belum diterapkan ke DB (eksekusi SQL), dan mencatat yang sudah dijalankan di tabel khusus django_migrations agar tidak diulang.

### 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Konvensi kuat: struktur proyek jelas (settings/urls/views/models/templates) sehingga memudahkan memahami arsitektur web modern.
- Keamanan bawaan: proteksi CSRF, XSS, SQL injection, password hashing sehingga sejak awal belajar secure by default.
- Produktif untuk CRUD: ORM dan admin mempercepat eksperimen konsep.
- Skalabilitas konsep: setelah paham MVT dan middleware, mudah memahami framework lain (Flask/FastAPI, bahkan arsitektur di luar Python).
- Ekosistem & dokumentasi: contoh dan paket banyak (rest framework, dll.), bagus untuk pemula.

### 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
- Ritme penjelasan runut dari setup → model → view → template.
- Live-coding membantu melihat kesalahan umum dan solusinya.


## Tugas 3

---

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena platform hanya akan berguna jika data yang diproses dan dihasilkan dapat dikirimkan ke pihak yang membutuhkannya dengan tepat, cepat, dan aman. Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Aspek | XML | JSON | 
--- | --- | --- | 
Struktur | Menggunakan tag pembuka dan penutup | Menggunakan pasangan key–value |
Size | Lebih panjang karena banyak tag | Lebih ringkas dan ringan |
Tipe data | Semua data berupa teks | Mendukung tipe data asli: string, number, boolean, array, object |

Menurut saya, yang lebih baik antara XML dan JSON adalah JSON. Selain itu, JSON memang lebih populer dibandingkan dengan XML karena lebih mudah diproses oleh banyak bahasa pemrograman masa kini yang mana salah satunya adalah python. (Sumber: https://dasarpemrogramanpython.novalagung.com/basic/json#:~:text=Operasi%20JSON%20(%20JavaScript%20Object%20Notation%20),json%20(%20JavaScript%20Object%20Notation%20)%20.)

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk memvalidasi data yang sudah di-bind ke form. Kita membutuhkan method tersebut. Kita membutuhkan method `is_valid()` untuk memastikan input aman & benar, memberi respon error ke user, dan mencegah crash & melindungi database di mana validasi di level form mencegah pelanggaran constraint/tipe sebelum sampai ke database.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF atau Cross-Site Request Forgery adalah serangan yang memungkinkan situs web jahat melakukan tindakan atas nama pengguna yang terautentikasi. Django menyediakan built-in CSRF protection. Hal ini lah alasan mengapa kita membutuhkan csrf_token saat membuat form di Django. Jika kita tidak menambahkan csrf_token pada form Django, penyerang dapat membuat browser kita melakukan aksi tanpa sepengetahuan kita. Hal ini dapat dimanfaatkan oleh penyerang dengan mengirim link ke suatu halaman dan kita membuka halaman tersebut. Selanjutnya browser akan mengirim session cookie ke form kita dan jika endpoint tidak memeriksa CSRF token, server mengeksekusi aksi (hapus produk, ganti email, transfer dana, dll).

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
(1) Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Saya menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan, dalam proyek ini objek yang dimaksud adalah product. Berikut fungsinya:

    def show_xml(request):
         product_list = Product.objects.all()
         xml_data = serializers.serialize("xml", product_list)
         return HttpResponse(xml_data, content_type="application/xml")
    
    def show_json(request):
        product_list = Product.objects.all()
        json_data = serializers.serialize("json", product_list)
        return HttpResponse(json_data, content_type="application/json")
    
    def show_xml_by_id(request, product_id):
       try:
           product_item = Product.objects.filter(pk=product_id)
           xml_data = serializers.serialize("xml", product_item)
           return HttpResponse(xml_data, content_type="application/xml")
       except Product.DoesNotExist:
           return HttpResponse(status=404)
    
    def show_json_by_id(request, product_id):
       try:
           product_item = Product.objects.get(pk=product_id)
           json_data = serializers.serialize("json", [product_item])
           return HttpResponse(json_data, content_type="application/json")
       except Product.DoesNotExist:
           return HttpResponse(status=404)

(2) Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
Saya membuat routing url untuk masing-masing views yang telah ditambahkan ke `urlpatterns` untuk mengakses fungsi yang sudah dibuat tadi (perlu diimpor di `urls.py`).

    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    ...

(3) Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
Saya membuat file html (main.html) yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form (diteruskan ke create_product.html), serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek (diteruskan ke product_detail.html). Saya juga menampilkan kategori apakah produk tersebut, apakah produk tersebut merupakan produk unggulan, apakah produk tersebut merupakan barang baru atau bekas, harganya, dan jumlah stok yang tersedia. 

Main.html:

    <h1>Football Shop</h1>

    <h5>NPM: </h5>
    <p>{{ npm }}</p>
    
    <h5>Name:</h5>
    <p>{{ name }}</p>
    
    <h5>Class:</h5>
    <p>{{ class }}</p>
    
    <a href="{% url 'main:create_product' %}">
      <button>+ Add Product</button>
    </a>
    
    <hr>
    
    {% if not product_list %}
    <p>Belum ada data barang pada football product.</p>
    {% else %}
    
    {% for product in product_list %}
    <div>
      <h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>
    
      <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
        <b>Featured</b>{% endif %} | <i>{{ product.get_condition_display }} | </i>
        Price: Rp{{ product.price }},00 | Stock: {{ product.stock }}
      </p>
    
      {% if product.thumbnail %}
      <img src="{{ product.thumbnail }}" alt="{{ product.name }} thumbnail" width="150" height="100">
      <br />
      {% endif %}
    
      <p>{{ product.content|truncatewords:25 }}...</p>
    
      <p><a href="{% url 'main:show_product' product.id %}"><button>Read More</button></a></p>
    </div>
    
    <hr>
    {% endfor %}
    
    {% endif %}

create_product.html:

    {% extends 'base.html' %}
    {% block content %}
    <h1>Add Product</h1>
    
    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td>
            <input type="submit" value="Add PRODUCT" />
          </td>
        </tr>
      </table>
    </form>
    
    {% endblock %}

(4) Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
Saya membuat file baru yaitu `forms.py` untuk membuat struktur form yang dapat menerima data Product baru (objek model pada app sebelumnya).

    from django.forms import ModelForm
    from main.models import Product
    
    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "stock", "description", "thumbnail", "category", "condition", "is_featured"]

(5) Membuat halaman yang menampilkan detail dari setiap data objek model.
Saya membuat product_detail.html:

product_detail.html:

    {% extends 'base.html' %}
    {% block content %}
    <p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>
    
    <h1>{{ product.name }}</h1>
      <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
        <b>Featured</b>{% endif %} | <i>{{ product.get_condition_display }} | </i>
        Price: Rp{{ product.price }},00 | Stock: {{ product.stock }}
      </p>
    
    {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt=" {{ product.name }} thumbnail" width="300">
    <br /><br />
    {% endif %}
    
    <p>{{ product.description }}</p>
    
    {% endblock content %}


### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Sudah sangat membantu.

### Link Screenshot Postman: https://drive.google.com/drive/folders/1HNZU0pDkQ2HT68aKyJSK8if-LZ1hTSDN?usp=sharing
