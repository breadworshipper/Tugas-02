1. csrf sendiri adalah cross-site request forgery yang artinya suatu orang menggunakan web lainnya untuk menggunakan 
request POST pada seseorang korban. csrf token akan menambahkan suatu string yang di-generate secara random untuk kepada
POST agar dapat diingat oleh server. Jika string csrf token sama dengan yang ada di server, maka POST akan diproses. 
Pada django, tanpa adanya {% csrf token %} request post tidak akan diproses.
2. Bisa, tapi jika hanya {{form}} saja maka format form yang ditampilkan akan berantakan. Lalu, untuk manual terdapat 
contoh (https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html). Ditambahkan 
{{ form.non_field_errors }}, {{ form.source.errors }}, dan {{ form.source }}. Lalu, mengakses field yang ada pada form

3. User akan tiba pada page dengan url /todolist/create-task. User akan mengirim HTTP request dengan method POST setelah 
klik tombol submit. Dari situ request akan di-handle oleh function create_task dan menyimpannya ke dalam database dengan 
panggilan form.save(). Lalu, funciton show_todo_list() akan menampilkan halaman dengan data task yang sudah di-submit 
sebelumnya
4. Pertama, bikin class baru dengan nama TaskForm di forms.py. Lalu, import ke views.py untuk digunakan pada function 
create_task(). Function tersebut akan digunakan untuk menampilkan form pada page create-task. Lalu akan dicek dengan 
form.is_valid() dan jika valid akan di-save ke database dengan form.save()

HEROKU : https://djangoajrakatalog.herokuapp.com/

1. Inline CSS adalah CSS yang terdapat di dalam suatu tag HTML. Kelebihan dari inline css adalah mudah untuk mengubah style 
dari suatu tag HTML yang spesifik, namun hal ini akan membuat struktur HTML kita akan lebih berantakan dan lebih sulit jika kita harus 
mencari tag tersebut untuk mengganti style-nya. Sebagai contoh
```
<h1 style="color:white;">Contoh</h1>
```

Internal CSS adalah CSS yang terdapat di dalam tag style yang terdapat di tag head. Kelebihan dari interal CSS adalah tidak perlu repot bikin 
file external lagi, namun dengan ini struktur dari HTML kita akan lebih berantakan/messy. Sebagai contoh
```
<head>
    <style>
    h1 {
        color : red;
        padding : 10px;
    }
    </style
</head
```

External CSS adalah CSS yang terdapat pada file external. Kelebihan dari External CSS adalah
file HTML yang kita pakai akan lebih rapih/clean, namun terdapat kemungkinan website kita tidak ke-render sebagaimana yang seharusnya
karena file CSS kita belum ter-load. 

2. ```<nav> untuk mendefinisikan suatu bagian dari link navigasi```
3. Element Selector adalah selector untuk memilih semua tag spesifik yang ada di HTML-nya.
Class Selector (digunakana dengan didahului .) untuk memilih semua tag yang memiliki class yang sama. ID selector (digunakan dengan didahului #)
untuk memilih semua tag yang memiliki id yang sama.
4. Untuk tugas ini hanya menggunakan inline css
