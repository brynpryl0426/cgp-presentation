import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def add_texture():
    image = pygame.image.load('texture1.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)

pygame.init()
pygame.display.set_mode((500, 500), OPENGL | DOUBLEBUF)
add_texture()
gluPerspective(45, (500 / 500), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

vertices = [(1,1,1),(-1,1,1),(-1,-1,1),
            (1,1,1),(-1,-1,1),(1,-1,1)]
texture = [(0,0),(0,1),(1,1),(0,0),(1,1),(1,0)]

def draw_square():
    glBegin(GL_TRIANGLES)
    for i, tri in enumerate(vertices):
        glTexCoord2f(texture[i][0], texture[i][1])
        glVertex3fv(tri)
    glEnd()

def draw_cube():
    glPushMatrix()
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(90,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-90,1,0,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(180,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-90,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(90,1,0,0)
    draw_square()
    glPopMatrix()

while True:
    glRotatef(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(10)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()