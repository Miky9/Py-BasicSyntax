# Importujeme základní vykreslovací modul
import matplotlib.pyplot as plt
import matplotlib

# A samozřejmě numpy
import numpy as np

# Občas se hodí i matematika
import math


# Vytvoříme jednoduchá data
# (50 bodů rovnoměrně rozmístěných na úseku -1,5)
x = np.linspace(-1, 5, 8)
y = x ** 2

fig = plt.figure()

# U add_axes musíme zadat, jakou část obrázku zabere čtverec se souřadnicemi
# zleva, odspodu, šířka, výška (v relativních hodnotách 0 až 1)
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Nyní vykreslíme data
print (axes.plot(x, y));

