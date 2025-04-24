from cards import Card
from random import randint
import pygame  
from time import sleep

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
                    "Defend", 1, 5, 
                    pygame.transform.scale(pygame.image.load(".assets/Cards/card_defend.png"), (225, 225)), 
                    x, y
                )
                self.out_of_deck.append(card)

        # Adding 7 new cards to the deck
        new_cards = [
            ("Bloodletting", 3, ".assets/Cards/card_bloodletting.png"),
            ("Bludgeon", 32, ".assets/Cards/card_bludgeon.png"),
            ("Cleave", 8, ".assets/Cards/card_cleave.png"),
            ("Iron Wave", 5, ".assets/Cards/card_iron_wave.png"),
            ("Bash", 8, ".assets/Cards/card_Bash.png"),
            ("Pommel Strike", 9, ".assets/Cards/card_pommel_strike.png"),
            ("Twin Strike", 5, ".assets/Cards/card_twin_strike.png")
        ]

        for name, value, image_path in new_cards:
            card = Card(
                name, 1, value,
                pygame.transform.scale(pygame.image.load(image_path), (225, 225)),
                x, y
            )
            self.out_of_deck.append(card)
    
    
    def shuffle_indeck(self):
        card_counts = {}

        for i in range(5):
            rand_index = randint(0, len(self.out_of_deck) - 1)
            card = self.out_of_deck[rand_index]

            # Count occurrences of each card type in the hand
            card_name = card.name
            if card_name not in card_counts:
                card_counts[card_name] = 0

            # Ensure at most 1 of the new cards and up to 3 of Strike/Defend
            if (card_name in ["Strike", "Defend"] and card_counts[card_name] < 3) or \
               (card_name not in ["Strike", "Defend"] and card_counts[card_name] < 1):
                self.out_of_deck.pop(rand_index)
                self.in_deck.append(card)
                card_counts[card_name] += 1

        x = (1920 // 3) - 36  # Adjust x-coordinate for screen dimensions
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
    
    def draw_card(self):
        card = self.out_of_deck[randint(0, len(self.out_of_deck) - 1)]
        self.out_of_deck.remove(card)
        self.in_deck.append(card)
        self.draw_deck
    
    def use_card(self, card, current_player, current_monster):
        if card.name == "Strike":
            current_player.mana = current_player.mana - 1
            current_monster.hp = current_monster.hp - 6
        elif card.name == "Defend":
            current_player.mana = current_player.mana - 1
            current_player.block += 5
        elif card.name == "Bloodletting":
            current_player.hp = current_player.hp - 3
            current_player.mana = current_player.mana + 2
        elif card.name == "Bash":
            current_player.mana = current_player.mana - 2
            current_monster.hp = current_monster.hp - 8
        elif card.name == "Cleave":
            current_player.mana = current_player.mana - 1
            current_monster.hp = current_monster.hp - 8
        elif card.name == "Twin Strike":
            current_player.mana = current_player.mana - 1
            current_monster.hp = current_monster.hp - 5
            sleep(0.25)
            current_monster.hp = current_monster.hp - 5
        elif card.name == "Pommel Strike":
            current_player.mana = current_player.mana - 1
            current_monster.hp = current_monster.hp - 9
            self.draw_card()
        elif card.name == "Iron Wave":
            current_player.mana = current_player.mana - 1
            current_monster.hp = current_monster.hp - 5
            current_player.block += 5
        elif card.name == "Bludgeon":
            current_player.mana = current_player.mana - 3
            current_monster.hp = current_monster.hp - 32