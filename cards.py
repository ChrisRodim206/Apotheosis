import pygame

class Card:
    def __init__(self, name, energy_cost, value, image, x, y):
        self.name = name
        self.energy_cost = energy_cost
        self.value = value
        self.image = image
        self.x = x
        self.y = y

    