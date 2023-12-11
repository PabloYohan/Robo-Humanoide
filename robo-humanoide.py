from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np

rot = 0
texturas = []

def cubo(size_x, size_y, size_z):
        glBegin(GL_POLYGON)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size_x, size_y,size_z)
        glTexCoord2f(1.0,0.0)
        glVertex3f(size_x, size_y,size_z)
        glTexCoord2f(1.0,1.0)
        glVertex3f(size_x, -size_y,size_z)
        glTexCoord2f(0.0,1.0)
        glVertex3f(-size_x, -size_y,size_z)
        glEnd()

        glBegin(GL_POLYGON)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size_x,size_y,-size_z)
        glTexCoord2f(1.0,0.0)
        glVertex3f(size_x,size_y,-size_z)
        glTexCoord2f(1.0,1.0)
        glVertex3f(size_x,-size_y,-size_z)
        glTexCoord2f(0.0,1.0)
        glVertex3f(-size_x,-size_y,-size_z)
        glEnd()

        glBegin(GL_POLYGON)
        glTexCoord2f(0.0,0.0)
        glVertex3f(size_x,-size_y,size_z)
        glTexCoord2f(1.0,0.0)
        glVertex3f(size_x,size_y,size_z)
        glTexCoord2f(1.0,1.0)
        glVertex3f(size_x,size_y,-size_z)
        glTexCoord2f(0.0,1.0)
        glVertex3f(size_x,-size_y,-size_z)
        glEnd()

        glBegin(GL_POLYGON)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size_x,-size_y,size_z)
        glTexCoord2f(1.0,0.0)
        glVertex3f(-size_x,size_y,size_z)
        glTexCoord2f(1.0,1.0)
        glVertex3f(-size_x,size_y,-size_z)
        glTexCoord2f(0.0,1.0)
        glVertex3f(-size_x,-size_y,-size_z)
        glEnd()

        glBegin(GL_POLYGON)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size_x,size_y,size_z)
        glTexCoord2f(1.0,0.0)
        glVertex3f(size_x,size_y,size_z)
        glTexCoord2f(1.0,1.0)
        glVertex3f(size_x,size_y,-size_z)
        glTexCoord2f(0.0,1.0)
        glVertex3f(-size_x,size_y,-size_z)
        glEnd()

        glBegin(GL_POLYGON)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size_x,-size_y,size_z)
        glTexCoord2f(1.0,0.0)
        glVertex3f(size_x,-size_y,size_z)
        glTexCoord2f(1.0,1.0)
        glVertex3f(size_x,-size_y,-size_z)
        glTexCoord2f(0.0,1.0)
        glVertex3f(-size_x,-size_y,-size_z)
        glEnd()

