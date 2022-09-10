- [10/Sep/2022 09:42:49] "GET /katalog/ HTTP/1.1" 200 1951
  
  [10/Sep/2022 09:42:49] "GET /static/css/style.css HTTP/1.1" 404 1798

- Kita menggunakan virtual environment agar package yang kita install untuk project tidak terinstall juga di environment
global komputer. Hal ini dilakukan agar jika kita ingin membuat project kedepannya tidak ada package yang tabrakan. 
  Kita masih bisa membuat web django tanpa virtual environment, namun seperti yang saya sebutkan sebelumnya, best 
  practicenya tetap menggunakan virtual environment.

- Pertama, saya menambahkan function ```show_katalog``` di views.py untuk mengambil template HTML. Lalu, 
initialize database django lokal dengan file .json yang terdapat di folder fixtures sebagai datanya. Kemudian, routing 
  URL dengan menambahkan function yang ada di view ke urls.py dan ini akan terpanggil jika terdapat request ke route 
  tersebut. Selanjutnya, menambahkan data yang ada di file .json dengan menambahkan argumen context yaitu dictionary 
  yang berisi data yang kita ingin masukkan ke dalam file HTML. Di dalam file HTML kita tambahkan data yang ada di file
  .json dengan ```{% for katalog in katalog_list %}```. 