import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#add_texture

pygame.init()
pygame.display.set_mode((500, 500), OPENGL | DOUBLEBUF)
#add_texture
gluPerspective(45, (500 / 500), 0.1, 50.0)
glTranslatef(0.0, 0.0, -15)

vertices = [(1,1,1),(-1,1,1),(-1,-1,1),
            (1,1,1),(-1,-1,1),(1,-1,1)]
texture = [(0,0),(0,1),(1,1),(0,0),(1,1),(1,0)]

def draw_square():
    glBegin(GL_TRIANGLES)
    for i, tri in enumerate(vertices):
        glTexCoord2f(texture[i][0], texture[i][1])
        glVertex3fv(tri)
    glEnd()
# draw_cube
while True:
    glRotatef(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_square()
    pygame.display.flip()
    pygame.time.wait(10)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()