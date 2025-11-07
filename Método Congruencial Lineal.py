# Método  Congruencia Lineal
a = 1664525
c = 1013904223
m = 2**32
x = 12345  # Semilla

for i in range(10):
    x = (a * x + c) % m
    print(x / m)  # Convertir a [0, 1)