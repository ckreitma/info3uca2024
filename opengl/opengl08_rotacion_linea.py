from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

altura, ancho = 800, 800

ojox, ojoy, ojoz = 0.8, 0.8, 2


def display():
    global ojox, ojoy, ojoz
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(35, altura/ancho, 0.1, 10.0)

    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

    # Inicializar la matriz.
    glLoadIdentity()

    # Desde, Hacia, Dirección arriba
    ojox += 0.2
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    ejes()
    glColor(0.3, 0.1, 0.9, 1)
    lado = 0.3
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0)
    glVertex3f(lado, 0, 0)
    glVertex3f(lado, lado, 0)
    glVertex3f(0, lado, 0)
    glEnd()

    # Rotación respecto a una recta arbitraria
    x0, y0, z0 = 0.4, 0, 0
    x1, y1, z1 = 0.6, 0.4, 0
    angulo1 = 80
    angulo2 = 30
    A = x1 - x0
    B = y1 - y0
    C = z1 - z0

    V = math.sqrt(B**2 + C**2)
    N = math.sqrt(A**2 + B**2 + C**2)

    rot_x = math.degrees(math.asin(B/V))
    rot_y = math.degrees(math.acos(B/N))
    print(f'Rotx={rot_x} rot_y:{rot_y}')

    # glPushMatrix()
    # glColor(0.3, 0.6, 0.6)
    # glTranslatef(x1, y1, z1)
    # glRotate(-rot_x, 1, 0, 0)
    # glRotate(-rot_y, 0, 1, 0)
    # glRotatef(angulo1, 0, 0, 1)
    # glRotate(rot_y, 0, 1, 0)
    # glRotate(rot_x, 1, 0, 0)
    # glTranslatef(-x1, -y1, -z1)
    # glBegin(GL_QUADS)
    # glVertex3f(0, 0, 0)
    # glVertex3f(lado, 0, 0)
    # glVertex3f(lado, lado, 0)
    # glVertex3f(0, lado, 0)
    # glEnd()
    # glPopMatrix()

    glPushMatrix()
    glColor(0.8, 0.1, 0.1)
    glTranslatef(x1, y1, z1)
    glRotate(angulo1, x1-x0, y1-y0, z1-z0)
    glTranslatef(-x1, -y1, -z1)
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0)
    glVertex3f(lado, 0, 0)
    glVertex3f(lado, lado, 0)
    glVertex3f(0, lado, 0)
    glEnd()
    glPopMatrix()
    glFlush()


def ejes():
    # Eje x
    largo = 2
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(largo, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, largo, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, largo)

    glEnd()

    glFlush()


def buttons(key, x, y):
    global ojox
    print(f'key={key}')
    if key == b'a':
        ojox += 0.1


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glDepthFunc(GL_LESS)
    glutInitWindowSize(altura, ancho)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow("Cubo 3D con rotación de caras")
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()


main()
