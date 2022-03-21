# 8. Errors and Exceptions
Sumber : [tutorial python](https://docs.python.org/3/tutorial/errors.html)


Ada dua jenis kesalahan yang dapat dibedakan: kesalahan sintaksis dan pengeculian.

## 8.1. Syntax Errors
Kesalahan sintaks yang dikenal sebagai kesalahan penguraian, kesalahan ini sering dijumpai saat masih belajar Python:

```python
>>> while True print('Hello world')
File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

Kesalahahan disebabkan oleh (atau setidaknya terdeteksi pada) token sebelum panah, pada fungsi print(). Karena titik dua (':') hilang sebelumnya. Nama file dan nomor baris dicetak sehingga kita tahu dimana mencarinya jika input berasal dari skrip. 

## 8.2 Exceptions
Kesalahan yang terdeteksi selama ekskusi disebut pengecualian dan titik fatal tanpa syarat. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti berikut ini:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' +2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Pengecualian datang dalam tipe yang berbeda, dan tipe tersebut dicetak sebagai bagian dari pesan: tipe dalam contoh yaitu ZeroDivisionError, NameError dan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama pengecualian bawaan yang terjadi dan berlaku untuk semua bawaan pengecualian. Tetapi untuk pengguna, pengecualian yang ditentukan tidak harus benar. Identifikasi bawaan merupakan nama pengecualian yang standar. 

Untuk bagian pesan kesalahan sebelumnya, menunjukkan konteks di mana pengecualian itu terjadi dalam bentuk pelacakan balik tumpukan. Yang secara umum berisi baris sumber daftar traceback stack. Namun, tidak dapat menampilkan baris yang dibaca dari input standar nya.

## 8.3 Handling Exceptions
```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops! That was no valid number. Try again...")
...
```

Pernyataan try tersebut berfungsi sebagai berikut:
- Pertama, klausa try (pernyataan antara try dan except kata kunci) dieksekusi.
- Jika tidak ada pengecualian yang terjadi, klausa kecuali dilewati dan eksekusi try pernyataan selesai. 
- Jika pengecualian terjadi selama eksekusi try klausa, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai except kata kunci, klausa kecuali dieksekusi, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali. 
- Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke try pernyataan luar; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas. 

Sebuah try pernyataan mungkin memiliki lebih dari satu kecuali klausa, untuk menentukan penangan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Penangan hanya menangani pengecualian yang terjadi di klausa try yang sesuai, bukan di penangan lain dari try pernyataan yang sama. Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tupel dalam kurung, misalnya :

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

Kelas dalam except klausa komptibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar. Tetapi tidak sebaliknya, klausa pengecualian yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar. Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

```python
>>> class B(Exception):
...     pass
>>>
>>> class C(B):
...     pass
>>>
>>> class D(C):
...    pass
>>>
>>> for cls in [B, C, D]:
...     try:
...         raise cls()
...     except D:
...         print("D")
...    except C:
...        print("C")
...    except B:
...        print("B")
```

Perhatikan bahwa jika klausa kecuali dibalik dengan yang pertama, itu akan dicetak B, B, B - pencocokan pertama klausa kecuali dipicu except B. 

Semua pengecualian mewarisi dari BaseException, sehingga dapat digunakan sebagai karakter pengganti. 

```python
>>> import sys
>>>
>>> try:
...    f = open('myfile.txt')
...    s = f.readline()
...    i = int(s.strip())
>>> except OSError as err:
...    print("OS error: {0}".format(err))
>>> except ValueError:
...    print("Could not convert data to an integer.")
>>> except BaseException as err:
...    print(f"Unexpected {err=}, {type(err)=}")
...    raise
```

Sebagai alternatif, klausa pengecualian terakhir dapat menghilangakn nama pengecualian, namun nilai pengecualian harus diambil dari sys.exc_info()[1].

Pernyataan try memiliki klausa else except opsional, yang berguna untuk menjalankan kode jika klausa try nya tidak muncul eksepsi. Sebagai contoh:

```python
>>> for arg in sys.argv[1:]:
...    try:
...        f = open(arg, 'r')
...    except OSError:
...        print('cannot open', arg)
...    else:
...        print(arg, 'has', len(f.readlines()), 'lines')
...    f.close()
```

Ketika pengecualian terjadi, memungkinkan untuk memiliki nilai yang terkait yang biasa dikenal sebagai argumen pengecualian, yang bergantung pada tipe pengecualian. 

Variabel terikat ke instance pengecualian dengan argumen yang disimpan di instance.args. Instance pengecualian mendefinisikan ___str__() sehingga argumen dapat dicetak secara langsung tanpa harus reference .args. Dapat juga membuat instance pengecualian terlebih dahulu sebelum sebelum menambahkan atribut apapun. 

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika pengecualian memiliki argumen, mereka akan dicetak sebagai bagian terakhir ('detail') dari pesan untuk pengecualian yang tidak ditangani. 

Jika terjadi ekspesi didalam penangan eksepsi maupun dalam fungsi yang dipanggil, maka akan segera di klausa try. Sebagai contoh:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Raising Exceptions
Pernyataan raise digunakan untuk memaksa pengecualian tertentu yang terjadi. Sebagai contoh:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Argumen raise yang menunjukkan pengecualian yang akan diajukan, harus berupa instance pengecualian atau kelas pengecualiannya. Jika melewati kelas pengecualian, secara implisit akan memanggil konstruktornya tanpa argumen:

```python
>>> raise ValueError  # shorthand for 'raise ValueError()'
```

Bentuk raise pernyataan yang lebih sederhana untuk menaikkan kembali pengecualian tanpa perli menanganinya: 

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5. Exception Chaining
Pernyataan raise itu memungkinkan opsional form yang memungkinkan pengecualiann rantai. Sebagai contoh:

```python
>>> # exc must be exception instance or None.
>>> raise RuntimeError from exc
```

Dan ini berguna saat mengubah pengecualian, contohnya:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam except atau finally bagian. Ini dapat di nonaktifkan dengan menggunakan idiom:from None

```python
>>> try:
...    open('database.sqlite')
>>> except OSError:
...    raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

## 8.6. User-defined Exceptions
Kelas pengecualian dapat didefinisikan dapat melakukan apapun yang dilakukan oleh kelas lain. Tetapi biasanya dibuat sederhana, dan seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian. 

Sebagain besar pengecualian didefinisikan dengan nama yang diakhiri dengan "Kesalahan", hampir sama dengan penamaan pengecualian standar.

## 8.7. Defining Clean-up Actions
Pernyataan try memiliki klausa opsional yang digunakan untuk mendefinisikan tindakan pembersihan dalam semua keadaan, sebagai contoh :

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Poin-poin berikut membahas kasus yang lebih kompleks ketika pengecualian terjadi :
- Jika pengecualian terjadi selama eksekusi try klausa, pengecualian dapat ditangani oleh except klausa. Jika eksepsi tidak ditangani oleh except klausa, eksepsi dimunculkan kembali setelah finally klausa dieksekusi.
- Pengecualian dapat terjadi selama eksekusi suatu except atau else klausa. Sekali lagi, pengecualian dinaikkan kembali setelah finally klausa dieksekusi.
- Jika finally klausa mengeksekusi a break, continue atau returnpernyataan, pengecualian tidak dimunculkan kembali.
- Jika try pernyataan mencapai break, continue atau return pernyataan, finally klausa akan dieksekusi tepat sebelum eksekusi break, continue atau return pernyataan.
- Jika finally klausa menyertakan return pernyataan, nilai yang dikembalikan akan menjadi nilai dari pernyataan finally klausa return, bukan nilai dari pernyataan try klausa return.

Sebagai contoh :

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

Contoh yang lebih rumit :

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang dilihat, finally klausa dieksekusi dalam acara apapun. Dibangkitkan TypeError dengan membagi dua string yang tidak ditangani oleh except klausa, karena itu dinaikkan kembali setelah finally klausa dieksekusi. 

## 8.8. Predefined Clean-up Actions
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Contoh berikut yang mencoba membuka dan mencetak isi file ke layar :

```python
>>> for line in open("myfile.txt"):
...    print(line, end="")
```

Masalah dengan kode ini adalah membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Pernyataan with tersebut memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar. 

```python
>>> with open("myfile.txt") as f:
...    for line in f:
...        print(line, end="")
```

Setelah pernyataan dieksekusi, file f selalu ditutup. Objek yang sepeti file, menyediakan tindakan pembersihan yang telah ditentukan sebelumnya akan menunjukkan hal ini dalam dokumentasinya.


