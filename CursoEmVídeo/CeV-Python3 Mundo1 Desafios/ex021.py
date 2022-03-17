# DESAFIO 021
# Faça um programa em Pyhon que abra e reproduza o áudio de um arquivo mp3.

#import playsound
#playsound.playsound('ex021.mp3')

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()


