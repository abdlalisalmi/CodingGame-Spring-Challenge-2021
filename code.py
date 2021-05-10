import sys
import math

MY_TREES = list()
SEED = list()
GROW = list()
COMPLETE = list()

class Tree:
    def __init__(self, index, size, dormant, neighbors):
        self.index = index
        self.size = size
        self.dormant = dormant
        self.neighbors = []
        for neigh in neighbors:
            if not neigh == -1:
                self.neighbors.append(neigh)


def get_number_of_trees(size=None):
    number = 0
    if not size == None:
        for tree in MY_TREES:
            if tree.size == size:
                number += 1
    else:
        for tree in MY_TREES:
            number += 1
    return number


def get_tree_by_index(index):
    for tree in MY_TREES:
        if tree.index == index:
            return tree


def get_trees_by_color(color):
    trees = []
    if color == 'G':
        for tree in GROW:
            index = int(tree.split(" ")[1])
            if index >= 0 and index <= 6:
                tree = get_tree_by_index(index)
                trees.append(tree)
    elif color == 'Y':
        for tree in GROW:
            index = int(tree.split(" ")[1])
            if index >= 7 and index <= 18:
                tree = get_tree_by_index(index)
                trees.append(tree)
    elif color == 'O':
        for tree in GROW:
            index = int(tree.split(" ")[1])
            if index >= 19 and index <= 36:
                tree = get_tree_by_index(index)
                trees.append(tree)
    return trees



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

def get_green_seed(seeds):
    green_seeds = list()
    for seed in seeds:
        to = int(seed.split(" ")[2])
        if to >= 0 and to <= 6:
            green_seeds.append(seed)
    return green_seeds

def get_yellow_seed(seeds):
    green_seeds = list()
    for seed in seeds:
        to = int(seed.split(" ")[2])
        if to >= 7 and to <= 18:
            green_seeds.append(seed)
    return green_seeds

def get_orange_seed(seeds):
    orange_seeds = list()
    for seed in seeds:
        to = int(seed.split(" ")[2])
        if to >= 19 and to <= 36:
            orange_seeds.append(seed)
    return orange_seeds

def best_seed_tree_and_index():
    best_seed = []
    if get_number_of_trees(3):
        bigger_trees_index = []
        for tree in MY_TREES:
            if tree.size == 3:
                bigger_trees_index.append(tree.index)
        for seed in SEED:
            if int(seed.split(" ")[1]) in bigger_trees_index:
                best_seed.append(seed)
    elif get_number_of_trees(2):
        medium_trees_index = []
        for tree in MY_TREES:
            if tree.size == 2:
                medium_trees_index.append(tree.index)
        for seed in SEED:
            if int(seed.split(" ")[1]) in medium_trees_index:
                best_seed.append(seed)
    else:
        return SEED
    return best_seed

def valid_tree(tree, sun):
    return tree.size == 0 and get_number_of_trees(0) <= sun or tree.size == 1 and sun >= 3 or tree.size == 2 and sun >= 7

def grow_function(sun):
    green_trees = sorted(get_trees_by_color('G'), key=lambda tree: tree.index)
    yellow_trees = sorted(get_trees_by_color('Y'), key=lambda tree: tree.index)
    orange_trees = sorted(get_trees_by_color('O'), key=lambda tree: tree.index)


    if green_trees:
        for tree in green_trees:
            if valid_tree(tree, sun):
                print(f"GROW {tree.index}")
                return True
                
    if yellow_trees:
        for tree in yellow_trees:
            if valid_tree(tree, sun):
                print(f"GROW {tree.index}")
                return True

    if orange_trees:
        for tree in orange_trees:
            if valid_tree(tree, sun):
                print(f"GROW {tree.index}")
                return True
    
    return False

