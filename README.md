"# mustard-sports"

Cara saya membuat tugas ini dan mengimplementasikan checklist yang ada di web pbp adalah dengan pertama saya membuat proyek django yang sebelumnya sudah dipelajari saat sesi lab. Pembuatan ini diawali dengan membuat direktori baru bernama mustard-sports, lalu saya mengaktifkan virutal enivornment dan membuat proyek django menggunakan requirements.txt, isi dari file txt tersebut adalah hal-hal yang diperlukan untuk menginstall django. Instalasinya juga tidak rumit dan hanya memerlukan 1 perintah di command prompt, waktunya juga tidak begitu lama. Setelah django terinstall, saya membuat file .env yang meurpakan environment variables yang disimpan di luar kode program. Environment variables adalah variabel yang disimpan di luar kode program dan digunakan untuk menyimpan informasi konfigurasi seperti kredensial database, API keys, atau pengaturan environment. Ini memungkinkan kode yang sama berjalan di environment berbeda tanpa perlu mengubah kode. Lalu saya juga membuat file .env.prod yang digunakan untuk production deployment. Karena PRODUCTION=True, aplikasi akan menggunakan database PostgreSQL dengan kredensial yang disediakan ITF Fasilkom UI. Lalu saya juga mengubah settings.py agar dapat menggunakan environment variables. Kemudian saya juga mengubah isi dari ALLOWED_HOSTS agar bisa mengakses aplikasi web lewat local host. Tak lupa juga saya menambahkan konfigurasi PRODUCTION dan mengubah konfigurasi database di settings.py. 

Setelah itu saya menyambungkan direktori mustard-sports dengan github dengan membuat repositori baru di github, lalu saya melakukan git init untuk membuat folder .git, lalu saya juga membuat file/berkas .gitignore untuk menentukan berkas-berkas yang diabaikan oleh git. Lalu saya melakukan git remote add origin (link repositori) agar git tahu harus mengirim kode saya ke repositori spesifik itu saat melakukan push. Lalu saya membuast branch utama bernama master dan melalukan add, commit, push.

Setelah itu, saya melakukan deploy lewat PWS. Pertama saya membuat proyek baru di PWS dan mengubah environs dengan isi dari berkas   .env.prod lalu saya menambahkan URL dari deployment PWS ke ALLOWED_HOSTS agar saya bisa view project. Lalu saya melakukan push ke pws agar kode di pws merupakan yang paling baru.

Setelah itu, saya membuat aplikasi baru yang bernama main pada proyek saya yang bernama mustard sports. Lalu agar main dapat dijalankan di proyek, saya menambahkan main ke INSTALLED_APPS. Karena tema utama dari proyek ini adalah toko bola, maka saya mengubah model-model yang ada di models.py. Model-model yang saya guanakn adalah jersey, sepatu, celana, joggers, kaus kaki, bola, dan lainnya. Lalu saya menambahkan nama untuk nama item, price untuk harga item, description untuk deskripsi item, category untuk kategori item, thumbnail untuk gambar item, dan is_featured untuk menunjukkan barang yang 'featured' atau sedang direkomendasikan.
Alasan saya menggunakan tipe data yang digunakan adalah karena
nama, category : CharField karena tipe data yang cocok untuk menyimpan teks singkat
price : IntegerField karena tipe data yang cocok untuk menyimpan angka
deskripsi : TextField karena tipe data cocok untuk menyimpan teks panjang
thumbnail : URLField karena tipe data yang cocok untuk menyimpan url, untuk kasus ini gambar
is_featured : BooleanField karena tipe data yang paling cocok untuk mewakili kondisi biner

Setelah model-model dibuat, saya membuat HTML template dengan file main.html. Fungsi dari file ini unntuk menyimpan konten dasar dari TUgas 1, termasuk teks "Main", nama, dan kelas saya. Tujuannya adalah untuk menampilkan halaman ini melalui routing. Routing saya lakukan dengan menggunakan file views.py dan urls.py. views.py berfungsi untuk memproses permintaan dan mengirim respons, dan urls.py berfungsi untuk menentukan jalur URL.

