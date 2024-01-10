import matplotlib.pyplot as plt
import numpy as np
import os 

os.system('clear')

"""
MENGATUR GRAFIK MENJADI LEBIH INDAH SEHINGGA LEBIH INFORMATIF 
"""

x = np.arange(1,20,0.5)
y = x**2

# MERUBAH UKURAN & MERUBAH KETAJAMAN :

# VERSI PERTAMA : 
fig = plt.figure(figsize=(5.5,3.5), dpi=200, facecolor='silver') # figsize UNTUK MENENTUKAN UKURAN FIGURE YAITU MEMILIKI 2 PARAMETER YAITU TINGGI & LEBAR, dpi UNTUK UNTUK MEENTUKAN RESOLUSI ATAU KETAJAMAN, facecolor UNUTK MENAMBAHKAN WARNA BACKGROUND
axes = fig.add_axes((0.2,0.2,0.6,0.6))
axes.plot(x,y, color = 'red')

plt.show()

# VERSI KEDUA :
fig2,axes2 = plt.subplots(2,1, figsize = (5.5,4.5), dpi = 100, facecolor = 'silver')

# UNTUK PLOT PERTAMA :
axes2[0].plot(x,y, color = 'red')
axes2[0].set_xlabel('Sumbu X')
axes2[0].set_ylabel('Sumbu Y')

# UNTUK PLOT KEDUA :
axes2[1].plot(y,x, color = 'blue')
axes2[1].set_xlabel('Sumbu X')
axes2[1].set_ylabel('Sumbu Y')

plt.tight_layout()

plt.show()

# MENAMBAHKAN SEBUAH FUNGSI LEGENDA ATAU KETERANGAN DALAM SEBUAH GRAFIK
fig3 = plt.figure(dpi=100, facecolor='grey')
axes3 = fig3.add_axes((0.2,0.2,0.7,0.6))

axes3.set_title('Data Publikasi Jurnal Tahun 2023')
axes3.plot(x,y, color = 'blue', label = 'Komunikasi', lw = 1, ls = '-') # lw = LINE WIDHT ATAU KETEBALAN GARIS PLOT, ls = LINE STYLE ATAU MODEL GARIS YANG DIGUNAKAN
axes3.plot(x,x**3, color = 'red', label = 'Hukum',lw = 1, ls = '-.') # MASIH BANYAK LAGI FUNGSI SELAIN ls DAN lw, ADA JUGA FUNGSI MARKER YAITU : MFC = MarkerFaceColor , MEC = MarkerEdgeColor, MEW = MarkerEdgeWidth, SILAHKAN DI ULIK SENDRI
axes3.plot(x,x**4, color = 'green', label = 'Teknik',lw = 1, ls = '--')

axes3.set_xlim(0,15.0) # FUNGSI INI DIGUNAKAN JIKA KITA INGIN MENAMPILKAN DATA MINIMAL YAITU UNTUK SUMBU X HANYA DITAMPPILKAN DARI DATA 0 - 15.0
axes3.set_ylim(0,10000) # FUNGSI INI DIGUNAKAN JIKA KITA INGIN MENAMPILKAN DATA MINIMAL YAITU UNTUK SUMBU Y HANYA DITAMPPILKAN DARI DATA 0 - 10000

axes3.legend(loc=(0.1,0.7)) # FUNGSI legend(0.1,0.7) UNTUK MENAMBAHKAN KETERANGAN PADA SEBUAH GRAFIK DENGAN PARAMETER loc UNTUK MENENTUKAN LETAK SECARA SEPSIFIK 
axes3.grid(True) # MENAMBAHKAN GRID PADA PLOT

plt.show()