def grow_function_v2(day, sun):

    def applicate_a_grow(trees, sun):
        if trees:
            if valid_tree(trees[0], sun):
                print(f"GROW {trees[0].index}")
                return True
        return False

    ##   
    # Grow the trees with the size 2 in the last days
    ##
    if day > 18 and get_number_of_trees(2):
        green_trees = [tree for tree in get_trees_by_color('G') if tree.size == 2]
        if green_trees:
            if applicate_a_grow(green_trees, sun):
                return True
        yellow_trees = [tree for tree in get_trees_by_color('Y') if tree.size == 2]
        if yellow_trees:
            if applicate_a_grow(yellow_trees, sun):
                return True
        orange_trees = [tree for tree in get_trees_by_color('O') if tree.size == 2]
        if orange_trees:
            if applicate_a_grow(orange_trees, sun):
                return True


    green_trees = sorted(get_trees_by_color('G'), key=lambda tree: tree.index)
    yellow_trees = sorted(get_trees_by_color('Y'), key=lambda tree: tree.index)
    orange_trees = sorted(get_trees_by_color('O'), key=lambda tree: tree.index)

    medium_green = [tree for tree in green_trees if tree.size == 2]
    if applicate_a_grow(medium_green, sun):
        return True
    medium_yellow = [tree for tree in yellow_trees if tree.size == 2]
    if applicate_a_grow(medium_yellow, sun):
        return True

    small_green = [tree for tree in green_trees if tree.size == 1]
    if applicate_a_grow(small_green, sun):
        return True
    small_yellow = [tree for tree in yellow_trees if tree.size == 1]
    if applicate_a_grow(small_yellow, sun):
        return True
    seed_green = [tree for tree in green_trees if tree.size == 0]
    if applicate_a_grow(seed_green, sun):
        return True
    
    medium_orange = [tree for tree in orange_trees if tree.size == 2]
    if applicate_a_grow(medium_orange, sun):
        return True
    small_orange = [tree for tree in orange_trees if tree.size == 1]
    if applicate_a_grow(small_orange, sun):
        return True

    seed_yellow = [tree for tree in yellow_trees if tree.size == 0]
    if applicate_a_grow(seed_yellow, sun):
        return True
    seed_orange = [tree for tree in orange_trees if tree.size == 0]
    if applicate_a_grow(seed_orange, sun):
        return True

    return False

def seed_function():
    global SEED
    neighbors_index = set()
    for tree in MY_TREES:
        for neigh_index in tree.neighbors:
            neighbors_index.add(neigh_index)
    for seed in SEED:
        print(seed, file=sys.stderr, flush=True)

    new_seed = SEED
    SEED = []
    for seed in new_seed:
        if not int(seed.split(" ")[2]) in neighbors_index:
            SEED.append(seed)
    print("-----------------", file=sys.stderr, flush=True)
    for seed in SEED:
        print(seed, file=sys.stderr, flush=True)

    best_seed = best_seed_tree_and_index()
    if best_seed:
        green_seeds = get_green_seed(best_seed)
        if green_seeds:
            print(green_seeds[0])
            return True
        yellow_seeds = get_yellow_seed(best_seed)
        if yellow_seeds:
            print(yellow_seeds[0])
            return True
        orange_seeds = get_orange_seed(best_seed)
        if orange_seeds:
            print(orange_seeds[0])
            return True


    return False

FIERS_COMPLETE = 0
def silver_algorithme(sun, day):
    #complete
    #grow the best index green yellow orange
    #seed bets index
    #wait

    if COMPLETE:
        global FIERS_COMPLETE
        if get_number_of_trees(3) > 4 and FIERS_COMPLETE < 2:
            print(f"{COMPLETE[-1]}")
            FIERS_COMPLETE += 1
            return
        if day >= (19 - get_number_of_trees(3)) or get_number_of_trees(3) > 6:
            if sun >= 4:
                print(f"{COMPLETE[-1]}")
                return

    if GROW:
        if grow_function_v2(day, sun):
            return

    if SEED and (get_number_of_trees(0) + get_number_of_trees(1) < 2) and day <= 16:
        if seed_function():
            return
            
    
    print("WAIT Zzz")


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_of_cells = int(input())  # 37
cell_neighbors = []
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    cell_neighbors.append([neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5])


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
            tree = Tree(cell_index, size, is_dormant, cell_neighbors[cell_index])
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

    #print(MY_TREES[0].neighbors, file=sys.stderr, flush=True)
    
    silver_algorithme(sun, day)

    MY_TREES.clear()
    SEED.clear()
    GROW.clear()
    COMPLETE.clear()

