import numpy as np
import pandas as pd
import random

action_cards = pd.read_csv('data/action_cards_and_points.csv').drop(columns=['Color', 'Suite', 'SlideURL'])

class Player(object):
    def __init__(self, generation):
        self.generation = generation
        self.trade_gen = 1
        self.objectives = 0
        self.points = 1000
        self.cards = pd.DataFrame(columns=action_cards.columns)

    def get_generation(self):
        return self.generation

    def get_trade_gen(self):
        return self.trade_gen

    def get_objectives(self):
        return self.objectives

    def get_cards(self):
        return self.cards

    def trade_generation(self, generation):
        self.generation = generation

    def draw_card(self, deck):
        card = deck.sample()
        self.cards = pd.concat([self.cards, card])
        return card

    def play_card(self):
        if len(self.cards) > 0:
            card = self.cards.sample()
            points = card.get(self.generation).values[0]
            self.points += points
            self.cards = self.cards.drop(card.index)
        else:
            print(f"No cards in hand for player {self.generation}")


    def perform_dance(self):
        return "Dance performed"

    def __str__(self):
        nl = "\n"
        return f"Player: {self.generation}{nl}" \
               f"Objectives: {self.objectives}{nl}" \
               f"Points: {self.points}{nl}"
