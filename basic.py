import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def add_texture():
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    image = pygame.image.load('texture1.jpg')            
    datas = pygame.image.tostring(image, 'RGBA')
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)

pygame.init()
pygame.display.set_mode((500,500), DOUBLEBUF|OPENGL)
# pygame.display
add_texture()
gluPerspective(45, (500/500), 0.1, 50.0)
glTranslate(0,0,-10)

vertices = [(1,1,1),(-1,1,1),(-1,-1,1),
            (1,1,1),(-1,-1,1),(1,-1,1)]

texture = [(0,0),(0,1),(1,1),(0,0),(1,1),(1,0)]

def draw_square():
    glBegin(GL_TRIANGLES)
    # for i in range(6):
    #     glTexCoord2f(texture[i][0], texture[i][1])
    #     glVertex3fv(vertices[i])
    for i,tri in enumerate(vertices):
        glTexCoord2f(texture[i][0], texture[i][1])
        glVertex3fv(tri)
    glEnd()

rotations = [
            (0,0,0,0), # No movement
            (90,0,1,0), # To the right
            (-90,1,0,0), # To the top
            (180,0,1,0), # To the back
            (-90,0,1,0), # To the left
            (90,1,0,0) # To the bottom
            ]

first = 0
first_translator = 10
second = 0
second_translator = 10
third = 0
third_translator = 10
fourth = 0
fourth_translator = 10
fifth = 0
fifth_translator = -10
sixth = 0
sixth_translator = -10

def draw_cube():
    glPushMatrix()
    glScale(first,first,1)
    glTranslate(first_translator,0,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glScale(second,second,1)
    glTranslate(second_translator,0,0)
    glRotatef(90,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glScale(third,third,1)
    glTranslate(0,third_translator,0)
    glRotatef(-90,1,0,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glScale(fourth,fourth,1)
    glTranslate(0,0,fourth_translator)
    glRotatef(180,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glScale(fifth,fifth,1)
    glTranslate(fifth_translator,0,0)
    glRotatef(-90,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glScale(sixth,sixth,1)
    glTranslate(0,sixth_translator,0)
    glRotatef(90,1,0,0)
    draw_square()
    glPopMatrix()

a1, a2 = 0, 0 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                first = 0
                first_translator = 5
                second = 0
                second_translator = 5
                third = 0
                third_translator = 5
                fourth = 0
                fourth_translator = 5
                fifth = 0
                fifth_translator = -5
                sixth = 0
                sixth_translator = -5
                a1 = 0
                a2 = 0
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        glScalef(1.1,1.1,1.1)

    elif keys[pygame.K_DOWN]:
        glScalef(0.9,0.9,0.9)

    a1 += (keys[pygame.K_d] - keys[pygame.K_a]) * 2
    a2 += (keys[pygame.K_w] - keys[pygame.K_s]) * 2

    first += (keys[pygame.K_1]) * 0.01
    first_translator -= (keys[pygame.K_1]) * 0.10
    if first > 1:
        first = 1
        first_translator = 0

    second += (keys[pygame.K_2]) * 0.01
    second_translator -= (keys[pygame.K_2]) * 0.10
    if second > 1:
        second = 1
        second_translator = 0

    third += (keys[pygame.K_3]) * 0.01
    third_translator -= (keys[pygame.K_3]) * 0.10
    if third > 1:
        third = 1
        third_translator = 0

    fourth += (keys[pygame.K_4]) * 0.01
    fourth_translator -= (keys[pygame.K_4]) * 0.10
    if fourth > 1:
        fourth = 1
        fourth_translator = 0
    
    fifth += (keys[pygame.K_5]) * 0.01
    fifth_translator += (keys[pygame.K_5]) * 0.10
    if fifth > 1:
        fifth = 1
        fifth_translator = 0

    sixth += (keys[pygame.K_6]) * 0.01
    sixth_translator += (keys[pygame.K_6]) * 0.10
    if sixth > 1:
        sixth = 1
        sixth_translator = 0

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(a1,0,1,0)
    glRotate(a2,-1,0,0)
    draw_cube()
    glPopMatrix()
    pygame.time.wait(15)
    pygame.display.flip()