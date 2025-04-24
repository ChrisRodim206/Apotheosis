import pygame as pg
import sys
import time
from deck import deck

double_click_speed = 318 # milliseconds

class EventHandler:
    def __init__(self):
        self.dragging_card = None
        self.game_deck = deck()
        self.cards = self.game_deck.in_deck 
        self.last_click_time = 0  # Track the time of the last click

    def check_events(self, current_player, current_monster):
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Process card-related events only if no button is clicked
                if not any(button.rect.collidepoint(event.pos) for button in self.cards):
                    self.check_mousedown_events(event)
                    self.double_click(event, current_player, current_monster)
            elif event.type == pg.MOUSEMOTION:
                self.mouse_motion(event)
            elif event.type == pg.MOUSEBUTTONUP:
                self.check_mouseup_events(event)

    def check_mousedown_events(self, event):
        """Respond to mouse events"""
        if event.button == 1:
            for card in self.cards:
                card_rect = card.image.get_rect(topleft=(card.x, card.y))
                if card_rect.collidepoint(event.pos):
                    self.dragging_card = card
                    break

    def check_mouseup_events(self, event):
        """Respond to mouse release"""
        if event.button == 1:
            self.dragging_card = None

    def mouse_motion(self, event):
        """Respond to mouse motion and move cards while cursor moves"""
        if self.dragging_card:
            card_rect = self.dragging_card.image.get_rect()
            self.dragging_card.x = event.pos[0] - card_rect.width // 2
            self.dragging_card.y = event.pos[1] - card_rect.height // 2

    def double_click(self, event, current_player, current_monster):
        """Handle double click events"""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            current_time = time.time() * 1000  # Get current time in milliseconds
            if current_time - self.last_click_time <= double_click_speed:
                if self.dragging_card:
                    # apply card effects and move to discard pile
                    # example: strike card deals damage, moves to outdeck
                    if self.dragging_card in self.cards: # checks if in deck
                        self.game_deck.use_card(self.dragging_card, current_player, current_monster)
                        self.cards.remove(self.dragging_card)
                        self.game_deck.out_of_deck.append(self.dragging_card)
                    self.dragging_card = None
            self.last_click_time = current_time