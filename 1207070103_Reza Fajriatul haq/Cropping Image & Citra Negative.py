import matplotlib.pyplot as plt  # Modul untuk membuat plot dan visualisasi data
import cv2  # Library OpenCV untuk operasi pengolahan citra
#%matplotlib inline  # Menggunakan mode inline untuk menampilkan plot secara langsung di notebook

from skimage import data  # Modul dari scikit-image untuk mengakses dataset citra
from skimage.io import imread  # Fungsi untuk membaca citra dari file
from skimage.color import rgb2gray  # Fungsi untuk mengubah citra RGB menjadi grayscale
from skimage.util import invert  # Fungsi untuk melakukan inversi citra

import numpy as np  # Library untuk operasi numerik pada array


#percobaan 1 crop image

img = cv2.imread('zee.jpeg')  # Membaca citra 'zee.jpeg' menggunakan OpenCV
img2 = cv2.imread('Ronaldo.jpeg')  # Membaca citra 'Ronaldo.jpeg' menggunakan OpenCV

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Mengubah mode warna citra 'zee.jpeg' menjadi RGB
RGB_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)  # Mengubah mode warna citra 'Ronaldo.jpeg' menjadi RGB

zeeCropped = RGB_img.copy()  # Membuat salinan citra 'zee.jpeg'
zeeCropped = zeeCropped[0:256, 64:320]  # Memotong citra 'zee.jpeg' pada area yang ditentukan

RonaldoCropped = RGB_img2.copy()  # Membuat salinan citra 'Ronaldo.jpeg'
RonaldoCropped = RonaldoCropped[64:256, 128:320]  # Memotong citra 'Ronaldo.jpeg' pada area yang ditentukan

print('zee Ori Shape : ', RGB_img.shape)  # Menampilkan dimensi citra asli 'zee.jpeg'
print('zee Crop Shape : ', zeeCropped.shape)  # Menampilkan dimensi citra hasil pemotongan 'zee.jpeg'

print('Ronaldo Ori Shape : ', RGB_img2.shape)  # Menampilkan dimensi citra asli 'Ronaldo.jpeg'
print('Ronaldo Crop Shape : ', RonaldoCropped.shape)  # Menampilkan dimensi citra hasil pemotongan 'Ronaldo.jpeg'


fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Membuat subplot dengan ukuran 2x2 dan ukuran total 12x12
ax = axes.ravel()  # Meratakan array subplot menjadi array 1 dimensi

ax[0].imshow(RGB_img)  # Menampilkan citra input pertama
ax[0].set_title("Citra Input 1")  # Menambahkan judul pada citra input pertama

ax[1].imshow(RGB_img2, cmap='gray')  # Menampilkan citra input kedua
ax[1].set_title('Citra Input 2')  # Menambahkan judul pada citra input kedua

ax[2].imshow(zeeCropped)  # Menampilkan citra output pertama (hasil pemotongan)
ax[2].set_title("Citra Output 1")  # Menambahkan judul pada citra output pertama

ax[3].imshow(RonaldoCropped, cmap='gray')  # Menampilkan citra output kedua (hasil pemotongan)
ax[3].set_title('Citra Output 2')  # Menambahkan judul pada citra output kedua

plt.show()  # Menampilkan plot dengan subplot


#Percobaan 2 - Citra Negative
inv = invert(zeeCropped)  # Membalik citra input menggunakan fungsi invert dari skimage.util

print('Shape Input : ', zeeCropped.shape)  # Menampilkan dimensi citra input
print('Shape Output : ', inv.shape)  # Menampilkan dimensi citra output (gambar terbalik)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Membuat subplot dengan ukuran 2x2 dan ukuran total 12x12
ax = axes.ravel()  # Meratakan array subplot menjadi array 1 dimensi

ax[0].imshow(zeeCropped)  # Menampilkan citra input pada subplot indeks 0
ax[0].set_title("Citra Input")  # Menambahkan judul "Citra Input" pada subplot indeks 0

ax[1].hist(zeeCropped.ravel(), bins=256)  # Menampilkan histogram citra input pada subplot indeks 1
ax[1].set_title('Histogram Input')  # Menambahkan judul "Histogram Input" pada subplot indeks 1

ax[2].imshow(inv)  # Menampilkan citra output (gambar terbalik) pada subplot indeks 2
ax[2].set_title('Citra Output (Inverted Image)')  # Menambahkan judul "Citra Output (Inverted Image)" pada subplot indeks 2

ax[3].hist(inv.ravel(), bins=256)  # Menampilkan histogram citra output pada subplot indeks 3
ax[3].set_title('Histogram Output')  # Menambahkan judul "Histogram Output" pada subplot indeks 3

plt.show()  # Menampilkan plot dengan subplot


copyCamera = RonaldoCropped.copy().astype(float)  # Membuat salinan citra input dengan tipe data float

shape = copyCamera.shape  # Mendapatkan dimensi citra input
output1 = np.empty(shape)  # Membuat array kosong dengan dimensi yang sama dengan citra input

for baris in range(0, shape[0]-1):  # Loop melalui baris citra input
    for kolom in range(0, shape[1]-1):  # Loop melalui kolom citra input
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] / 192  # Memperoleh nilai kecerahan baru dengan membagi nilai piksel dengan 192

fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Membuat subplot dengan ukuran 2x2 dan ukuran total 12x12
ax = axes.ravel()  # Meratakan array subplot menjadi array 1 dimensi

ax[0].imshow(RonaldoCropped, cmap='gray')  # Menampilkan citra input pada subplot indeks 0
ax[0].set_title("Citra Input")  # Menambahkan judul "Citra Input" pada subplot indeks 0

ax[1].hist(RonaldoCropped.ravel(), bins=256)  # Menampilkan histogram citra input pada subplot indeks 1
ax[1].set_title('Histogram Input')  # Menambahkan judul "Histogram Input" pada subplot indeks 1

ax[2].imshow(output1, cmap='gray')  # Menampilkan citra output (kecerahan citra) pada subplot indeks 2
ax[2].set_title('Citra Output (Brightness)')  # Menambahkan judul "Citra Output (Brightness)" pada subplot indeks 2

ax[3].hist(output1.ravel(), bins=192)  # Menampilkan histogram citra output pada subplot indeks 3
ax[3].set_title('Histogram Output')  # Menambahkan judul "Histogram Output" pada subplot indeks 3

print(output1.shape)  # Menampilkan dimensi citra output
plt.show()  # Menampilkan plot dengan subplot
