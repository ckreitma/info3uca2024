from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

altura, ancho = 1500, 1500

# Un cubo que "rodea" el origen
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def inicializar():
    # Borrar la pantalla
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(45, altura/ancho, 0.1, 50.0)
    
    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)
    
    # Inicializar la matriz.
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5.0)

    


def ejes():
    
    # Modificamos la ubicación de los ejes
    glPushMatrix()
    i = 5
    delta = 0.00
    glTranslatef(vertices[i][0]-delta,vertices[i][1]-delta,vertices[i][2]-delta)
    # Eje x
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)

    glEnd()
    glPopMatrix()


def cubo():
    # Ángulo,
    glPushMatrix()
    #glRotatef(20, 0, 0, 1)
    
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glPopMatrix()


def actualizar():
    inicializar()
    ejes()
    cubo()
    ejes()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(altura, ancho)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cubo 3D sencillo con líneas")
    glutDisplayFunc(actualizar)
    glutMainLoop()


main()
