
import pygame as pg
import sys
from deck import deck


class EventHandler:
    def __init__(self):
        self.dragging_card = None
        self.game_deck = deck()
        self.cards = self.game_deck.in_deck 

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.check_mousedown_events(event)
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