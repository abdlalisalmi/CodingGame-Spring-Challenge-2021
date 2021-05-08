import sys
import math


MY_TREES = list()
SEED = list()
GROW = list()
COMPLETE = list()

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


def get_number_of_trees(size):
    number = 0
    for tree in MY_TREES:
        if tree.size == size:
            number += 1
    return number

def get_tree_by_index(index):
    for tree in MY_TREES:
        if tree.index == index:
            return tree


def get_green_trees():
    trees = []
    for tree in GROW:
        index = int(tree.split(" ")[1])
        if index >= 0 and index <= 6:
            trees.append(index)
    return trees

def get_yellow_trees():
    trees = []
    for tree in GROW:
        index = int(tree.split(" ")[1])
        if index >= 7 and index <= 18:
            trees.append(index)
    return trees

def get_orange_trees():
    trees = []
    for tree in GROW:
        index = int(tree.split(" ")[1])
        if index >= 19 and index <= 36:
            trees.append(index)
    return trees

def get_bets_seed():
    SEED.sort()
    best_seed = []
    for seed in SEED:
        best_seed.append({
            'frm': int(seed.split(" ")[1]),
            'to': int(seed.split(" ")[2])
        })
    best_seed = sorted(best_seed, key=lambda k: k['to'])
    return best_seed[0]
    #print(best_seed, file=sys.stderr, flush=True)

def seed_to_green():
    for seed in SEED:
        to = int(seed.split(" ")[2])
        if to >= 0 and to <= 6:
            return True
    return False

def seed_to_yellow():
    for seed in SEED:
        to = int(seed.split(" ")[2])
        if to >= 7 and to <= 18:
            return True
    return False



def bronze_algorithme(sun, day):
    #complete
    #seed bets index
    #grow the best index green yellow orange
    #wait

    if COMPLETE:
        if get_number_of_trees(3) > 3 or day >= 13:
            COMPLETE.sort()
            if sun >= 4:
                print(f"{COMPLETE[0]}")
                return

    if SEED:
        if day < 16 and seed_to_green():
            SEED.sort()
            #print(SEED, file=sys.stderr, flush=True)
            if len(MY_TREES) < 8 and get_number_of_trees(0) <= sun:
                seed = get_bets_seed()
                print(f"SEED {seed.get('frm')} {seed.get('to')}")
                return

        if day < 16 and seed_to_yellow() and get_number_of_trees(3):
            SEED.sort()
            #print(SEED, file=sys.stderr, flush=True)
            if len(MY_TREES) < 8 and get_number_of_trees(0) <= sun:
                seed = get_bets_seed()
                print(f"SEED {seed.get('frm')} {seed.get('to')}")
                return

    if GROW:
        green_trees = get_green_trees()
        if green_trees:
            for index in green_trees:
                tree = get_tree_by_index(index)
                if tree.size == 0 and get_number_of_trees(0) <= sun or tree.size == 1 and sun >= 3 or tree.size == 2 and sun >= 7:
                    print(f"GROW {tree.index}")
                    return
        
        yellow_trees = get_yellow_trees()
        print(f"tree : {yellow_trees}", file=sys.stderr, flush=True)
        if yellow_trees:
            for index in yellow_trees:
                tree = get_tree_by_index(index)
                if tree.size == 0 and get_number_of_trees(0) <= sun or tree.size == 1 and sun >= 3 or tree.size == 2 and sun >= 7:
                    print(f"GROW {tree.index}")
                    return

        orange_trees = get_orange_trees()
        if orange_trees:
            for index in orange_trees:
                tree = get_tree_by_index(index)
                if tree.size == 0 and get_number_of_trees(0) <= sun or tree.size == 1 and sun >= 3 or tree.size == 2 and sun >= 7:
                    print(f"GROW {tree.index}")
                    return
        
    print("WAIT Zzz")




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

    #print(SEED, file=sys.stderr, flush=True)
    #print(GROW, file=sys.stderr, flush=True)
    #print(COMPLETE, file=sys.stderr, flush=True)

    bronze_algorithme(sun, day)


    MY_TREES.clear()
    SEED.clear()
    GROW.clear()
    COMPLETE.clear()

