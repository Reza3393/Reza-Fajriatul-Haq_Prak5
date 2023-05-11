#import liblalry
import numpy as np # mengimpor library numpy dengan alias "np"
import cv2 # mengimpor library OpenCV
import matplotlib.pyplot as plt # mengimpor library pyplot dari matplotlib dengan alias "plt"

img = cv2.imread("Ronaldo.jpeg") # membaca gambar "Ronaldo.jpeg" menggunakan OpenCV dan menyimpannya dalam variabel "img".

img_height = img.shape[0] # mengambil dimensi tinggi gambar (jumlah piksel vertikal) dan menyimpannya dalam variabel "img_height".
img_width = img.shape[1] # mengambil dimensi lebar gambar (jumlah piksel horizontal) dan menyimpannya dalam variabel "img_width".
img_channel = img.shape[2] # mengambil jumlah saluran warna pada gambar (misalnya, 3 saluran untuk gambar warna RGB) dan menyimpannya dalam variabel "img_channel".
img_type = img.dtype # mengambil jenis data gambar

#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100

img_brightness = np.zeros(img.shape, dtype=np.uint8) # membuat array numpy dengan ukuran yang sama dengan gambar asli 

def brighter(nilai): # mendefinisikan fungsi "brighter" dengan satu parameter "nilai"
    for y in range(0, img_height): # baris ini memulai pengulangan untuk setiap baris pada gambar.
        for x in range(0, img_width): # baris ini memulai pengulangan untuk setiap piksel pada baris saat ini.
            red = img[y][x][0] # baris ini mengambil nilai komponen warna merah dari piksel saat ini.
            green = img[y][x][1] # baris ini mengambil nilai komponen warna hijau dari piksel saat ini.
            blue = img[y][x][2] # baris ini mengambil nilai komponen warna biru dari piksel saat ini.
            gray = (int(red) + int(green) + int(blue)) / 3 # baris ini menghitung nilai rata-rata dari ketiga komponen warna untuk mendapatkan nilai kecerahan (grayscale) piksel saat ini.
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray) # menyimpan nilai kecerahan baru pada array numpy "img_brightness" untuk piksel saat ini.

brighter(-100) # memanggil fungsi "brighter" dengan nilai parameter -100 untuk mengurangi kecerahan gambar.
plt.imshow(img_brightness) # menampilkan gambar yang telah dimanipulasi kecerahannya dengan matplotlib.
plt.title("Brightness -100") # menambahkan judul pada gambar yang ditampilkan.
plt.show() # baris ini menampilkan gambar

brighter(100)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()

#Menampilkan RGB Brignest dengan nilai brightness -100 dan 100

img_rgbbrighter = np.zeros(img.shape, dtype= np.uint8) # membuat array numpy dengan ukuran yang sama dengan gambar asli 

def rgbbrighter(nilai): # mendefinisikan fungsi "brighter" dengan satu parameter "nilai". Fungsi ini akan digunakan untuk meningkatkan atau mengurangi kecerahan gambar.
    for y in range (0, img_height): # memulai pengulangan untuk setiap baris pada gambar.
        for x in range (0, img_width): #  memulai pengulangan untuk setiap piksel pada baris saat ini.
            red = img[y][x][0] # mengambil nilai komponen warna merah dari piksel saat ini.
            red += nilai 
            if red > 255: 
                red = 255
            if red <0:
                red = 0
            green = img[y][x][1] # baris ini mengambil nilai komponen warna hijau dari piksel saat ini.
            green += nilai
            if green > 255:
                green = 255
            if green <0:
                green = 0
            blue = img[y][x][2] # mengambil nilai komponen warna biru dari piksel saat ini.
            blue += nilai
            if blue > 255:
                blue = 255
            if blue <0:
                blue = 0
            img_rgbbrighter [y][x] = (red,green,blue)



rgbbrighter(-100)
plt.imshow(img_rgbbrighter)
plt.title("rgbbrighter -100")
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbrighter)
plt.title("rgbbrighter 100")
plt.show()

#Menampilkan  Contrass

# Buat array yang diisi dengan nol dengan bentuk yang sama dengan gambar input
img_contrass = np.zeros(img.shape, dtype=np.uint8)

