import math
import os
from binary_tree import BinaryTree
'''
Inputs: Symbols(probabilities, code)
Oputput: K, L, n, H(X)
'''
# INSERT HERE EACH SYMBOL PROBABILITY AND CODE AS PYTHON TUPLES

# EXAMPLE: symbol_list = [('x1', 0.1, '00'), ('x2', 0.2, '01'), ('x3', 0.3, '10'), ('x4', 0.4, '11')]
symbol_list = [('a', 0.2, '000'), ('b', 0.15, '001'), ('c', 0.05, '010'), ('d', 0.15, '011'), ('e', 0.45, '1')]
tree = BinaryTree()

# Tree creation
for symbol in symbol_list:
    tree.insert(symbol[2])

# -----------------------------------------------Entropy calculation-----------------------------------------------
def entropy():
    global symbol_list
    H = 0
    for symbol in symbol_list:
        H += symbol[1] * math.log2(1 / symbol[1])
    return H

def average_length():
    global symbol_list
    L = 0
    for symbol in symbol_list:
        L += symbol[1] * len(symbol[2])
    return L

def efficiency():
    global symbol_list
    H = entropy()
    L = average_length()
    return H / L

def kraft_inequality():
    global symbol_list
    k = 0
    for symbol in symbol_list:
        k += 2 ** -len(symbol[2])
    return k

def print_tree():
    global tree
    tree.draw()


def main():
    os.system('cls')

    print('Results: ')
    global symbol_list
    H = entropy()
    L = average_length()
    n = efficiency()
    K = kraft_inequality()

    #print_tree()

    print(f"H(X) = {H}")
    print(f"L = {L}")
    print(f"n = {n}")
    print(f"K = {K}")

if __name__ == '__main__':
    main()