Dalam proyek ini, di views.py ada sebuah fungsi show_main yang berfungsi untuk mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. Dalam kata lain, fungsi ini digunakan untuk merender file main.html. Lalu kode di main.html juga diubah agar sesuai dengan struktur django, contohnya seperti {{ name }} yang akan menampilkan nama saya "Alexius Christhoper Wijaya". Perubahan ini hanya akan terlihat jika membuka aplikasi lewat routing yang diatur oleh urls.py dan views.py. Jadi jika membuka file html langsung maka tidak akan ada perubahan. 

Setelah melakukan routing, saya melakukan deployment di PWS dan saya mengupdate repository saya dengan
git add .
git commit -m "penambahan model, html, dll"
git push origin master
git push pws master

# Bagan request client ke web aplikasi berbasis django
![alt text](image.png) reference: https://medium.com/@im_khalidbutt/understanding-the-django-request-lifecycle-6ea5ea48caec
Di bagan tersebut, kit abisa melihat alur dari request client ke web. Pertama client akan melakukan request yang akan diterima oleh URL router, setelah itu diarahkan ke views dan akan diproses oleh context processor menuju ke template yang sesuai. Setelah itu akan mengelola database dan menghasilkan halaman web yang akan dikirim kembali ke client untuk ditampilkan.
Fungsi dari masing-masing komponen:
- client -> pengguna web
- URL -> Melakukan matching dari request path ke fungsi di dalam views
- Views -> melakukan interaksi dengan model dan database, lalu menghasilkan context processor yang akan memilik template yang tepat
- Model -> struktur data dari aplikasi
- Template -> file html, dalam proyek ini bernama main.html yang berisi markup statis, menampilkan data dinamis yang dikirimkan oleh views

# Fungsi settings.py pada proyek django
Dalam sebuah proyej django, file settings.py berperan sebagai pusat konfigurasi yang menyimpan banyak pengaturan penting. Dengan mengubah isi dari settings.py kita bisa menambahkan atau menghapus ALLOWED_HOSTS, mencantumkan aplikasi, memberikan detail databse, dan menggunakan env. Jadi settings.py berfungsi sebagai pusat konfigurasi utama dalam proyek django.

# Cara kerja migrasi database di django
Migrasi database dalam django ada lah cara untuk menyelaraskan perubahan yang dibuat di model python dengan struktur tabel database. Hal ini memudahkan kita karena kita tidak perlu menulis SQL secara manual.

manage.py makemigrations -> membuat file migrasi di folder migrations/ (berfungsi utk menggambarkan perubahan pada databse) 
manage.py migrate -> django menerjemahkan file migrasi menjadi perintah SQL sesuai dengan database dan mengeksekusinya

# Kelebihan framework django
Beberapa kelebihan dari penggunaan django adalah bahasanya yang simple dan mudah dipahami karena menggunakan python, django memiliki banyak fitur yang dapat digunakan, django memiliki standar keamanan yang tinggi dan baik, django juga memiliki banyak hal mulai dari server web dan mesin templat hingga Object Relational Mapper (ORM), dan yang terakhit django juga scalable.

# Feedback
Untuk tutorial 1, menurut saya langkah-langkahnya sudah cukup mudah diikuti dan penjelasannya juga cukup mudah dipahami. Hanya saja karena terhalang akibat online jadinya sedikit lebih sulit saat ingin bertanya. Akan tetapi, penjelasan dari web juga sudah cukup.

