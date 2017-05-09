# Tugas 4 - RSA

## Pendahuluan
RSA Cipher atau kriptografi kunci publik merupakan salah satu kriptografi asimetris, dimana kunci untuk melakukan enkripsi dan dekripsi berbeda. Kekuatan utama RSA adalah kesulitan dalam memfaktorkan bilangan yang besar (NP Hard Problem), sehingga dapat dimanfaatkan untuk mengamankan data.

## Langkah-Langkah 
Langkah-langkah dalam mengenkripsi atau mendekripsi RSA adalah sebagai berikut :
1. Pilih dua bilangan prima a dan b.
2. Hitung nilai n = a*b, usahakan setidaknya n > 255 agar dapat mewakili seluruh karakter ASCII.
3. Hitung nilai m = (a-1)*(b-1)
4. Cari nilai e, dimana e merupakan relatif prima dari m.
5. Cari nilai d, yang memenuhi persamaan ed ≡ 1 mod m atau d = e^-1 mod m.
6. Kunci public (e,n) dan kunci private (d,n).
7. Fungsi enkripsi: ![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/rumus1.JPG); dimana ta merupakan karakter ke-a dari message (pesan) yang akan dienkripsi.
8. Fungsi dekripsi: ![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/rumus2.JPG); dimana ca merupakan karakter ke-a dari ciphertext yang akan didekripsikan.

## Hasil Implementasi
### Server
1. Setting dari server

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar1.JPG)

2. Kemudian menghitung private key, lalu hasil private key disimpan dalam file txt. 

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar2.JPG)

3. Setelah itu, server akan membaca hasil dari client_key.txt. Lalu menghitung shared key dan hasil shared key disimpan ke file txt.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar3.JPG)

4. Pesan dari client dienkripsi dan disimpan ke file enkripsi.txt, lalu mengeksekusi file dekripsi.py untuk memproses hasil dekripsi pesan. Setelah itu hasil dekripsi disimpan ke file dekripsi.txt.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar4.JPG)

### Client
1. Setting dari client

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar5.JPG)

2. Menghitung private key. Kemudian hasil dari perhitungan private key disimpan di client_key.txt dan server_key.txt harus memiliki isi yang sama dengan file client_key.txt. Setelah itu kita bisa mendapatkan shared key-nya

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar6.JPG)

3. File dataset.txt adalah untuk menyimpan sebuah pesan. Kemudian eksekusi enkripsi.py untuk mengenkripsi pesan tersebut. Setelah itu hasil enkripsi disimpan di enkripsi.txt. Selanjutnya, hasil enkripsi didekripsi dan hasil dekripsi disimpan dalam bentuk file txt

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar7.JPG)

4. Berikut ini adalah hasil peritungan dari Diffie-Hellman

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar8.JPG)
