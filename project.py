from Collectible import Collectible
from Enemy import Enemy
from Platform import Platform
from Player import Player
from defines import Constants
from Engine import Engine
####################################################################################
# Данный код представляет собой каркас для игры в жанре платформер                 #
# В нем определены: классы главного героя, врагов, собираемых предметов и платформ #
# управление с помощью клавиатуры, проверка коллизий объектов                      #
# Проект можно запустить для демонстрации функционала                              #
####################################################################################


################################################################
#При запуске:                                                  #
# синие элементы - платформы,                                  #
# красный элемент - враг,                                      #
# зеленый элемент - игрок,                                     #
# желтый элемент - собираемый предмет                          #
#                                                              #
#Управление: стрелки клавиатуры для движения, пробел для прыжка#
################################################################

#подключние бибилиотек
import pygame

#инициализация Pygame
pygame.init()

eng = Engine()
eng.define_level()
eng.load_world()

eng.main_loop()

pygame.quit()