1. Synchronous programming sendiri akan memiliki program yang bersifat berjalan secara sequential berdasarkan antrian 
eksekusi program. Sedangkan, asynchronous programming akan memiliki program yang berjalan secara asynchronous atau dapat
berjalan tanpa menunggu antrian eksekusi.
2. Event-Driven Programming adalah paradigma yang di mana cara kerjanya bergantung pada event atau peristiwa tertentu. 
Misal pada tugas ini, bila button create task di-klik, maka web akan me-redirect ke laman baru. Hal ini terjadi karena 
terdapat event button create task di-click.
3. Penerapan asynchronous programming pada AJAX dapat menggunakan jquery dengan $.ajax. Contohnya dalam tugas ini,
digunakan ajax untuk mengambil data dari /json secara asynchronous, sehingga tidak perlu untuk me-reload page untuk 
meng-update data yang ada di todolist.
4. Pada tugas ini digunakan AJAX untuk mengambil data dan menge-post data ke database secara asynchronous. Pada todolist.html
terdapat penerapan AJAX GET dan AJAX POST dalam bagian <script>.
```
    $(document).ready(function () {
      setInterval(function () {
        $.ajax({
          type: "GET",
          url: "{% url 'todolist:json' %}",
          success: function (response) {
            // console.log(response);
            $(".container").empty();
            for (var key in response) {
              var responseLength = response.length;

              if ((key + 1) % 3 == 1) {
                result += '<div class="row gx-5">';
              }

              result +=
                `
              <div class="col-md-4">
                <div class="card" style="width: 18rem">
                  <div class="card-body">
                    <h5 class="card-title">` +
                response[key].fields.title +
                " (" +
                response[key].fields.date +
                ")" +
                `</h5>
                    <p class="card-text">` +
                response[key].fields.description +
                `</p>
                  </div>
                </div>
              </div>
              `;

              if ((key + 1) % 3 == 0 || responseLength - key == 1) {
                result += `
                </div>
                <br>
                `;
              }
            }
            $(".container").append(result);
            result = "";
            console.log(result);
          },
          error: function (response) {
            // alert("Error getting data");
          },
        });
      }, 1000);
    });
```
Dengan ini, web dapat mengambil data secara asynchronous dari json tanpa harus me-reload page.
```
    $('#modalForm').on('submit', function(e) {
      $.ajax({
        method: 'POST',
        url : $('#modalForm').data('url'),
        data: {
          tasktitle: $('#tasktitle').val(),
          description: $('#description').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {
            
            alert('Data Successfully Posted');

          },
      });
      $("#modalTask").modal('hide');
      return false
    });
```
Dengan ini, form yang terdapat pada modal akan ter-post secara asynchronous 