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
<<<<<<< HEAD

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

## Tugas 4

---

### 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form bawaan Django yang berfungsi untuk menolak pengguna yang `is_active` flag-nya disetel ke False. Singkatnya, form ini digunakan untuk proses login (otorisasi) di Django.

Kelebihan | Kekurangan | 
--- | --- | 
Siap pakai dan sudah terintegrasi dengan Django | Terbatas pada username+password secara default |
Error handlingnya jelas | Belum mencakup signup, reset password, email verification, dll |
Aman secara default di mana password dicek via hashing sehingga otomatis bekerja baik dengan CSRF di template | Tidak memuat fitur anti-abuse seperti captcha |

### 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi | Otorisasi | 
--- | --- | 
Proses memverifikasi identitas pengguna | Proses menentukan hak akses setelah identitas diverifikasi |
Biasanya berhubungan erat dengan username dan password | Menjawab pertanyaan "Apakah pengguna boleh membaca data ini? mengedit? menghapus?" |
Contoh: Login dengan akun email & password. | Contoh: Admin boleh hapus produk, user biasa tidak boleh. |

Django mengimplementasikan kedua konsep tersebut dengan cara:
- Autentikasi: Menggunakan authentication framework milik Django (django.contrib.auth). Ketika user memasukkan username dan password, jika valid ID user akan disimpan di session.
- Otorisasi: Django tidak built-in penuh, tapi bisa pakai `django-guardian` atau melakukan kustomisasi sendiri. Django juga menyediakan decorators dan mixins seperti `@login_required`, `@permission_required('app_name.permission_code')`, `UserPassesTestMixin`, dan `PermissionRequiredMixin`.

### 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session
Kelebihan | Kekurangan | 
--- | --- | 
Lebih aman karena data ada di server dan client hanya punya ID | Semakin banyak user aktif, maka semakin besar storage sessionnya |
Mampu menyimpan data besar & kompleks | Butuh manajemen tambahan seperti session timeout, invalidasi manual, dll |
Mudah dikontrol di mana server bisa menghapus/expire session kapan saja | Masih tergantung cookies/header untuk menyimpan session ID di sisi client |

Cookies
Kelebihan | Kekurangan | 
--- | --- | 
Mudah diakses client | Ukuran terbatas (± 4 KB per cookie) |
Tidak membebani server karena disimpan di sisi client | mudah dibaca/dimanipulasi user, meskipun bisa di-encrypt |
Cocok untuk data ringan seperti pilihan tema, last visited page, dll | Tidak cocok untuk data sensitif seperti password atau session token mentah |

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Cookies tidak aman sepenuhnya dalam pengembangan web. Terdapat potensi risiko yang harus diwaspadai, seperti adanya manipulasi data, pencurian cookies, dan karena cookie dikirim otomatis pada setiap request ke domain terkait, attacker bisa memanfaatkan ini untuk memalsukan request dari browser user. Django menangani hal ini dengan:
- Session cookies terenkripsi
- Pengaturan keamanan cookie (di settings.py)
- CSRF Protection ({% csrf_token %})
- Rotasi session key, tujuannya supaya session lama tidak bisa dipakai lagi jika dicuri.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
(1) Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Registrasi:

    def register(request):
      form = UserCreationForm()
  
      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)

Login:

    def login_user(request):
       if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
    
          if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')
    
       else:
          form = AuthenticationForm(request)
       context = {'form': form}
       return render(request, 'login.html', context)

Logout:

    def logout_user(request):
        logout(request)
        return redirect('main:login')

(2) Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
Saya menjalankan program dengan `python manage.py runserver`, membuka di browser, dan mulai melakukan registrasi sebanyak 2 kali. Saya login ke masing-masing akun dan membuat masing-masing 3 dummy data. Maksud dummy data di sini adalah produk yang dijual.

