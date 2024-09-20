from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
"""
Para inteacción.
x,X
y,Y     "Corresponden al ojo
z,Z

i,I
o,O     Corresponden al look_at
p,P

n entre 0 y 5 Inhabilitar caras

w e r t
"""

pantallax, pantallay = 800, 800

ojox, ojoy, ojoz = 0.8, 0.8, 3
look_x, look_y, look_z = 0.0, 0.0, 0.0
rotacion_general = [0.4, 1, 1, 0]
lado = 0.3
caras = [True, True, True, True, True, True]


def cara(vertices, color):
    glColor(color[0], color[1], color[2], 1)
    glBegin(GL_QUADS)
    for v in vertices:
        glVertex3fv(v)
    glEnd()


def display():
    global ojox, ojoy, ojoz, look_x, look_y, look_z
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(35, pantallax / pantallay, 0.1, 10.0)

    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

    # Inicializar la matriz.
    glLoadIdentity()

    # Desde, Hacia, Dirección arriba
    print(f'ojox={ojox}')
    gluLookAt(ojox, ojoy, ojoz, look_x, look_y, look_z, 0.0, 1.0, 0.0)

    ejes()

    # Aplicamos la rotación general
    glPushMatrix()
    glRotate(*rotacion_general)
    glTranslate(0.2, 0.3, -0.4)
    Cube()
    glPopMatrix()


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

    # Ahora la linea de rotación
    glColor3f(1, 1, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(rotacion_general[1], rotacion_general[2], rotacion_general[3])

    glEnd()


def Cube():
    vertices = []
    global lado
    global caras
    z = 0
    # Inferior izquierdo
    vertices.append((0, 0, z))
    # Inferior derecho
    vertices.append((lado, 0, z))
    # Superior derecho
    vertices.append((lado, lado, z))
    # Superior izquierdo
    vertices.append((0, lado, z))

    square = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    )

    # Cara izquierda #rosada
    if caras[0]:
        glPushMatrix()
        glRotate(-90, 0, 1, 0)
        cara(vertices, (0.8, 0.2, 0.5))
        glPopMatrix()

    # # Cara inferior #amarillo
    if caras[1]:
        glPushMatrix()
        glRotate(90, 1, 0, 0)
        cara(vertices, (0.7, 0.7, 0.1))
        glPopMatrix()

    # # Cara derecha #celeste
    if caras[2]:
        glPushMatrix()
        glTranslatef(lado, 0, 0)
        glRotate(-90, 0, 1, 0)
        cara(vertices, (0.2, 0.4, 0.8))
        glPopMatrix()

    # # Cara frontal #verde
    if caras[3]:
        glPushMatrix()
        glTranslatef(0, 0, lado)
        cara(vertices, (0.1, 0.7, 0.2))
        glPopMatrix()

    # # Cara superior #lila
    if caras[4]:
        glPushMatrix()
        glTranslatef(0, lado, 0)
        glRotate(90, 1, 0, 0)
        cara(vertices, (0.3, 0.1, 0.3))
        glPopMatrix()

    # # Cara trasera #gris
    if caras[5]:
        cara(vertices, (0.4, 0.4, 0.4))

    glFlush()


def buttons(key, x, y):
    global ojox, ojoy, ojoz
    global look_x, look_y, look_z
    global rotacion_general
    delta = 0.1
    print(f'key={key} x={x} y={y}')
    # Ojo
    if key == b'x':
        ojox += delta
    if key == b'X':
        ojox -= delta
    if key == b'y':
        ojoy += delta
    if key == b'Y':
        ojoy -= delta
    if key == b'z':
        ojoz += delta
    if key == b'Z':
        ojoz -= delta
    if key == b'i':
        look_x += delta
    if key == b'I':
        look_x -= delta
    if key == b'o':
        look_y += delta
    if key == b'O':
        look_y -= delta
    if key == b'p':
        look_z += delta
    if key == b'P':
        look_z -= delta
    if key in [b'0', b'1', b'2', b'3', b'4', b'5', b'6']:
        caras[int(key)] = not caras[int(key)]

    # Rotación respecto al origen
    delta = 0.5
    if key == b'w':
        rotacion_general[0] -= delta
    if key == b'W':
        rotacion_general[0] += delta
    if key == b'e':
        rotacion_general[1] -= delta
    if key == b'E':
        rotacion_general[1] += delta
    if key == b'r':
        rotacion_general[2] -= delta
    if key == b'R':
        rotacion_general[2] += delta
    if key == b't':
        rotacion_general[3] -= delta
    if key == b'T':
        rotacion_general[3] += delta

    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glDepthFunc(GL_LESS)
    glutInitWindowSize(pantallax, pantallay)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow("Cubo 3D con rotación de caras")
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()


main()
