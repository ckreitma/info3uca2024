from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

altura, ancho = 800, 800

ojox, ojoy, ojoz = 0.8, 0.8, 2


def cara(vertices, color):
    glColor(color[0], color[1], color[2], 1)
    glBegin(GL_QUADS)
    for v in vertices:
        glVertex3fv(v)
    glEnd()


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

    Cube()


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


def Cube():
    vertices = []
    ancho = 0.3
    z = 0
    # Inferior izquierdo
    vertices.append((0, 0, z))
    # Inferior derecho
    vertices.append((ancho, 0, z))
    # Superior derecho
    vertices.append((ancho, ancho, z))
    # Superior izquierdo
    vertices.append((0, ancho, z))

    square = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    )

    # ejes()

    # Cara izquierda #rosada
    glPushMatrix()
    glRotate(-90, 0, 1, 0)
    cara(vertices, (0.8, 0.2, 0.5))
    glPopMatrix()

    # Cara inferior #amarillo
    glPushMatrix()
    glRotate(90, 1, 0, 0)
    cara(vertices, (0.7, 0.7, 0.1))
    glPopMatrix()

    # Cara derecha #celeste
    glPushMatrix()
    glTranslatef(ancho, 0, 0)
    glRotate(-90, 0, 1, 0)
    cara(vertices, (0.2, 0.4, 0.8))
    glPopMatrix()

    # Cara frontal #verde
    glPushMatrix()
    glTranslatef(0, 0, ancho)
    # cara(vertices, (0.1, 0.7, 0.2))
    glPopMatrix()

    # Cara superior #lila
    glPushMatrix()
    glTranslatef(0, ancho, 0)
    glRotate(90, 1, 0, 0)
    cara(vertices, (0.3, 0.1, 0.3))
    glPopMatrix()

    # Cara trasera #gris
    cara(vertices, (0.4, 0.4, 0.4))

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
