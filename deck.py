from cards import Card
from random import randint
import pygame  

class deck:
    def __init__(self):
        self.in_deck = []
        self.out_of_deck = []

    def initialize_deck(self):
        
        for i in range(10):
            x = (((800 - (5 * (225 // 2))) // 2 ))
            y = 1080 - 350
            if i < 5:
                #x += total_change
                card = Card(
                    "Strike", 1, 6, 
                    pygame.transform.scale(pygame.image.load(".assets/Cards/card_strike.png"), (225, 225)),
                    x, y
                )
                self.out_of_deck.append(card)
            elif i < 9:
                #x += total_change
                card = Card(
                    "Block", 1, 5, 
                    pygame.transform.scale(pygame.image.load(".assets/Cards/card_block.png"), (225, 225)), 
                    x, y
                )
                self.out_of_deck.append(card)
    
    
    def shuffle_indeck(self):
        for i in range(5):
            rand_index = randint(0, len(self.out_of_deck) - 1)
            card = self.out_of_deck.pop(rand_index)
            self.in_deck.append(card)

        screen = pygame.display.set_mode((800, 600)) #change this when switching over to apotheosis
        x = (1920 // 3) - 36 #also change this as well ;;; this will not work with some screen dimensions
        change = 125
        for card in self.in_deck:
            card.x = x
            x += change           
    
    def shuffle_outofdeck(self):
        for i in range(4):
            rand_index = randint(0, len(self.in_deck) - 1)
            card = self.in_deck.pop(rand_index)
            self.out_of_deck.append(card)

    def draw_deck(self, screen):

        for card in self.in_deck:
            screen.blit(card.image, (card.x, card.y))