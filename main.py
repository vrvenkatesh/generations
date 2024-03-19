from Player import Player
from Game import Game
import pandas as pd
import random
generations = ['Boomer', 'GenX', 'Millennial', 'GenZ']
# Unit Test Code
nl = '\n'
players = []
action_cards = pd.read_csv('data/action_cards_and_points.csv').drop(columns=['Color', 'Suite', 'SlideURL']) # start with getting ACs working first
objective_cards = []
impact_cards = []
deck = action_cards.sample(frac=1).head() # consider adding objective cards to AC list
min_players = 2
max_players = 4
num_players = random.randint(min_players, max_players) # first try without random

action_cards[generations] = action_cards[generations].astype(int)

for x in range(num_players):
    generation = generations.pop(random.randrange(len(generations)))
    #print(generation)
    players.append(Player(generation))

#print([player.generation for player in players])
game = Game(players, deck)
#print([player.generation for player in game.players])
for x in range(game.max_rounds):
    game.play_round()
