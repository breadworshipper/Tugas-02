1. )
- [10/Sep/2022 09:42:49] "GET /katalog/ HTTP/1.1" 200 1951
| Di sini request dari client akan diteruskan dari urls.py ke views.py untuk menampilkan laman /katalog
- [10/Sep/2022 09:42:49] "GET /static/css/style.css HTTP/1.1" 404 1798 | Di sini views.py akan menampilkan laman /katalog
dengan mengambil file HTML atau CSS yang terdapat pada folder template

2.)
Kita menggunakan virtual environment agar package yang kita install untuk project tidak terinstall juga di environment
global komputer. Hal ini dilakukan agar jika kita ingin membuat project kedepannya tidak ada package yang tabrakan. 
  Kita masih bisa membuat web django tanpa virtual environment, namun seperti yang saya sebutkan sebelumnya, best 
  practicenya tetap menggunakan virtual environment.

3.) Pertama, saya menambahkan function ```show_katalog``` di views.py untuk mengambil template HTML. Lalu, 
initialize database django lokal dengan file .json yang terdapat di folder fixtures sebagai datanya. Kemudian, routing 
  URL dengan menambahkan function yang ada di view ke urls.py dan ini akan terpanggil jika terdapat request ke route 
  tersebut. Selanjutnya, menambahkan data yang ada di file .json dengan menambahkan argumen context yaitu dictionary 
  yang berisi data yang kita ingin masukkan ke dalam file HTML. Di dalam file HTML kita tambahkan data yang ada di file
  .json dengan ```{% for katalog in katalog_list %}```. Terakhir, deploy ke Heroku melalui GitHub dengan inisialisasi 
  git di repositori lokal dengan ```git init```, lalu ```git add .``` untuk menambahkan file-file yang ingin di-commit, 
  selanjutnya ```git commit -m ""``` untuk commit, terakhir tambahkan url repositori GitHub dan ```git push origin main```
  untuk menyimpan repo lokal ke repositori yang ada di GitHub. Langkah terakhir hanya pasang secrets untuk heroku app 
  name dan API key akun Heroku dan pasang ulang actionnya yang gagal untuk build ke Heroku.