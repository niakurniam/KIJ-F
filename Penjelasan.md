# Algoritma DES
- DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis <i>cipher</i> blok.
- DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci 
internal (internal key) atau upa-kunci (<i>subkey</i>). Kunci internal dibangkitkan dari kunci eksternal (<i>external key</i>) 
yang panjangnya 64 bit.
- Skema global dari algoritma DES adalah sebagai berikut:
1. Blok plainteks dipermutasi dengan matriks permutasi awal
(<i>initial permutation</i> atau IP).
2. Hasil permutasi awal kemudian di-<i>enciphering</i>- sebanyak
16 kali (16 putaran). Setiap putaran menggunakan kunci
internal yang berbeda.
3. Hasil <i>enciphering</i> kemudian dipermutasi dengan matriks
permutasi balikan (<i>invers initial permutation</i> atau IP-1
 ) menjadi blok cipherteks.
 
 # Mode CFB
 - Dalam CFB, data dienkripsikan dalam unit yang lebih kecil daripada ukuran blok.
 - Unit yang dienkripsikan dapat berupa bit per bit (seperti <i>cipher</i> aliran), 2 bit, 3 bit, dst.
 
