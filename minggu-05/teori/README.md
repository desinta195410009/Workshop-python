# 7. INPUT dan OUTPUT
Sumber : [tutorial python](https://docs.python.org/3.10/tutorial/inputoutput.html)


Ada beberapa cara untuk menampilkan output dari suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang. Bab ini akan membahas beberapa kemungkinan.

## 7.1 Fancier Output Formatting
Sejauh ini kita telah menemukan dua cara untuk menulis nilai: pernyataan ekspresi dan print() fungsi. (Cara ketiga adalah menggunakan write() metode objek file; file keluaran standar dapat dirujuk sebagai sys.stdout. Lihat Referensi Pustaka untuk informasi lebih lanjut tentang ini.)

Seringkali Anda ingin lebih mengontrol pemformatan output Anda daripada sekadar mencetak nilai yang dipisahkan oleh spasi. Ada beberapa cara untuk memformat output.

- Untuk menggunakan literal string berformat, mulailah string dengan fatau Fsebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda dapat menulis ekspresi Python antara {dan } karakter yang dapat merujuk ke variabel atau nilai literal.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
```

- Metode str.format() string membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan {dan }untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.

```python
>>> yes_votes = 42_572_654
>>> no_votes   = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
```

- Terakhir, Anda dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan untuk membuat tata letak apa pun yang dapat Anda bayangkan. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu.

Ketika Anda tidak membutuhkan output yang mewah tetapi hanya ingin tampilan cepat dari beberapa variabel untuk keperluan debugging, Anda dapat mengonversi nilai apa pun menjadi string dengan fungsi repr()or str().

Fungsi str()ini dimaksudkan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr()dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh interpreter (atau akan memaksa a SyntaxErrorjika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str()akan mengembalikan nilai yang sama dengan repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi yang berbeda.

Beberapa contoh :
```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10*3.25
>>> y = 200*200
>>> s= 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> #The repr() of a string adds string quotes and backlashes:
... hello ='hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> #The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

Modul string berisi Templatekelas yang menawarkan cara lain untuk mengganti nilai menjadi string, menggunakan placeholder seperti $xdan menggantinya dengan nilai dari kamus, tetapi menawarkan kontrol pemformatan yang jauh lebih sedikit.

### 7.1.1 Formatted String Literals
Literal string yang diformat (disingkat juga disebut f-string) memungkinkan Anda memasukkan nilai ekspresi Python di dalam string dengan mengawali string denganforFdan menulis ekspresi sebagai {expression}.

Penentu format opsional dapat mengikuti ekspresi. Ini memungkinkan kontrol yang lebih besar atas bagaimana nilai diformat. Contoh berikut membulatkan pi ke tiga tempat setelah desimal :

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142
```

Melewati bilangan bulat setelah ':'akan menyebabkan bidang itu menjadi jumlah karakter minimum. Ini berguna untuk membuat kolom berbaris.

```python
>>> table = {'Sjored': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...    print(f'{name:10} ==> {phone:10d}')
...
Sjored  ==> 4127
Jack    ==> 4098
Dcab    ==> 7678
```

Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. '!a'berlaku ascii(), '!s'berlaku str(), dan '!r' berlaku repr():

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
Untuk referensi tentang spesifikasi format ini, lihat panduan referensi untuk Bahasa Mini Spesifikasi Format .

### 7.1.2 The String format() Method

Penggunaan dasar str.format()metode ini terlihat seperti ini:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke str.format()metode. Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam str.format()metode.

```python
>>> print('{0} and {1}'.format('spam','eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam','eggs'))
eggs and spam
```

Jika argumen kata kunci digunakan dalam str.format()metode, nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> ('This {food} is {adjective}.'.format(
...    food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Argumen posisi dan kata kunci dapat digabungkan secara sewenang-wenang:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
other='Georg'))  
The story of Bill, Manfred, and Georg.
```

Jika Anda memiliki string format yang sangat panjang yang tidak ingin Anda pisahkan, alangkah baiknya jika Anda dapat mereferensikan variabel yang akan diformat berdasarkan nama alih-alih berdasarkan posisi. Ini dapat dilakukan hanya dengan melewatkan dict dan menggunakan tanda kurung siku '[]'untuk mengakses kunci.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...    'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Ini juga dapat dilakukan dengan meneruskan tabel sebagai argumen kata kunci dengan notasi '**'.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Ini sangat berguna dalam kombinasi dengan fungsi bawaan vars(), yang mengembalikan kamus yang berisi semua variabel lokal.

Sebagai contoh, baris berikut menghasilkan kumpulan kolom yang tersusun rapi yang memberikan bilangan bulat dan kuadrat serta kubusnya:

```python
>>> for x in range(1, 11):
...    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
1   1   1
2   4   8   
3   9   27
4   16  64
5   25  125
6   36  216 
7   49  343
8   64  512
9   81  729
10  100 1000
```
Untuk gambaran lengkap tentang pemformatan string dengan str.format(), lihat Memformat Sintaks String .

### 7.1.3 Manual String Formatting
Berikut tabel kotak dan kubus yang sama, diformat secara manual :

```python
>>> for x in range(1, 11):
...    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...    # Note use of 'end' on previous line
...    print(repr(x*x*x).rjust(4))
...
1   1   1
2   4   8
3   9   27
4   16  64
5   25  125
6   36  216
7   49  343
8   64  512
9   81  729
10  100 1000
```
(Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan dengan cara print()kerjanya: selalu menambahkan spasi di antara argumennya.)

Metode str.rjust()objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. Ada metode serupa str.ljust()dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda, tetapi itu biasanya lebih baik daripada alternatifnya, yang berbohong tentang nilai. (Jika Anda benar-benar menginginkan pemotongan, Anda selalu dapat menambahkan operasi irisan, seperti pada x.ljust(n)[:n].)

Ada metode lain, str.zfill(), yang mengisi string numerik di sebelah kiri dengan nol. Ia mengerti tentang tanda plus dan minus:

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4 Old string formatting
Operator % (modulo) juga dapat digunakan untuk pemformatan string. Mengingat , contoh di diganti dengan nol atau lebih elemen dari . Operasi ini biasa disebut dengan interpolasi string. Sebagai contoh:'string' % values%stringvalues

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

Informasi lebih lanjut dapat ditemukan di bagian Format String gaya printf.

## 7.2 Reading and Writting Files
open() mengembalikan objek file , dan paling sering digunakan dengan dua argumen: .open(filename, mode)

```python
f = open('workfile', 'w')
```
Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan. mode bisa 'r'ketika file hanya akan dibaca, 'w' untuk hanya menulis (file yang ada dengan nama yang sama akan dihapus), dan 'a'membuka file untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke akhir. 'r+'membuka file untuk membaca dan menulis. Argumen mode adalah opsional; 'r'akan diasumsikan jika dihilangkan.

Biasanya, file dibuka dalam mode teks , artinya, Anda membaca dan menulis string dari dan ke file, yang dikodekan dalam pengkodean tertentu. Jika penyandian tidak ditentukan, defaultnya adalah bergantung pada platform (lihat open()). 'b'ditambahkan ke mode membuka file dalam mode biner : sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak berisi teks.

Dalam mode teks, default saat membaca adalah mengonversi akhiran baris khusus platform ( \npada Unix, \r\npada Windows) menjadi hanya \n. Saat menulis dalam mode teks, defaultnya adalah mengonversi kemunculan \nkembali ke akhir baris khusus platform. Modifikasi di balik layar untuk file data ini baik untuk file teks, tetapi akan merusak data biner seperti itu di JPEGatau EXEfile. Berhati-hatilah untuk menggunakan mode biner saat membaca dan menulis file tersebut.

Ini adalah praktik yang baik untuk menggunakan withkata kunci ketika berhadapan dengan objek file. Keuntungannya adalah file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika pengecualian muncul di beberapa titik. Menggunakan withjuga jauh lebih pendek daripada menulis yang setara try- finallyblok:

```python
>>> with open('workfile') as f:
...    read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

Jika Anda tidak menggunakan withkata kunci, maka Anda harus menelepon f.close()untuk menutup file dan segera membebaskan semua sumber daya sistem yang digunakan olehnya.

Peringatan Memanggil f.write()tanpa menggunakan withkata kunci atau panggilan f.close() dapat mengakibatkan argumen f.write()tidak sepenuhnya ditulis ke disk, bahkan jika program berhasil keluar.

Setelah objek file ditutup, baik dengan withpernyataan atau dengan memanggil f.close(), upaya untuk menggunakan objek file secara otomatis akan gagal.
```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: I/0 operation on closed file.
```

### 7.2.1 Methods of File Object
Contoh lainnya di bagian ini akan mengasumsikan bahwa objek file yang dipanggil ftelah dibuat.

Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file dua kali lebih besar dari memori mesin Anda. Jika tidak, paling banyak karakter ukuran (dalam mode teks) atau ukuran byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read()akan mengembalikan string kosong ( '').

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```
f.readline() membaca satu baris dari file; karakter baris baru ( \n) ditinggalkan di akhir string, dan hanya dihilangkan pada baris terakhir file jika file tidak diakhiri dengan baris baru. Ini membuat nilai pengembalian tidak ambigu; jika f.readline()mengembalikan string kosong, akhir file telah tercapai, sedangkan baris kosong diwakili oleh '\n', string yang hanya berisi satu baris baru.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, Anda dapat mengulang objek file. Ini hemat memori, cepat, dan mengarah ke kode sederhana:

```python
>>> for line in f:
...    print(line, end='')
...
This is the first line of the file.
Second line of the file
```

Jika Anda ingin membaca semua baris file dalam daftar, Anda juga dapat menggunakan list(f)atau f.readlines().

f.write(string)menulis isi string ke file, mengembalikan jumlah karakter yang ditulis.

```python
f.write('This is a test\n')
15
```

Jenis objek lain perlu dikonversi – baik menjadi string (dalam mode teks) atau objek byte (dalam mode biner) – sebelum menulisnya:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

f.tell()mengembalikan bilangan bulat yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file saat dalam mode biner dan angka buram saat dalam mode teks.

Untuk mengubah posisi objek file, gunakan . Posisi dihitung dari penambahan offset ke titik referensi; titik referensi dipilih oleh argumen where . Nilai dari mana 0 mengukur dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. mana dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.f.seek(offset, whence)

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

Dalam file teks (yang dibuka tanpa bstring dalam mode), hanya pencarian relatif ke awal file yang diizinkan (pengecualian mencari ke akhir file dengan ) dan satu-satunya nilai offset yang valid adalah yang dikembalikan dari , atau nol. Nilai offset lainnya menghasilkan perilaku yang tidak terdefinisi.seek(0, 2)f.tell()

Objek file memiliki beberapa metode tambahan, seperti isatty()dan truncate()yang lebih jarang digunakan; lihat Referensi Perpustakaan untuk panduan lengkap tentang objek file.

### 7.2.2 Saving structured data with json
String dapat dengan mudah ditulis dan dibaca dari sebuah file. Angka membutuhkan sedikit lebih banyak usaha, karena read()metode ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil seperti string '123' dan mengembalikan nilai numeriknya 123. Saat Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar bersarang dan kamus, parsing dan serialisasi dengan tangan menjadi rumit.

Daripada membuat pengguna terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan Anda untuk menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation) . Modul standar yang dipanggil jsondapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serialisasi . Merekonstruksi data dari representasi string disebut deserializing . Antara serialisasi dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.

Catatan Format JSON biasanya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Banyak programmer sudah mengenalnya, yang menjadikannya pilihan yang baik untuk interoperabilitas.

Jika Anda memiliki object x, Anda dapat melihat representasi string JSON dengan sebaris kode sederhana:

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Varian lain dari dumps()fungsi, yang disebut dump(), hanya membuat serial objek ke file teks . Jadi jika objek ffile teks dibuka untuk ditulis, kita bisa melakukan ini:

```python
>>> json.dump(x, f)
```

Untuk memecahkan kode objek lagi, jika fadalah objek file teks yang telah dibuka untuk dibaca:
```python
>>> x = json.load(f)3
```

Teknik serialisasi sederhana ini dapat menangani daftar dan kamus, tetapi membuat serialisasi instance kelas arbitrer di JSON membutuhkan sedikit usaha ekstra. Referensi untuk jsonmodul berisi penjelasan tentang ini.