class Robo:
    def __init__(self):
        global rot

        self.perna_direita_rot = 40, 0
        self.perna_esquerda_rot = -40, 0
        self.braco_direito_rot = -20, 0
        self.braco_esquerdo_rot = 20, 40
        self.movimento = 5.0
        self.perna = 'r'
        self.braco = 'l'
   
    def animation(self):
        if self.perna == 'r':
            self.perna_direita_rot = self.perna_direita_rot[0] - self.movimento, self.perna_direita_rot[1]
            self.perna_esquerda_rot = self.perna_esquerda_rot[0] + self.movimento, self.perna_esquerda_rot[1] + (1 if self.perna_esquerda_rot[0] > 0 else - 1) * self.movimento * 2
            if self.perna_direita_rot[0] <= -40:
                self.perna_direita_rot = -40, 0
                self.perna_esquerda_rot = 40, 0
                self.perna = 'l'
        elif self.perna == 'l':
            self.perna_direita_rot = self.perna_direita_rot[0] + self.movimento, self.perna_direita_rot[1] + (1 if self.perna_direita_rot[0] > 0 else - 1) * self.movimento * 2
            self.perna_esquerda_rot = self.perna_esquerda_rot[0] - self.movimento, self.perna_esquerda_rot[1]
            if self.perna_esquerda_rot[0] <= -40:
                self.perna_direita_rot = 40, 0
                self.perna_esquerda_rot = -40, 0
                self.perna = 'r'

        
        if self.braco == 'r':
            self.braco_direito_rot = self.braco_direito_rot[0] - self.movimento / 2, self.braco_direito_rot[1] - self.movimento / 2
            self.braco_esquerdo_rot = self.braco_esquerdo_rot[0] + self.movimento / 2, self.braco_esquerdo_rot[1] + self.movimento / 2
            if self.braco_direito_rot[0] <= -20:
                self.braco_direito_rot = -20, 0
                self.braco_esquerdo_rot = 20, 40
                self.braco = 'l'
        elif self.braco == 'l':
            self.braco_direito_rot = self.braco_direito_rot[0] + self.movimento / 2, self.braco_direito_rot[1] + self.movimento / 2
            self.braco_esquerdo_rot = self.braco_esquerdo_rot[0] - self.movimento / 2, self.braco_esquerdo_rot[1] - self.movimento / 2
            if self.braco_esquerdo_rot[0] <= -20:
                self.braco_direito_rot = 20, 40
                self.braco_esquerdo_rot = -20, 0
                self.braco = 'r'


    def render(self):
        self.animation()
       
        glPushMatrix()
        glTranslatef(0.0, abs(abs(self.perna_direita_rot[0] / 20) - 1) / 15, 0.0)
        glRotatef(rot, 0, 1, 0)
        self.corpo()
        self.cabeca()
        self.braco_direito()
        self.braco_esquerdo()
        self.perna_direita()
        self.perna_esquerda()
        glPopMatrix()

    def corpo(self):
        glPushMatrix()
        cubo(0.3, 0.4, 0.1)
        glPopMatrix()
   
    def cabeca(self):
        glPushMatrix()
        glTranslatef(0.0, 0.7, 0.0)
        cubo(0.25, 0.25, 0.25)
        glPopMatrix()

    def braco_direito(self):
        glPushMatrix()
        
        glTranslatef(-0.4, 0.4, 0.0)
        glRotatef(self.braco_direito_rot[0], 1, 0, 0)
        glTranslatef(0.0, -0.2, 0.0)
        cubo(0.1, 0.2, 0.1)

        
        glRotatef(self.braco_direito_rot[1], 1, 0, 0)
        glTranslatef(0.0, -0.5, 0.0)
        cubo(0.1, 0.2, 0.1)
        glPopMatrix()
   
    def braco_esquerdo(self):
        glPushMatrix()
        
        glTranslatef(0.4, 0.4, 0.0)
        glRotatef(self.braco_esquerdo_rot[0], 1, 0, 0)
        glTranslatef(0.0, -0.2, 0.0)
        cubo(0.1, 0.2, 0.1)

        
        glRotatef(self.braco_esquerdo_rot[1], 1, 0, 0)
        glTranslatef(0.0, -0.5, 0.0)
        cubo(0.1, 0.2, 0.1)
        glPopMatrix()
   
    def perna_direita(self):
        glPushMatrix()
        
        glRotatef(self.perna_direita_rot[0], 1, 0, 0)
        glTranslatef(-0.15, -0.7, 0.0)
        cubo(0.15, 0.2, 0.15)

        
        glRotatef(self.perna_direita_rot[1], 1, 0, 0)
        glTranslatef(0.0, -0.5, 0.0)
        cubo(0.15, 0.2, 0.15)
        glPopMatrix()
   
    def perna_esquerda(self):
        glPushMatrix()
        
        glRotatef(self.perna_esquerda_rot[0], 1, 0, 0)
        glTranslatef(0.15, -0.7, 0.0)
        cubo(0.15, 0.2, 0.15)

        
        glRotatef(self.perna_esquerda_rot[1], 1, 0, 0)
        glTranslatef(0.0, -0.5, 0.0)
        cubo(0.15, 0.2, 0.15)
        glPopMatrix()

def CarregaTextura():
    global texturas
    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    textura = Image.open("textura.jpg")
  
    textura_data = np.array(textura)


    textura_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, textura.width, textura.height, 0, GL_RGB, GL_UNSIGNED_BYTE, textura_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )

    texturas.append(textura)

def lightning():
    light0_pos = (0.0, 0.0, 0.0, 1.0)
    white = (1.0, 1.0, 1.0, 1.0)
    black = (0.0, 0.0, 0.0, 1.0)

    glLightfv(GL_LIGHT0,GL_POSITION,light0_pos)
    glLightfv(GL_LIGHT0,GL_AMBIENT,black)
    glLightfv(GL_LIGHT0,GL_DIFFUSE,white)
    glLightfv(GL_LIGHT0,GL_SPECULAR,white)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)




def update(*args):
    display()

Robo = Robo()

def display():
    global Robo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    glPushMatrix()
    glScalef(0.5, 0.5, 0.5)
    Robo.render()
    glPopMatrix()

    glutSwapBuffers()
    glutTimerFunc(20, update, 1)

def tecladoEspecial(tecla, x, y):  
    global rot, movimento

    if tecla == GLUT_KEY_RIGHT:
        rot += 1
    elif tecla == GLUT_KEY_LEFT:
        rot -= 1

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 640)
    glutCreateWindow("Robo")
    glutDisplayFunc(update)
    glutSpecialFunc(tecladoEspecial)
    glEnable(GL_DEPTH_TEST)
    lightning()
    CarregaTextura()
    glutMainLoop()

if __name__ == '__main__':
    print(__name__)
    main()
