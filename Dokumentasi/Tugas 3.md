# Diffie - Hellman

## Algoritma Diffie-Hellman
- Kegunaan : untuk berbagi kunci enkripsi simetri yang sama antara 2 orang atau lebih
- Keamanan algoritma ditentukan oleh sulitnya menghitung logaritma diskrit
- Peneraan Algoritma :
1. Alice Membangkitkan bilangan bulat acak yang besar x dan mengirim hasil perhitungan berikut kepada Bob :

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/rumus1.PNG)

2. Bob membangkitkan bilangan bulat acak yang besar ydan mengirimhasil perhitungan berikut kepada Alice :

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/rumus2.PNG)

3. Alice menghitung

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/rumus3.PNG)

4. Bob menghitung

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/rumus4.PNG)

## Hasil Implementasi
### Server
1. Setting dari server

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar1.JPG)

2. Kemudian hasil dari private key diterima oleh client dalam bentuk format txt. Dan mendapatkan shared key dari hasil perhitungan algoritma Diffie-Hellman

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar2.JPG)

3. Ketika memasukkan pesan, maka pesan tersebut akan disimpan di dataset.txt. Lalu mengeksekusi hasil enkripsi.py untuk melakukan proses enkripsi pesan tersebut. Dan hasil enkripsi itu nantinya akan disimpan di enkripsi.txt

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar3.JPG)

4. Kemudian hasil enkripsi, didekripsi dan hasil dekripsi disimpan di dekripsi.txt

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar4.JPG)