(3) Menghubungkan model Product dengan User.
Saya menambahkan `from django.contrib.auth.models import User` di models.py bagian paling atas bersama dengan import lainnya dan menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)` di dalam class Product untuk menghubungkan model Product dengan User.

(4) Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Saya melakukan perubahan pada fungsi `login_user` terutama pada bagian if form.is_valid() dengan menambahkan:

    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))

Saya juga melakukan perubahan pada fungsi `logout_user` dengan menambahkan:

    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')

dan mengubah return pada kedua fungsi tersebut menjadi `return response`. Pada fungsi `show_main` saya juga menambahkan context `'last_login': request.COOKIES.get('last_login', 'Never')` sehingga waktu terakhir pengguna login sekarang dapat ditampilkan di halaman web dengan mengakses key last_login. Namun, untuk menampilkannya, saya juga mengedit di main.html yaitu dengan menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` setelah tombol logout.

## Tugas 5

---

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
(1) Inline style (ditulis langsung pada elemen dengan style="")

(2) ID selector (#id)

(3) Class, pseudo-class, attribute selector (.class, :hover, [type="text"]).

(4) Element selector (p, h1, div) dan pseudo-element (::before, ::after).

(5) Urutan terakhir dalam file CSS. Jika specificity sama, aturan paling akhir yang menang (the cascade).

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design adalah desain web yang menyesuaikan tampilan sesuai ukuran layar (desktop, tablet, smartphone). Hal ini penting user-user sekarang banyak mengakses web dari berbagai device. Contoh yang sudah responsive adalah Shopee karena tampilan grid produk otomatis menyesuaikan layar HP maupun desktop. Contoh yang belum responsive adalah website lama berbasis HTML tabel (misalnya situs berita jadul) → di layar HP teks terlalu kecil, harus zoom in/out, tombol sulit ditekan, seperti https://rawpowerlifting.com/`

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin = jarak di luar border, memisahkan elemen dengan elemen lain.

- Border = garis yang mengelilingi konten/padding elemen.

- Padding = jarak antara konten dengan border elemen.

Cara implementasi:

    .box {
      margin: 20px;           /* jarak luar */
      border: 2px solid black;/* garis tepi */ 
      padding: 15px;          /* jarak dalam */
    }

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Konsep flex box dan grid layout adalah teknik modern untuk mengatur layout di CSS.

(1) Flexbox (Flexible Box Layout): 
- Digunakan untuk mengatur layout 1 dimensi (horizontal atau vertikal).
- Cocok untuk navbar, alignment item dalam baris/kolom.

(2) Grid Layout: 
- Digunakan untuk layout 2 dimensi (baris dan kolom sekaligus).
- Cocok untuk tampilan dashboard, galeri, katalog produk.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
(1) Implementasikan fungsi untuk menghapus dan mengedit product.

Menambahkan di views.py:

    def edit_product(request, id):
        product = get_object_or_404(Product, pk=id)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:show_main')

        context = {
            'form': form
        }

        return render(request, "edit_product.html", context)

    def delete_product(request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))

Menambahkan di urls.py:

    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),

