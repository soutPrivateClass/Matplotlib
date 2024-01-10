import matplotlib.pyplot as plt
import numpy as np
import os

os.system("clear")

"""
MEMBUAT PLOT DENGAN OBJEK MENGGUNAKAN FUNGSI FIGURE DAN AXES
"""


# VERSI 1 : MEMBUAT ATAU MENAMPILKAN SATU MODEL PLOT
x = np.arange(0,20,0.5)
y = x**2

fig = plt.figure() # MEMBUAT PLOT BESAR KOSONG YANG SIAP UNTUK DIISI
axes = fig.add_axes((0.1,0.1,0.8,0.8)) # MEMBUAT PLOT KECIL KOSONG YANG SIAP UNTUK DIISI
axes.plot(x,y, color='red')
axes.set_ylabel('Sumbu Y') # KHUSUS UNTUK OBJEK SEDIKIT MENAMBAHKAN SET_ UNTUK MENAMBAHKAN JUDUL
axes.set_xlabel('Sumbu X') # KHUSUS UNTUK OBJEK SEDIKIT MENAMBAHKAN SET_ UNTUK MENAMBAHKAN JUDUL
axes.set_title('Judul Grafik')

plt.show()


# VERSI 2 : MEMBUAT ATAU MENAMPILKAN DUA MODEL PLOT DIDALAM PLOT 
fig2 = plt.figure()

# PLOT PERTAMA :
axes1 = fig2.add_axes((0.1,0.1,0.8,0.8))
axes1.plot(x,y, color = 'red')
axes1.set_ylabel('Sumbu Y')
axes1.set_xlabel('Sumbu X')
axes1.set_title('Data')

# PLOT KEDUA YANG ADA DIDALAM PLOT PERTAMA :
axes2 = fig2.add_axes((0.2,0.5,0.3,0.3))
axes2.plot(y,x, color = 'blue')
axes2.set_ylabel('Sumbu Y')
axes2.set_xlabel('Sumbu X')
axes2.set_title('Sub Data')

plt.show()

# VERSI 2 : MEMBUAT ATAU MENAMPILKAN BANYAK PLOT DALAM SATU PLOT 
fig,axes = plt.subplots(1,2) # CARA INI JUGA BISA DIGUNAKAN DAN LEBIH SIMPEL UNTUK MEMBUAT PLOT DAAM PLOT, 1,2 ARTINYA AKAN ADA 2 MODEL PLOT DALAM SATU PLOT 

# PLOT UNUTK AXES YANG PETAMA :
axes[0].plot(x,y, color = 'red')
axes[0].set_xlabel('Sumbu X')
axes[0].set_ylabel('Sumbu Y')
axes[0].set_title('Grafik 1')

# PLOT UNUTK AXES YANG KEDUA :
axes[1].plot(y,x, color = 'blue')
axes[1].set_xlabel('Sumbu X')
axes[1].set_ylabel('Sumbu Y')
axes[1].set_title('Grafik 2')

plt.tight_layout()
plt.show()