# Fungsi untuk mengatur kontras
def kontras(nilai):
    # Melakukan perulangan melalui setiap piksel dalam gambar
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Ekstrak saluran warna merah, hijau, dan biru
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            # Konversi piksel menjadi skala keabuan
            gray = (int(red) + int(green) + int(blue)) / 3
            # Sesuaikan nilai skala keabuan berdasarkan parameter masukan
            gray += nilai
            # Batasi nilai skala keabuan antara 0 dan 255
            if gray > 255:
                gray = 255
            # Tetapkan nilai piksel pada gambar output
            img_contrass[y][x] = (gray, gray, gray)

# Sesuaikan kontras gambar input dengan jumlah yang berbeda dan tampilkan hasilnya
kontras(2)
plt.imshow(img_contrass)
plt.title("Kontras 2")
plt.show()

kontras(3)
plt.imshow(img_contrass)
plt.title("Kontras 3")
plt.show()

# Buat array yang diisi dengan nol dengan bentuk yang sama dengan gambar input
img_rgbcontrass = np.zeros(img.shape, dtype=np.uint8)

# Fungsi untuk mengatur kontras pada saluran warna RGB
def rgbcontrass(nilai):
    # Melakukan perulangan melalui setiap piksel dalam gambar
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Ekstrak nilai saluran warna merah
            red = img[y][x][0]
            red += nilai
            # Batasi nilai saluran warna merah antara 0 dan 255
            if red > 255:
                red = 255
            # Ekstrak nilai saluran warna hijau
            green = img[y][x][1]
            green += nilai
            # Batasi nilai saluran warna hijau antara 0 dan 255
            if green > 255:
                green = 255
            # Ekstrak nilai saluran warna biru
            blue = img[y][x][2]
            blue += nilai
            # Batasi nilai saluran warna biru antara 0 dan 255
            if blue > 255:
                blue = 255
            # Tetapkan nilai piksel pada gambar output
            img_rgbcontrass[y][x] = (red, green, blue)

# Sesuaikan kontras pada saluran warna RGB gambar input dengan jumlah yang berbeda dan tampilkan hasilnya
rgbcontrass(20)
plt.imshow(img_rgbcontrass)
plt.title("Kontras RGB 20")
plt.show()

rgbcontrass(100)
plt.imshow(img_rgbcontrass)
plt.title("Kontras RGB 100")
plt.show()

#contast autolevel
img_autocontrass = np.zeros(img.shape, dtype= np.uint8)  # Membuat numpy array dengan ukuran yang sama dengan gambar asli untuk menampung gambar hasil

def autocontrass():  # Membuat fungsi autocontrass
    xmax = 300  # Inisialisasi nilai maksimum
    xmin = 0  # Inisialisasi nilai minimum
    d = 0  # Inisialisasi range nilai
    for y in range(0, img_height):  # Looping untuk setiap pixel pada sumbu y
        for x in range(0, img_width):  # Looping untuk setiap pixel pada sumbu x
            red = img[y][x][0]  # Mendapatkan nilai red dari pixel
            green = img[y][x][1]  # Mendapatkan nilai green dari pixel
            blue = img[y][x][2]  # Mendapatkan nilai blue dari pixel
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung nilai gray dari rata-rata rgb
            if gray < xmax:  # Jika nilai gray lebih kecil dari xmax, maka xmax diupdate
                xmax = gray
            if gray > xmin:  # Jika nilai gray lebih besar dari xmin, maka xmin diupdate
                xmin = gray
    d = xmin-xmax  # Menghitung range nilai
    for y in range(0, img_height):  # Looping untuk setiap pixel pada sumbu y
        for x in range(0, img_width):  # Looping untuk setiap pixel pada sumbu x
            red = img[y][x][0]  # Mendapatkan nilai red dari pixel
            green = img[y][x][1]  # Mendapatkan nilai green dari pixel
            blue = img[y][x][2]  # Mendapatkan nilai blue dari pixel
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung nilai gray dari rata-rata rgb
            gray = int(float(255/d) * (gray-xmax))  # Menghitung nilai gray baru setelah di-normalisasi
            img_autocontrass [y][x] = (gray, gray, gray)  # Menyimpan nilai pixel ke dalam array img_autocontrass dengan gray yang baru

autocontrass()  # Memanggil fungsi autocontrass
plt.imshow(img_autocontrass)  # Menampilkan gambar hasil
plt.title("Contrass Autolevel")  # Memberi judul pada gambar hasil
plt.show()  # Menampilkan gambar hasil ke dalam plot matplotlib













