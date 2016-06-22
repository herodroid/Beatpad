# -*- coding: utf-8 -*-
__author__ = 'Celso'
# Projeto de projetos
import pyaudio
import wave
import sys
import os
import msvcrt
import time
import serial
import pygame
import threading
from pygame import *

print "Seja bem-vindo ao Beatpad!"
# Inicializacao
sons = []

# Definir diretorio base
local = "C:\Users\Celso\PycharmProjects\lpthw\projeto"

# Definir ID para identificacao do usuario
print "Digite seu User ID:"
userid = raw_input()

# Ajustar diretorio para o usuario escolhido
# Mostrar os artistas encontrados para o usuario definido
local1 = local + chr(92) + userid
print "Ola %s!"  % userid
print "Os artistas encontrados nesse usuario foram:"
print os.listdir(local1)

# Definir o artista
print "Digite o nome do artista:"
artistname = raw_input()

# Ajustar o diretorio para o artista escolhido
# Mostrar as musicas encontradas
local2 = local1 + chr(92) + artistname
print "As musicas encontradas desse artista foram:"
print os.listdir(local2)

# Definir a musica
print "Digite o nome da musica para tocar:"
songname = raw_input()

# Ajustar diretorio para a musica escolhida
local3 = local2 + chr(92) + songname

# Mostrar arquivos '.wav' encontrados no diretorio especificado
print "Os arquivos encontrados foram:"
for file in os.listdir(local3):
    if file.endswith(".wav"):
        sons.append(local3 +chr(92) +file)
        print(file)

# print sons
# Dicionario
dicio = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
      '-': 10, '=': 11, 'q': 12, 'w': 13, 'e': 14, 'r': 15, 't': 16, 'y': 17, 'u': 18,
      'i': 19, 'o': 20, 'p': 21, '[': 22, ']': 23, 'a': 24, 's': 25, 'd': 26, 'f': 27,
      'g': 28, 'h': 29, 'j': 30, 'k': 31, 'l': 32, ';': 33, "'": 34, 'z': 35, 'x': 36,
      'c': 37, 'v': 38, 'b': 39, 'n': 40, 'm': 41, ',': 42, '.': 43, '/': 44, 'Q': 45,
      'W': 46, 'E': 47, 'R': 48, 'T': 49, 'Y': 50, 'U': 51, 'I': 52, 'O': 53, 'P': 46,
      'A': 47, 'S': 48, 'D': 49, 'F': 50, 'G': 51, 'H': 52, 'J': 53, 'K': 54, 'L': 55,
      'Z': 56, 'X': 57, 'C': 58, 'V': 59, 'B': 60, 'N': 61, 'M': 62}

## Porta serial
#portaserial = serial.Serial('COM4', 9600)

# Pygame
mixer.pre_init(frequency=96000, size=-16, channels=2, buffer=4096)
#mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)
#pygame.init()
pygame.mixer.init()
print pygame.mixer.get_init()

#while True:
#    pre_input_key = portaserial.read(1)
#    input_key = sons[dicio[pre_input_key]]
#    s2 = pygame.mixer.Sound(input_key)
#    ch = s2.play()

userinput = []

# Ler tecla
def read_input():
    input_key = msvcrt.getch()
    userinput.append(input_key)

# Tocar som associado a tecla
def play_input():
    a = userinput.pop(0)
    input_key = sons[dicio[a]]
    s2 = pygame.mixer.Sound(input_key)
    ch = s2.play()

input_key = msvcrt.getch()

# Loop
while input_key != '`':
    t1 = threading.Timer(0.005, read_input())
    t2 = threading.Timer(0.010, play_input())
    input_key = msvcrt.getch()

pygame.mixer.quit()