(2) Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

  1. Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
     
  login.html

              {% extends 'base.html' %}
        
              {% block meta %}
              <title>Login - Goal Store</title>
              {% endblock meta %}
        
              {% block content %}
              <div class="bg-gray-50 w-full min-h-screen flex items-center justify-center p-8">
                <div class="max-w-md w-full">
                  <div class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
                    <div class="text-center mb-8">
                      <h1 class="text-2xl font-bold text-gray-900 mb-2">Sign In</h1>
                      <p class="text-gray-600">Welcome back to Goal Store</p>
                    </div>
    
                <!-- Form Errors Display -->
                {% if form.non_field_errors %}
                  <div class="mb-6">
                    {% for error in form.non_field_errors %}
                      <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700">
                        {{ error }}
                      </div>
                    {% endfor %}
                  </div>
                {% endif %}
    
                {% if form.errors %}
                  <div class="mb-6">
                    {% for field, errors in form.errors.items %}
                      {% if field != '__all__' %}
                        {% for error in errors %}
                          <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                            <strong>{{ field|title }}:</strong> {{ error }}
                          </div>
                        {% endfor %}
                      {% endif %}
                    {% endfor %}
                  </div>
                {% endif %}
    
                <form method="POST" action="" class="space-y-6">
                  {% csrf_token %}
                  
                  <div>
                    <label for="username" class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                    <input 
                      id="username" 
                      name="username" 
                      type="text" 
                      required 
                      class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500 transition-colors" 
                      placeholder="Enter your username">
                  </div>
    
                  <div>
                    <label for="password" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                    <input 
                      id="password" 
                      name="password" 
                      type="password" 
                      required 
                      class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500 transition-colors" 
                      placeholder="Enter your password">
                  </div>
    
                  <button 
                    type="submit" 
                    class="w-full bg-green-600 text-white font-medium py-3 px-4 rounded-md hover:bg-green-700 transition-colors">
                    Sign In
                  </button>
                </form>
    
                <!-- Messages Display -->
                {% if messages %}
                  <div class="mt-6">
                    {% for message in messages %}
                      <div 
                        class="
                          px-4 py-3 rounded-md text-sm border
                          {% if message.tags == 'success' %}
                            bg-green-50 border-green-200 text-green-700
                          {% elif message.tags == 'error' %}
                            bg-red-50 border-red-200 text-red-700
                          {% else %}
                            bg-gray-50 border-gray-200 text-gray-700
                          {% endif %}
                        ">
                        {{ message }}
                      </div>
                    {% endfor %}
                  </div>
                {% endif %}
    
                <div class="mt-6 text-center pt-6 border-t border-gray-200">
                  <p class="text-gray-500 text-sm">
                    Don't have an account? 
                    <a href="{% url 'main:register' %}" class="text-green-600 hover:text-green-700 font-medium">
                      Register Now
                    </a>
                  </p>
                </div>
              </div>
            </div>
          </div>
          {% endblock content %}

  register.html

      {% extends 'base.html' %}
      {% load static %}

      {% block meta %}
      <title>{{ product.name }} - Goal Store</title>
      {% endblock meta %}

      {% block content %}
      {% include 'navbar.html' %}
      <div class="bg-gray-50 w-full min-h-screen">
          <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
              
              <!-- Back Navigation -->
              <div class="mb-6">
                  <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
                      ← Back to Store
                  </a>
              </div>
              
              <!-- Article -->
              <article class="bg-white rounded-lg border border-gray-200 overflow-hidden">
                  
                  <!-- Header -->
                  <div class="p-6 sm:p-8">
                      <div class="flex flex-wrap items-center gap-2 mb-4">
                          <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-green-600 text-white">
                              {{ product.get_category_display }}
                          </span>
                          {% if product.is_featured %}
                              <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-yellow-100 text-yellow-800">
                                  Featured
                              </span>
                          {% endif %}
                          {% if product.is_product_hot %}
                              <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-red-100 text-red-800">
                                  Hot
                              </span>
                          {% endif %}
                      </div>
                      
                      <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 leading-tight mb-4">
                          {{ product.name }}
                      </h1>
                      
                      <div class="flex flex-wrap items-center text-sm text-gray-500 gap-4">
                          <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
                              <b>Featured</b>{% endif %} | <i>{{ product.get_condition_display }} | </i>
                              Price: Rp{{ product.price }},00 | Stock: {{ product.stock }}
                          </p>
                      </div>
                  </div>

                  <!-- Featured Image -->
                  {% if product.thumbnail %}
                      <div class="px-6 sm:px-8">
                          <img src="{{ product.thumbnail }}" 
                              alt="{{ product.name }}" 
                              class="w-full h-64 sm:h-80 lg:h-96 object-cover rounded-lg">
                      </div>
                  {% endif %}

                  <!-- Content -->
                  <div class="p-6 sm:p-8">
                      <div class="prose prose-lg max-w-none">
                          <div class="text-gray-700 leading-relaxed whitespace-pre-line text-base sm:text-lg">
                              <p>{{ product.description }}</p>
                          </div>
                      </div>
                  </div>

                  <!-- Author Info -->
                  <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-50">
                      <div class="flex items-center justify-between">
                          <div>
                              <div class="font-medium text-gray-900">
                                  {% if product.user %}
                                      <p>Author: {{ product.user.username }}</p>
                                  {% else %}
                                      <p>Author: Anonymous</p>
                                  {% endif %}
                              </div>
                              <p class="text-sm text-gray-500">Author</p>
                          </div>
                      </div>
                  </div>

                  <div class="border-t border-gray-200 p-6 sm:p-8 bg-white">
                      <div class="flex justify-end">
                          <form action="{% url 'main:buy_product' product.id %}" method="POST">
                          {% csrf_token %}
                          <button type="submit"
                              class="inline-flex items-center px-6 py-3 bg-green-600 text-white text-lg font-medium rounded-lg shadow hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 transition">
                              🛒 Buy Now
                          </button>
                          </form>
                      </div>
                  </div>
              </article>
              
          </div>

      </div>
      {% endblock content %}

  create_product.html

      {% load static %}
      <article class="bg-white rounded-xl shadow hover:shadow-md transition overflow-hidden flex border border-gray-200">
        
        <!-- Thumbnail -->
        <div class="w-1/3 relative">
          {% if product.thumbnail %}
            <img src="{{ product.thumbnail }}" alt="{{ product.name }}"
                class="w-full h-full object-cover">
          {% else %}
            <div class="w-full h-full bg-gray-200 flex items-center justify-center text-gray-400">
              No Image
            </div>
          {% endif %}
          
          <!-- Badge kategori -->
          <div class="absolute top-2 left-2">
            <span class="px-2 py-0.5 rounded-md text-xs font-medium bg-green-600 text-white shadow">
              {{ product.get_category_display }}
            </span>
          </div>
        </div>

        <!-- Content -->
        <div class="w-2/3 flex flex-col p-4">
          <!-- Nama + Harga -->
          <div class="mb-2">
            <h3 class="text-base font-semibold text-gray-900 line-clamp-1">
              <a href="{% url 'main:show_product' product.id %}" class="hover:text-green-600 transition">
                {{ product.name }}
              </a>
            </h3>
            <p class="text-green-700 font-bold text-sm">Rp {{ product.price }}</p>
          </div>

          <!-- Deskripsi -->
          <p class="text-gray-600 text-xs leading-relaxed line-clamp-2 flex-1 mb-3">
            {{ product.description|truncatewords:18 }}
          </p>

          <!-- Action Buttons -->
          <div class="flex items-center justify-between">
            <a href="{% url 'main:show_product' product.id %}"
              class="text-xs px-3 py-1.5 bg-green-600 text-white rounded-md hover:bg-green-700 transition">
              Read more
            </a>

            {% if user.is_authenticated and product.user == user %}
              <div class="flex gap-2">
                <a href="{% url 'main:edit_product' product.id %}"
                  class="text-xs px-2 py-1 bg-gray-200 text-gray-700 rounded hover:bg-gray-300 transition">
                  Edit
                </a>
                <a href="{% url 'main:delete_product' product.id %}"
                  class="text-xs px-2 py-1 bg-red-600 text-white rounded hover:bg-red-700 transition">
                  Delete
                </a>
              </div>
            {% else %}
              <form method="POST" action="{% url 'main:buy_product' product.id %}">
                {% csrf_token %}
                <button type="submit"
                  class="text-xs px-3 py-1.5 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition">
                  🛒 Buy
                </button>
              </form>
            {% endif %}
          </div>
        </div>
      </article>

  edit_product.html


      {% extends 'base.html' %}
      {% load static %}

      {% block meta %}
      <title>Edit Product - Goal Store</title>
      {% endblock meta %}

      {% block content %}
      {% include 'navbar.html' %}
      <div class="bg-gray-50 w-full min-h-screen">
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          
          <!-- Back Navigation -->
          <div class="mb-6">
            <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
              ← Back to Store
            </a>
          </div>
          
          <!-- Form -->
          <div class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
            <div class="mb-8">
              <h1 class="text-2xl font-bold text-gray-900 mb-2">Edit Product</h1>
              <p class="text-gray-600">Update your product</p>
            </div>
            
            <form method="POST" class="space-y-6">
              {% csrf_token %}
              {% for field in form %}
                <div>
                  <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-gray-700 mb-2">
                    {{ field.label }}
                  </label>
                  <div class="w-full">
                    {{ field }}
                  </div>
                  {% if field.help_text %}
                    <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                    <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
                </div>
              {% endfor %}
              
              <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
                <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50 transition-colors text-center">
                  Cancel
                </a>
                <button type="submit" class="order-1 sm:order-2 flex-1 bg-green-600 text-white px-6 py-3 rounded-md font-medium hover:bg-green-700 transition-colors">
                  Update Product
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      {% endblock %}
  
  product_detail.html

      {% extends 'base.html' %}
      {% load static %}

      {% block meta %}
      <title>{{ product.name }} - Goal Store</title>
      {% endblock meta %}

      {% block content %}
      {% include 'navbar.html' %}
      <div class="bg-gray-50 w-full min-h-screen">
          <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
              
              <!-- Back Navigation -->
              <div class="mb-6">
                  <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
                      ← Back to Store
                  </a>
              </div>
              
              <!-- Article -->
              <article class="bg-white rounded-lg border border-gray-200 overflow-hidden">
                  
                  <!-- Header -->
                  <div class="p-6 sm:p-8">
                      <div class="flex flex-wrap items-center gap-2 mb-4">
                          <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-green-600 text-white">
                              {{ product.get_category_display }}
                          </span>
                          {% if product.is_featured %}
                              <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-yellow-100 text-yellow-800">
                                  Featured
                              </span>
                          {% endif %}
                          {% if product.is_product_hot %}
                              <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-red-100 text-red-800">
                                  Hot
                              </span>
                          {% endif %}
                      </div>
                      
                      <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 leading-tight mb-4">
                          {{ product.name }}
                      </h1>
                      
                      <div class="flex flex-wrap items-center text-sm text-gray-500 gap-4">
                          <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
                              <b>Featured</b>{% endif %} | <i>{{ product.get_condition_display }} | </i>
                              Price: Rp{{ product.price }},00 | Stock: {{ product.stock }}
                          </p>
                      </div>
                  </div>

                  <!-- Featured Image -->
                  {% if product.thumbnail %}
                      <div class="px-6 sm:px-8">
                          <img src="{{ product.thumbnail }}" 
                              alt="{{ product.name }}" 
                              class="w-full h-64 sm:h-80 lg:h-96 object-cover rounded-lg">
                      </div>
                  {% endif %}

                  <!-- Content -->
                  <div class="p-6 sm:p-8">
                      <div class="prose prose-lg max-w-none">
                          <div class="text-gray-700 leading-relaxed whitespace-pre-line text-base sm:text-lg">
                              <p>{{ product.description }}</p>
                          </div>
                      </div>
                  </div>

                  <!-- Author Info -->
                  <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-50">
                      <div class="flex items-center justify-between">
                          <div>
                              <div class="font-medium text-gray-900">
                                  {% if product.user %}
                                      <p>Author: {{ product.user.username }}</p>
                                  {% else %}
                                      <p>Author: Anonymous</p>
                                  {% endif %}
                              </div>
                              <p class="text-sm text-gray-500">Author</p>
                          </div>
                      </div>
                  </div>

                  <div class="border-t border-gray-200 p-6 sm:p-8 bg-white">
                      <div class="flex justify-end">
                          <form action="{% url 'main:buy_product' product.id %}" method="POST">
                          {% csrf_token %}
                          <button type="submit"
                              class="inline-flex items-center px-6 py-3 bg-green-600 text-white text-lg font-medium rounded-lg shadow hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 transition">
                              🛒 Buy Now
                          </button>
                          </form>
                      </div>
                  </div>
              </article>
              
          </div>

      </div>
      {% endblock content %}

  2. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
  - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
    
  main.html


      ...
      {% if not product_list %}
      <div class="bg-white rounded-lg border border-gray-200 p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-product.png' %}" alt="No product available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No product found</h3>
        <p class="text-gray-500 mb-6">Be the first to sell football product to the community.</p>
        <a href="{% url 'main:create_product' %}" class="inline-flex items-center px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors">
          Create Product
        </a>
      </div>
      ...
  
  - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
    
  card_product.html

        {% load static %}
        <article class="bg-white rounded-xl shadow hover:shadow-lg transition overflow-hidden flex flex-col">
  
          <!-- Thumbnail -->
          <div class="relative">
            {% if product.thumbnail %}
              <img src="{{ product.thumbnail }}" alt="{{ product.name }}"
                  class="w-full h-48 object-cover">
            {% else %}
              <div class="w-full h-48 bg-gray-200 flex items-center justify-center text-gray-400">
                No Image
              </div>
            {% endif %}
            
            <!-- Badge kategori -->
            <div class="absolute bottom-2 left-2 flex flex-wrap gap-2">
              <span class="px-2 py-0.5 rounded-md text-xs font-medium bg-green-600 text-white shadow">
                {{ product.get_category_display }}
              </span>
              {% if product.is_featured %}
                <span class="px-2 py-0.5 rounded-md text-xs font-medium bg-yellow-400 text-yellow-900 shadow">
                  Featured
                </span>
              {% endif %}
              {% if product.is_product_hot %}
                <span class="px-2 py-0.5 rounded-md text-xs font-medium bg-red-500 text-white shadow">
                  Hot
                </span>
              {% endif %}
            </div>
          </div>
  
          <!-- Content -->
          <div class="flex-1 flex flex-col p-5">
            <!-- Nama + Harga -->
            <div class="mb-3">
              <h3 class="text-lg font-semibold text-gray-900 mb-1 line-clamp-1">
                <a href="{% url 'main:show_product' product.id %}" class="hover:text-green-600 transition">
                  {{ product.name }}
                </a>
              </h3>
              <p class="text-green-700 font-bold text-sm">Rp {{ product.price }}</p>
            </div>
  
            <!-- Deskripsi -->
            <p class="text-gray-600 text-sm leading-relaxed line-clamp-2 flex-1 mb-4">
              {{ product.description|truncatewords:16 }}
            </p>
  
            <!-- Tombol Aksi -->
            <div class="flex items-center justify-between pt-4 border-t border-gray-100">
              <a href="{% url 'main:show_product' product.id %}"
                class="text-sm px-3 py-1.5 bg-green-600 text-white rounded-md hover:bg-green-700 transition">
                Read more
              </a>
  
              {% if user.is_authenticated and product.user == user %}
                <div class="flex gap-2">
                  <a href="{% url 'main:edit_product' product.id %}"
                    class="text-sm px-3 py-1.5 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition">
                    Edit
                  </a>
                  <a href="{% url 'main:delete_product' product.id %}"
                    class="text-sm px-3 py-1.5 bg-red-600 text-white rounded-md hover:bg-red-700 transition">
                    Delete
                  </a>
                </div>
              {% else %}
                <form method="POST" action="{% url 'main:buy_product' product.id %}">
                  {% csrf_token %}
                  <button type="submit"
                    class="text-sm px-3 py-1.5 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition">
                    🛒 Buy
                  </button>
                </form>
              {% endif %}
            </div>
          </div>
        </article>

  3. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
     
  card_product.html


          ...
          {% if user.is_authenticated and product.user == user %}
          <div class="flex gap-2">
            <a href="{% url 'main:edit_product' product.id %}"
                class="text-sm px-3 py-1.5 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition">
              Edit
            </a>
            <a href="{% url 'main:delete_product' product.id %}"
                class="text-sm px-3 py-1.5 bg-red-600 text-white rounded-md hover:bg-red-700 transition">
              Delete
            </a>
          </div>
          ...

  5. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
     
  navbar.html

          {% load static %}
          <nav class="fixed top-0 left-0 w-full bg-[#8F88B9] border-b border-black/10 shadow-sm z-50">
    
              <div class="max-w-7xl mx-auto px-6 lg:px-8">
                <div class="flex items-center justify-between h-16">
                  <!-- Logo -->
                  <a href="/">
                  <div class="flex items-center">
                            <img src="{% static 'image/logo copy.png' %}" alt="Goal Store logo"
                      class="h-10 w-[auto] object-contain rounded">
                  </div>
                  </a>
                  
                  <!-- Desktop Navigation -->
                  <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-black-600 hover:text-gray-900 font-medium transition-colors">
                      Home
                    </a>
                    <a href="{% url 'main:create_product' %}" class="text-black-600 hover:text-gray-900 font-medium transition-colors">
                      Create Product
                    </a>
                  </div>
                  
                  <!-- Desktop User Section -->
                  <div class="hidden md:flex items-center space-x-6">
                    {% if user.is_authenticated %}
                      <div class="text-right">
                        <div class="text-sm font-medium text-gray-900">{{ name|default:user.username }}</div>
                        <div class="text-xs text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
                      </div>
                      <a href="{% url 'main:logout' %}" class="text-red-700 hover:text-red-800 font-medium transition-colors">
                        Logout
                      </a>
                    {% else %}
                      <a href="{% url 'main:login' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
                        Login
                      </a>
                      <a href="{% url 'main:register' %}" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded font-medium transition-colors">
                        Register
                      </a>
                    {% endif %}
                  </div>
                  
                  <!-- Mobile Menu Button -->
                  <div class="md:hidden flex items-center">
                    <button class="mobile-menu-button p-2 text-gray-600 hover:text-gray-900 transition-colors">
                      <span class="sr-only">Open menu</span>
                      <div class="w-6 h-6 flex flex-col justify-center items-center">
                        <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
                        <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"></span>
                        <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
                      </div>
                    </button>
                  </div>
                </div>
              </div>
              <!-- Mobile Menu -->
              <div class="mobile-menu hidden md:hidden bg-white border-t border-gray-200">
                <div class="px-6 py-4 space-y-4">
                  <!-- Mobile Navigation Links -->
                  <div class="space-y-1">
                    <a href="/" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
                      Home
                    </a>
                    <a href="{% url 'main:create_product' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
                      Create Product
                    </a>
                  </div>
                  
                  <!-- Mobile User Section -->
                  <div class="border-t border-gray-200 pt-4">
                    {% if user.is_authenticated %}
                      <div class="mb-4">
                        <div class="font-medium text-gray-900">{{ name|default:user.username }}</div>
                        <div class="text-sm text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
                      </div>
                      <a href="{% url 'main:logout' %}" class="block text-red-600 hover:text-red-700 font-medium py-3 transition-colors">
                        Logout
                      </a>
                    {% else %}
                      <div class="space-y-3">
                        <a href="{% url 'main:login' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
                          Login
                        </a>
                        <a href="{% url 'main:register' %}" class="block bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded text-center transition-colors">
                          Register
                        </a>
                      </div>
                    {% endif %}
                  </div>
                </div>
              </div>
              <script>
                const btn = document.querySelector("button.mobile-menu-button");
                const menu = document.querySelector(".mobile-menu");
              
                btn.addEventListener("click", () => {
                  menu.classList.toggle("hidden");
                });
              </script>
            </nav>
