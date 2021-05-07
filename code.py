import sys
import math


MY_TREES = list()
SEED = []
GROW = []
COMPLETE = []

class Tree:
    def __init__(self, index, size, dormant):
        self.index = index
        self.size = size
        self.dormant = dormant

    def sun_check(self, sun):
        if self.size == 0:
            if sun >= 1:
                return True
        if self.size == 1:
            if sun >= 3:
                return True
        if self.size == 2:
            if sun >= 7:
                return True
        if self.size == 3:
            if sun >= 4:
                return True
        return False

    @staticmethod
    def get_completed(trees):
        number_of_trees = 0
        for tree in trees:
            if tree.size == 3:
                number_of_trees += 1
        return number_of_trees
    
    @staticmethod
    def get_seed(trees):
        number_of_trees = 0
        for tree in trees:
            if tree.size == 0:
                number_of_trees += 1
        return number_of_trees


def get_the_best_action():
    if Tree.get_completed(MY_TREES) and Tree.get_seed(MY_TREES):
        return 'C'
    elif Tree.get_completed(MY_TREES) and not Tree.get_seed(MY_TREES):
        return 'S'
    else:
        return 'G'


def seed():
    SEED.sort()
    for i in range(0, len(SEED)-1):
        seed = SEED[i]
        next_seed = SEED[i + 1]
        if int(seed.split(' ')[1]) > int(next_seed.split(' ')[1]):
            SEED[i], SEED[i+1] = SEED[i + 1], SEED[i]
    for seed in SEED:
        print(seed)


def grow(sun):
    GROW.sort()
    for grow in GROW:
        tr = 0
        index = int(grow.split(' ')[1])
        for tree in MY_TREES:
            if tree.index == index:
                tr = tree
        if tree.sun_check(sun):
            print(f"GROW {tree.index}")


def complete(sun):
    COMPLETE.sort()
    for complete in COMPLETE:
        tr = 0
        index = int(complete.split(' ')[1])
        for tree in MY_TREES:
            if tree.index == index:
                tr = tree
        if tree.sun_check(sun):
            print(f"COMPLETE {tree.index}")


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]

# game loop
while True:
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        

        if is_mine:
            tree = Tree(cell_index, size, is_dormant)
            MY_TREES.append(tree)


    number_of_possible_actions = int(input())  # all legal actions
    for i in range(number_of_possible_actions):
        possible_action = input()  # try printing something from here to start with
        if possible_action.startswith('S'):
            SEED.append(possible_action)
        elif possible_action.startswith('G'):
            GROW.append(possible_action)
        elif possible_action.startswith('C'):
            COMPLETE.append(possible_action)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    
    print("WAIT")



    MY_TREES.clear()
    SEED.clear()
    GROW.clear()
    COMPLETE.clear()

