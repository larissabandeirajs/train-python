# from random import randrange, seed
from random import randrange, seed
import matplotlib.pyplot as plt

seed(10)

randrange(0, 11)

notas_matematica = []

for notas in range(8):
    notas_matematica.append([randrange(0,11)])
    
#append pegando o elemento e atribuindo o randrange 

notas_matematica

# import matplotlib.pyplot as plt

x = list(range(1, 9))
y = notas_matematica
plt.plot(x, y)