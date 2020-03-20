import random
import constant as C

Q_Matrix = []

def initialize():
      Q_Matrix = [[0 for a in range(len(C.actions))]for s in range(len(C.state))]
      return Q_Matrix

def choose_action(state):
    if random.random() < C.takerisk: return random.choice(range(len(C.actions)))
    else: return greedy_choice(state)

def greedy_choice(state):
    best = max(Q_Matrix[C.state.index(state)])
    bests = [i for i, x in enumerate(Q_Matrix[C.state.index(state)]) if x == best]
    return random.choice(bests)
