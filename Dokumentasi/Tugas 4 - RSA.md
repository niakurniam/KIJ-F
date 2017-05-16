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
### Client
1. Import library pickle dan tambahkan fungsi-fungsi sebagai converter.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar1.JPG);

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar2.JPG);

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar3.JPG);

2. Buatlah fungsi multiplicative inverse untuk mencari nilai private key.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar4.JPG);

3. Buatlah fungsi untuk mendapatkan key-nya.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar5.JPG);

4. Buatlah fungsi untuk mengenkripsi dan mendekripsi pesan.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar6.JPG);

5. 

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar7.JPG);

6. 

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar8.JPG);

7. 

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar9.JPG);

### Server
1. Import library pickle dan tambahkan fungsi-fungsi sebagai converter.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar10.JPG);

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar11.JPG);

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar12.JPG);

2. Buatlah fungsi multiplicative inverse untuk mencari nilai private key.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar13.JPG);

3. Buatlah fungsi untuk mendapatkan key-nya.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar14.JPG);

4. Buatlah fungsi untuk mengenkripsi dan mendekripsi pesan.

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar15.JPG);

5. 

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar16.JPG);

6. 

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar17.JPG);

7. 

![alt_tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%204%20-%20RSA/Screenshot/gambar18.JPG);
