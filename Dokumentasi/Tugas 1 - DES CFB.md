# Tugas 1 - DES CFB

## Anggota Kelompok 15:
1. M. Luqmanul Hakim P.    5114100081
2. Mustika Kurnia M.       5114100126

## Pendahuluan
DES (_Data Encryption Standard_) adalah algoritma cipher blok yang populer karena dijadikan standard algoritma enkripsi kunci-simetri, meskipun saat ini standard tersebut telah digantikan oleh algoritma yang baru yaitu, AES. Alasannya adalah karena DES sudah dianggap tidak aman lagi. Sebenarnya DES adalah nama standard enkripsi simetri. Nama algoritma enkripsinya adalah DEA (_Data Encryption Algorithm_).

## Dasar Teori
### DES
DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit _Plaintext_ menjadi 64 bit _Ciphertext_ dengan menggunakan 56 bit kunci internal (_internal key_) atau _subkey_. Kunci Internal dibangkitkan dari kunci eksternal yang panjangnya 64 bit.
### Metode CFB
Metode _Cipher Feedback_ menggunakan sistem Shift Register, dimana yang diproses terlebih dahulu adalah _Initialization Vector_ (IV) dalam algoritma Enkripsi dengan _key_. Setelah diproses, bit yang dihasilkan akan melalui proses seleksi bit, biasanya bit-bit paling kiri, untuk selanjutnya dienkripsi dengan Plaintext untuk menghasilkan Ciphertext. Bit hasil seleksi yang digunakan tergantung besarnya bit blok plaintext yang diinput. Selanjutnya, setelah mendapatkan blok ciphertext, selain di output, blok ciphertext tersebut dimasukkan ke IV yang sebelumnya, dan IV digeser sebanyak bit blok ciphertext sebelumnya, yang selanjutnya IV yang telah digeser bersama blok ciphertext yang digabung bersama IV tersebut diproses kembali oleh algoritma Enkripsi tersebut.

## Mengimplementasikan DES Dengan Metode CFB
1. Konversikan string ke bit dan sebaliknya.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/1.JPG)

2. Lakukan input data yaitu, initial vector, plaintext, serta key. Untuk key minimal 8 karakter.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/2.JPG)

3. Lalu, hitung panjang pesan yang diinput.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/3.JPG)

4. Buatlah sebuah fungsi untuk memasukkan key permutation.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/4.JPG)

5. Lalu, hasil permutation key yang awalnya 32 bit di expand menjadi 48 bit.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/5.JPG)

6. Buatlah fungsi S-Box. S-Box di sini adalah untuk menukar key dan plaintext.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/6.JPG)

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/7.JPG)

7. Kemudian mencari nilai S-Box

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/8.JPG)

8. Setelah didapatkan nilai vektor B ke-i, langkah-langkah selanjutnya memutasikan bit vektor menggunakan P-Box. Kemudian dikelompokkan menjadi 4 blok di mana tiap blok memiliki 32 bit data.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/9.JPG)

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/10.JPG)

9. Lalu, lakukan shift untuk menukar key dimulaidari bit paling kiri.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/11.JPG)

10. Lakukan permutation choice yang kedua.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/12.JPG)

11. Buatlah fungsi untuk melakukan permutasi pada plaintext.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/13.JPG)

12. Buatlah fungsi untuk mengenkripsi pesan.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/14.JPG)

Untuk memunculkan permutasi sampai paling akhir.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/15.JPG)

13. Buatlah fungsi untuk dekripsi pesan.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/16.JPG)

Untuk hasil akhir dekripsi pesan.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/17.JPG)

14. Untuk memunculkan hasil dari enkripsi dan dekripsi.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/18.JPG)

## Hasil Output

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%201%20-%20DES%20CFB/Screenshot/output.JPG)

Sumber : http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
         https://github.com/toddw-as/pyDes/blob/master/pyDes.py

 
