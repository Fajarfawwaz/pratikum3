# pratikum3
# BIODATA
# NAMA : FAJAR FAWWAZ ATALLAH
# KELAS TI.24.A4
# NIM : 312410357
# MATKUL: BAHASA PEMROGRAMAN
# ![WhatsApp Image 2024-10-20 at 10 55 01_a29547f6](https://github.com/user-attachments/assets/c75f7ade-4c8e-4282-bab8-a60d34b2e7cc)
# PRATIKUM 3
# Latihan KE 1
# ![Screenshot 2024-10-15 143542](https://github.com/user-attachments/assets/7da59fdf-531e-4872-b291-07ccd0f28c9b)
```Python
#penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('z')

#penggunaan separator
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='.....')
```
Penggunaan print () digunakan untuk mencetak output, seperti syntax dibawah ini :
Penggunaan END Penggunaan end dipakai untuk menambahkan karakter yang dicetak di akhir baris. secara default penggunaan end adalah untuk ganti baris.
```Python
print('A', end='')
print('B', end='')
print('C', end='')
```
Penggunaan print () digunakan untuk mencetak output, seperti syntax dibawah ini :
```Python
print()
```
Syntax dibawah ini digunakan untuk menampilkan output berupa string
```Python
print('X')
print('Y')
print('z')
```
Hasil dari source code tersebut seperti gambar dibawah ini :
# ![Screenshot 2024-10-15 133640](https://github.com/user-attachments/assets/bbd4b023-3b5c-4926-93a6-61ce7606138b)
Penggunaan separator Pendeklarasian beberapa variable beserta nilainya
```python
w,x,y,z=10,15,20,25
```
Menampilkan hasil dari variable tiap-tiap variable
```Python
print(w,x,y,z)
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah : (koma)
```python
print(w,x,y,z,sep=",")
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah
```Python
print(w,x,y,z,sep="")
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah : (titik dua)
```Python
print(w,x,y,z,sep=":")
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah -----
```Python
print(w,x,y,z,sep="-----")
```
hasil dari syntax / source code diatas adalah seperti berikut ini :
# ![Screenshot 2024-10-15 133703](https://github.com/user-attachments/assets/1a287e65-bd0e-46f9-9f51-1c4eea73d767)
# LATIHAN KE 2
# ![Screenshot 2024-10-15 135657](https://github.com/user-attachments/assets/e108554a-cf40-4257-93c0-c2491b9a134a)
```Python
a=int(input("masukkan nilai a:"))
b=int(input("masukkan nilai b:"))
print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil pejumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
```
Sekarang Kita akan coba lagi untuk run file tersebut, maka akan muncul seperti gambar dibawah ini :
# ![Screenshot 2024-10-15 140328](https://github.com/user-attachments/assets/dac02ba3-1821-4a93-9129-86b7be5ee1ab)
String Format String formatting atau pemformatan string memungkinan kita menyuntikkan item kedalam string dari pada kita mencoba menggabungkan string menggunakan koma atau string concatenation. Penggunaan source code yang di berikan oleh dosen seperti berikut :
# ![Screenshot 2024-10-15 140431](https://github.com/user-attachments/assets/35de4ec4-9b49-45c1-bf7b-91992b67421d)
```Python
#string format 1
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

#string format 2
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
```
String Format 1 Pada syntax / source code strring format satu akan menampilkan output berupa 2 outputan. Yang pertama (sebelah kiri) akan menampilkan angka urut dari angka 0 hingga 10, sedangkan untuk sebelah kanan akan menampilkan Operasi Aritmatika Pangkat. Dengan ketentuan sebagai berikut, Operasi pangkat dengan angka kiri sebagai pokok (Rumus : ** [bintang dua] ) Hasil dari syntax tersebut adalah 10 pangkat 0, hingga 10 pangkat 10, dengan output sebagai berikut :
# ![Screenshot 2024-10-15 141036](https://github.com/user-attachments/assets/9a3b03fb-16bd-4fda-b9b5-8db463979225)
2 * String Format 2* Pada syntax atau source code string format dua akan menampilkan output berupa 2 output'an juga (seperti String Format 1, yaitu kanan dan kiri ) Dengan ketentuan sebagai berikut :

secara Default, .format() menggunakan rata kiri, angka ke kanan. kita dapat menggunakan opsi opsional <,^, atau > untuk mengatur perataan kiri, tengah, atau kanan. Contoh lain dalam penggunaan .format() sebagai berikut :
Untuk hasil dari String Format 2 adalah :
# ![Screenshot 2024-10-15 141347](https://github.com/user-attachments/assets/78812982-5628-46be-a65d-f8147092cf13)
