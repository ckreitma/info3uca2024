# Ejemplo de Polígono simple a partir de lista de puntos
import pygame
import numpy as np
import math
# https://www.geeksforgeeks.org/three-dimensional-plotting-in-python-using-matplotlib/
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


# Ancho y alto teórico (Solo PYGAME)
ancho_teorico = 900
alto_teorico = 900

fig = None
ax = None


def poligono1():
    lp = []
    lp.append((0,10,50,1))
    lp.append((50,100,100,1))
    lp.append((0,200,10,1))
    lp.append((0,10,50,1))
   
    return lp

def dibujar_poligono(lp):
    print(f'Cantidad de puntos: {len(lp)}')
    x = []
    y = []
    z = []
    for i in range(len(lp)):
        x.append(lp[i][0])
        y.append(lp[i][1])
        z.append(lp[i][2])
    ax.plot3D(x,y,z)
    
def proyeccion_paralela_poligono(lp,direccion=[0,0,1]):
    # matriz paralela
    xp,yp,zp = direccion
    if yp:
        xpyp = -xp/yp
    else:
        xpyp = 0
    
    if zp:
        ypzp = -yp/zp
    else:
        ypzp = 0

    mp=[
        [1,         0,          0,          0],
        [0,         1,          0,          0],
        [xpyp,    ypzp,         0,          0],
        [0,         0,          0,          1]
    ]
    lpp = []
    for p in lp:
        lpp.append(np.matmul(p,mp))


    x = []
    y = []
    z = []
    for i in range(len(lpp)):
        x.append(lpp[i][0])
        y.append(lpp[i][1])
        z.append(lpp[i][2])
    ax.plot3D(x,y,z)


# Driver code
if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')    
    dibujar_poligono(poligono1())
    proyeccion_paralela_poligono(poligono1(),direccion=[0,0,1])
    plt.show()
