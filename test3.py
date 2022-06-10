import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
pygame.display.set_mode((500,500), DOUBLEBUF|OPENGL)
gluPerspective(50,(500/500),0.1,50)
glTranslate(0,0,-20)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
vertices = [(1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1)]
edges = [(0,1),(1,2),(2,3),(3,0)]
surfaces = [(0,1,2),(0,2,3)]

surfaces2 = [(0,1,2,3)]

colors = [(1,0,0,0.2),(0,1,0,0.4),(0,0,1,0.2)]

circle = gluNewQuadric()

def draw():
    '''glBegin(GL_LINES)
    for i, edge in enumerate(edges):
        for line in edge:
            glVertex3fv(vertices[line])
    glEnd()'''

    '''glBegin(GL_TRIANGLES)
    for i, edge in enumerate(surfaces):
        for line in edge:
            glVertex3fv(vertices[line])
    glEnd()'''

    '''glBegin(GL_QUADS)
    for i, edge in enumerate(surfaces2):
        glColor4fv(colors[i])
        for line in edge:
            glVertex3fv(vertices[line])
    glEnd()'''

    '''
    for i, edge in enumerate(surfaces2):
        glColor4fv(colors[i])
        gluSphere(circle,2,40,40)'''
    

def draw_object():
    glPushMatrix()
    glScale(2,2,2)
    draw()
    glPopMatrix()
    
    glPushMatrix()
    glScale(1.5,1.5,1.5)
    draw()
    glPopMatrix()

    glPushMatrix()
    glScale(1,1,1)
    draw()
    glPopMatrix()

while True:
    glRotate(1,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_object()
    pygame.display.flip()
    pygame.time.wait(20)
