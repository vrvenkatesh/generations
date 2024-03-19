import numpy as np
import pandas as pd
import random
from Player import Player
generations = {'Boomer': 1, 'GenX': 2, 'Millennial': 3, 'GenZ': 4}
class Game:

    def __init__(self, players, deck):
        self.players = sorted(players, key=lambda x: generations[x.generation])
        self.rounds = 0
        self.max_rounds = 100
        self.deck = deck
        self.discard_pile = pd.DataFrame(columns=deck.columns)


    def play_round(self):
        print(f"Round {self.rounds}")
        print(f"Point totals: {[(player.generation, player.points) for player in self.players]}")

        if self.rounds == self.max_rounds:
            print("Max rounds reached")
            print(f"Final point totals: {[(player.generation, player.points) for player in self.players]}")
        if any([player.objectives == 4 for player in self.players]):
            print("Game over")
            return "Game over"

        for player in self.players:
            if len(self.deck) == 0:
                self.deck = self.discard_pile.sample(frac=1)
                self.discard_pile = pd.DataFrame(columns=self.deck.columns)
            else:
                card = player.draw_card(self.deck)
                self.deck.drop(card.index)

            player.play_card()

            if player.points <= 0:
                player.points = 0
                print(f"{player.perform_dance()} by {player.generation}")
                continue

        self.rounds += 1