# Tugas 3
1. Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena hal ini dibutuhkan untuk memenuhi requirement dalam menampilkan maupun mengirimkan data yang relevan. Proses ini memungkinkan pertukaran data dari satu stack ke stack lainnya. Data delivery dapat dilakukan melalui berbagai format seperti HTML, JSON, dan XML, dengan JSON sebagai format yang paling umum digunakan karena sifatnya yang ringan dan mudah dipahami oleh mesin maupun manusia. Format-format tersebut berfungsi sebagai bahasa universal untuk memastikan data yang dikirim dapat diterima dan dimengerti. Sementara itu, HTML berperan dalam menampilkan data yang diterima menjadi bentuk visual yang dapat diakses pengguna.
2. Format daya delivery yang lebih baik adalah JSON, hal ini karena JSON terintegrasi dengan JavaScript yang merupakan bahasa pemrograman yang cukup populer dan membuat komunikasi antar layanan menjadi lebih mudah. Lalu JSON lebih mirip dengan struktur objek di bahasa pemrograman modern (JavaScript, Python, Java, dsb.), sehingga lebih mudah dipahami oleh developer. XML relatif lebih rumit dengan hierarki tag yang panjang.
3. Fungsi dari method is_valid() pada form Django (misalnya di views.py pada function add_product) adalah untuk melakukan checking terhadap data yang dikirim melalui form, apakah sudah sesuai aturan validasi yang ditentukan. Method ini sangat penting karena secara otomatis akan menolak data yang tidak valid agar tidak masuk ke database, misalnya jika format input salah atau ada field yang kosong padahal wajib diisi. Selain menjaga integritas dan keamanan data, is_valid() juga membuat proses coding lebih efisien karena developer tidak perlu menulis logika validasi manual, sekaligus memudahkan pemberian feedback error ke pengguna.
4. csrf_token diperlukan saat membuat form di Django karena token ini yang digenerate otomatis oleh Django berfungsi sebagai lapisan keamanan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Pada proyek ini kita juga menggunakan CSRF Trusted Origins untuk memberikan kepercayaan ke URL yang dideploy (harus mencantumkan protokol, mis. https://...). Jika csrf_token tidak ditambahkan, aplikasi menjadi rentan: penyerang bisa memaksa pengguna yang sudah ter-authenticated mengirimkan permintaan HTTP palsu (mis. ubah password, transfer uang, hapus data) tanpa sepengetahuan mereka. Serangan biasanya dilakukan dengan mengarahkan korban ke situs phishing yang menyertakan HTML tersembunyi atau skrip yang otomatis meng-submit form ke situs Django; karena browser mengirim cookie sesi korban, server akan menerima permintaan tersebut jika tidak ada token CSRF untuk diverifikasi.
5. Cara saya mengimplementasikan checklist adalah denagn pertama melakukan aktivasi virtual environment, lalu mengimplementasikan skeleton (base.html) yang berfungsi sebagai kerangka views. Lalu saya mengisi DIRS dengan BASE_DIR / 'templates' sebagai path yang terhubung dengan ptoject. Lalu APP_DIRS menjadi true dan hal ini perlu dilakukan agar templates milik app diprioritaskan daripasa base_site.html. Lalu saya menggunakan base.html untuk template utama dan menambahkan beberapa kode di main.html. Lalu saya membuat forms.py untuk membuat form yang dapat menerima data product baru. Lalu saya mengubah views.py dan menambahkan fungsi seperti add_product, show_product, dan import baru. Lalu saya menambahkan button add product, thumbnail, dan deskripsi product. Lalu saya menambahkan add_product dan product_detail di templates. Lalu saya menambahkan fungsi untuk mengembalikan data dalam xml dan json yang dipelajari dari tutorial sebelumnya. Agar hal tersebut dapat dilakukan, views.py perlu ditambahkan beberapa import dari django. Lalu saya melakukan edit juga di urls.py untuk menambahkan import dari fungsi yang sudah dibuat dan menambahkan path. Setelah selesai, saya mengecek dengan menggunakan localhost dari produk yang ditambahkan dan menggunakan postman untuk melihat hasil dari seluruh step. Lalu saya melakukan deactivate dan commit dan push.
6. Tidak ada feedback, asistensi untuk tutorial sudah cukup baik dan mudah dipahami

# screenshot
postman xml = ![alt text](image-2.png)
postman xml id = ![alt text](image-3.png)
postman json = ![alt text](image-4.png)
postman json id = ![alt text](image-5.png)