import pygame
import os
import sys
import time

from pygame.event import post

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 450
window = pygame.display.set_mode((WIDTH, HEIGHT))

CIASTKO = pygame.transform.scale(pygame.image.load(os.path.join("assets","ciastko.png")),(200,200)) #600x600  ->   200x200
ULEPSZENIE = pygame.image.load(os.path.join("assets", "ulepszenie.png"))
TLO = pygame.transform.scale(pygame.image.load(os.path.join("assets","ty-ciastko.jpg")), (WIDTH, HEIGHT)) #1600x900  ->  400x225
czcionka_szmalu = pygame.font.Font(os.path.join("assets", "font.otf"), 40)
czcionka_lvl = pygame.font.Font(os.path.join("assets", "font.otf"), 20)

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    window.blit(rotated_image, new_rect)

def redraw_window(kat, animacja, animacja2, animacja3):
      window.blit(TLO,(0, 0))
      #window.blit(pygame.transform.rotate(CIASTKO,kat), (WIDTH/2 - 100, HEIGHT/2 - 100))
      if (animacja > 0):
            rot_center(pygame.transform.scale(CIASTKO, (180,180)), kat, WIDTH/2, HEIGHT/2)
      else:
            rot_center(CIASTKO, kat, WIDTH/2, HEIGHT/2)
      szmal_napis = czcionka_szmalu.render(str(szmal), 1, (0,0,0))
      koszt1_napis = czcionka_lvl.render("koszt: " + str(koszt), 1, (0,0,0))
      level1_napis = czcionka_lvl.render("lvl: " + str(lvl), 1, (0,0,0))
      koszt2_napis = czcionka_lvl.render("koszt: " + str(koszt2), 1, (0,0,0))
      level2_napis = czcionka_lvl.render("lvl: " + str(lvl2), 1, (0,0,0))
      window.blit(szmal_napis,(WIDTH/2 - szmal_napis.get_width()/2, 30))
      window.blit(ULEPSZENIE, (20,150 - ULEPSZENIE.get_height()/2))
      window.blit(koszt1_napis, (20 + ULEPSZENIE.get_width() - 100, 150 - koszt1_napis.get_height()))
      window.blit(level1_napis, (20 + ULEPSZENIE.get_width() - 100, 150))
      if (animacja2 > 0):
            ulepszenie_male = pygame.transform.scale(ULEPSZENIE,(0.5 * ULEPSZENIE.get_width(),0.5 * ULEPSZENIE.get_height()))
            window.blit(ulepszenie_male, (20,300 - ULEPSZENIE.get_height()/2))
            window.blit(pygame.transform.scale(koszt2_napis,(0.5 * koszt2_napis.get_width(),0.5 * koszt2_napis.get_height())), (20 + ULEPSZENIE.get_width() - 100, 300 - koszt1_napis.get_height()))
            window.blit(pygame.transform.scale(level2_napis,(0.5 * level2_napis.get_width(),0.5 * level2_napis.get_height())), (20 + ULEPSZENIE.get_width() - 100, 300))
      else:
            window.blit(ULEPSZENIE, (20,300 - ULEPSZENIE.get_height()/2))
            window.blit(koszt2_napis, (20 + ULEPSZENIE.get_width() - 100, 300 - koszt1_napis.get_height()))
            window.blit(level2_napis, (20 + ULEPSZENIE.get_width() - 100, 300))
      
      
      pygame.display.update()

run = True
FPS = 60
clock = pygame.time.Clock()
kat = 0
szmal = 2000
koszt = 100
lvl = 1
koszt2 = 100
lvl2 = 1
ile_na_sekunde = 1
ile_daje_level = 1
animacja = 0
animacja2 = 0
animacja3 = 0
kiedy_dodac = 60
#wykonujemy 60 na sekunde   180 na sekunde  180/60 = 3
while run:
      clock.tick(FPS)
      if kiedy_dodac == 0:
            szmal += ile_na_sekunde * lvl2
            kiedy_dodac = 60
      kiedy_dodac -= 1
      animacja -= 1
      animacja2 -= 1
      animacja3 -= 1
      kat = kat % 360 + 3
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False;
            if event.type == pygame.MOUSEBUTTONDOWN:
                  pos = pygame.mouse.get_pos()
                  if (pos[0] > 300 and pos[0] < 500 and pos[1] > 125 and pos[1] < 325):
                        szmal += lvl * ile_daje_level
                        animacja = 5
                  if (pos[0] > 20 and pos[0] < 20 + ULEPSZENIE.get_width() and pos[1] >  150 - ULEPSZENIE.get_height()/2 and pos[1] < 150 - ULEPSZENIE.get_height()/2 + ULEPSZENIE.get_height()):
                        if szmal >= koszt:
                              szmal -= koszt
                              lvl += 1
                              koszt += 100
                        animacja2 = 200
                  if (pos[0] > 20 and pos[0] < 20 + ULEPSZENIE.get_width() and pos[1] >  300 - ULEPSZENIE.get_height()/2 and pos[1] < 300 - ULEPSZENIE.get_height()/2 + ULEPSZENIE.get_height()):
                        if szmal >= koszt2:
                              szmal -= koszt2
                              lvl2 += 1
                              koszt2 += 100
                        animacja3 = 5
      redraw_window(kat, animacja, animacja2, animacja3)

#upgrady
#animacje
#muzyka
#py2exe


