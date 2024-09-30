import math
import os
from binary_tree import BinaryTree
'''
Inputs: Symbols(probabilities, code)
Oputput: K, L, n, H(X)
'''


# ----------------------------------------------------------------------------------------------------------------
# INSERT HERE EACH SYMBOL PROBABILITY AND CODE AS PYTHON TUPLES

# EXAMPLE: symbol_list = [('x1', 0.1, '00'), ('x2', 0.2, '01'), ('x3', 0.3, '10'), ('x4', 0.4, '11')]
symbol_list = [(0.5, '0'), (0.25, '01'), (0.125, '011'), (0.125, '0111'), (0.125, '01100'), (0.125, '01000')]
# ----------------------------------------------------------------------------------------------------------------



tree = BinaryTree()
for symbol in symbol_list:
    tree.insert(symbol[1])

def entropy():
    global symbol_list
    H = 0
    for symbol in symbol_list:
        H += symbol[0] * math.log2(1 / symbol[0])
    return H

def average_length():
    global symbol_list
    L = 0
    for symbol in symbol_list:
        L += symbol[0] * len(symbol[1])
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
        k += 2 ** -len(symbol[1])
    return k

def print_tree():
    global tree
    tree.draw()


def main():
    os.system('cls')

    global symbol_list
    H = entropy()
    L = average_length()
    n = efficiency()
    K = kraft_inequality()

    print("-------------------Parametros de alfabeto-------------------")
    print(f"S = {len(symbol_list)}")
    print(f"H(X) = {H}\n")
    print("-------------------Parametros del codigo--------------------")
    print(f"L = {L}")
    print(f"n = {n}")
    print(f"K = {K}\n")

    print("-----------------Representacion del codigo------------------")
    print_tree()

if __name__ == '__main__':
    main()