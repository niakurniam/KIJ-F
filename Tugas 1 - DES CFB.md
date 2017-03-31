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


 
