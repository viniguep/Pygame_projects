import pygame
from pygame.locals import *
from pygame.display import *
from sys import exit
from tkinter import *
from tkinter.ttk import *

pygame.init()
pygame.font.init()

# fonts
font = pygame.font.Font('../Fontes/the_students_teacher/TheStudentsTeacher-Regular.ttf', 32)


class button:
    def __init__(self, texto, padding, tamanho, cor_da_caixa, cor_do_texto, font, bonito, x, y):
        self.txt = texto
        self.pad = padding
        self.tamanho = tamanho
        self.cor_caixa = cor_da_caixa
        self.cor_txt = cor_do_texto
        self.font = font
        self.bonito = bonito
        self.pos = (x, y)
        self.x = x
        self.y = y
        self.times = True
        self.type = 0
        self.text = 0
        self.rect = 0
        self.box = 0
        self.size = 0

    def click(self):
        self.type = pygame.font.Font(self.font, self.tamanho)
        self.text = self.type.render(self.txt, self.bonito, self.cor_txt)
        self.size = self.text.get_size()
        self.box = list(f'{self.size}')
        self.box.remove('(')
        self.box.remove(')')
        self.box.remove(',')
        self.box = ''.join(self.box)
        self.box = self.box.split(' ')

        self.rect = pygame.draw.rect(screen, self.cor_caixa, (self.x - self.pad - 2, self.y - self.pad // 2, int(self.box[0]) + self.pad * 2, int(self.box[1]) + self.pad))

        screen.blit(self.text, self.pos)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and self.times:
            self.times = False
            return True
        if not pygame.mouse.get_pressed()[0]:
            self.times = True


def sair():
    pygame.quit()
    exit()


b1 = button('Sair', 15, 60, (255, 0, 0), (250, 250, 250), '../Fontes/the_students_teacher/TheStudentsTeacher-Regular.ttf', True, 200, 200)

root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

screen = set_mode((width, height))
set_caption('Flappy Bird')
set_icon(pygame.image.load('../imagens/flappy_bird_ico.png'))

Menu = True
Jogo = False

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            sair()

    if Menu:
        pass

    if b1.click():
        sair()


    flip()

