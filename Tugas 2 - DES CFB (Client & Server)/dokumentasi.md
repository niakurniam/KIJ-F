## Tahapan Pengerjaan
Pada tugas kali ini, kami akan mendemonstrasikan implementasi algoritma DES dengan sistem client server. sebelumnya kami akan menjelaskan apa itu client dan server. Client-server adalah suatu bentuk arsitektur, dimana client adalah perangkat yang menerima yang akan menampilkan dan menjalankan aplikasi (software komputer) dan server adalah perangkat yang menyediakan dan bertindak sebagai pengelola aplikasi, data, dan keamanannya. alurnya sebagai berikut:

1. awalnya setting host dan port dari client dan server
2. kemudian jalankan server-nya terlebih dahulu, baru clientnya.
3. setelah keduanya dinyalakan maka masukkan key.
4. setelah itu masukkan plain text atau pesan yang akan anda kirim.

dari sisi enkripsinya, alurnya sebagai berikut:
1. setelah key dan plain text nya dimasukkan, maka key dan text tersebut akan disimpan dalam file pesan.txt dan key.txt.
2. kemudian setelah tersimpan di file txt, maka file akan dieksekusi dalam file cobades1.py, dimana enkripsi akan dilakukan
3. setelah dienkripsi oleh file cobades1.py, maka hasil dari enkripsi tersebut akan disimpan kembai dalam file hasilenkrip.txt
4. lalu dari file hasilenkrip.txt hasil enkripsi terebut akan dikirim ke server.
5. sebelum diterima oleh server, data dari hasilenkrip.txt hasil enkripsi, akan didekripsi kembali dengan menggunakan key yang sama, sehingga pesan dapat dibaca oleh server.
6. setelah didecrypt, maka dari sisi server akan mengambil teks hasil dekripsi tadi. dan teks tersampaikan pada sisi server.

alur tersebut juga berlaku pada sisi server, hanya berkebalikan saja.

sumber: 
1. https://security.stackexchange.com/questions/7390/how-to-properly-encrypt-a-communication-channel-between-a-client-and-a-server-w
2. https://docs.python.org/2/howto/sockets.html
3. http://www.bogotobogo.com/python/python_network_programming_server_client.php
