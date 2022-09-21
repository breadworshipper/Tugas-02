1. JSON (JavaScript Object Notation) berdasarkan pada bahaasa JavaScript, sedangkan XML (Extenxible Markup Language) 
adalah bahasa markup dan menggunakan tag untuk merepresentasikan data. JSON dan XML berfungsi untuk menyimpan data.
   HTML (Hypertext Markup Language) digunakan untuk menampilkan sesuatu di suatu web.
   
2. Data delivery diperlukan untuk keperluan data yang ada pada di platform tersebut. Misal HTML, XML, JSON, JPG, dan 
lain-lain. Tanpa data delivery tidak ada data yang dapat ditampilkan pada platform kita.
3. Untuk XML dan JSON, saya tambahkan pada views.py function yang menerima request dan me-return
XML atau JSON dengan function HTTPResponse dengan argumen application/xml atau application/json pada parameter content_type
4. 