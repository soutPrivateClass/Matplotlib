from matplotlib import pyplot as plt
import numpy as np
import os
os.system("clear")


"""
MATPLOTLIB ADALAH :  SEBUAH LIBRARY DI PYTHON UNTUK MELAKUKAN VISUALISASI DATA
"""

x = [10,20,30,40,50]
y = np.array(x)**2


plt.plot(x,y)
# MEMBERIKAN LABEL PADA GRAFIK :
plt.ylabel('Sumbu Y')
plt.xlabel('Sumbu X')
plt.title('Grafik')    
plt.show()

# MEMBUAT DUA PLOT SEKALIGUS :
plt.subplot(121) # 121 UNTUK MENENTUKAN UKURAN 1 BARIS 2 KOLOM & 1 ADALAH KARENA PLOT PERTAMA
plt.plot(x,y, color = 'Red') # COLOR UNTUK MEMBERIKAN WARNA PADA GARIS GRAFIK


plt.subplot(122) # 122 UNTUK MENENTUKAN UKURAN 1 BARIS 2 KOLOM & 2 ADALAH KARENA PLOT KEDUA
plt.plot(y,x, color = 'Blue')

plt.tight_layout() # AGAR LAYOUT TERLIHAT RAPI DANN TIDAK BERANTAKAN
plt.show()
