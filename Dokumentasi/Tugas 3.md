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

2. Kemudian menghitung private key, lalu hasil private key disimpan dalam file txt. 

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar2.JPG)

3. Setelah itu, server akan membaca hasil dari client_key.txt. Lalu menghitung shared key dan hasil shared key disimpan ke file txt.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar3.JPG)

4. Pesan dari client dienkripsi dan disimpan ke file enkripsi.txt, lalu mengeksekusi file dekripsi.py untuk memproses hasil dekripsi pesan. Setelah itu hasil dekripsi disimpan ke file dekripsi.txt.

![alt tag](https://github.com/niakurniam/KIJ-F/blob/master/Tugas%203%20Diffie%20Hillman/Screenshot/gambar4.JPG)

5. 
