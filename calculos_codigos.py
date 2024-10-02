import math
import os
from binary_tree import BinaryTree
from huffman import get_sorted_huffman_codes
from shannon_fano import calculations, shannon_fano
'''
Inputs: Symbols(probabilities, code)
Oputput: K, L, n, H(X)
'''


# ----------------------------------------------------------------------------------------------------------------
# INSERT HERE EACH SYMBOL PROBABILITY AND CODE AS PYTHON TUPLES

# EXAMPLE: symbol_list = [(0.1, '00'), (0.2, '01'), (0.3, '10'), (0.4, '11')]
symbol_list = [(0.2, '000', 'a'), (0.15, '001', 'b'), (0.05, '010', 'c'), (0.15, '011', 'd'), (0.45, '1', 'e')]
# ----------------------------------------------------------------------------------------------------------------



tree = BinaryTree()
for symbol in symbol_list:
    tree.insert(symbol[1])

if symbol_list[0][2] is not None:
    list_2 = []
    for symbol in symbol_list:
        list_2.append((symbol[0], symbol[2]))


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

def huffman():
    global list_2
    if list_2[0] is not None:
        huffman_code = get_sorted_huffman_codes(list_2)
        for item in huffman_code:
            print(item)
    
def shannon_fano_list():
    shannon = []
    for symbol in symbol_list:
        shannon.append(symbol[0])
    list = shannon_fano(shannon)
    return list

def print_shannon():
    shannon = shannon_fano_list()
    H_s, L_s, n_s, K_s = calculations(shannon)
    print(shannon)
    print(f"H(X) = {H_s}")
    print(f"L = {L_s}")
    print(f"n = {n_s}")
    print(f"K = {K_s}")

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
    print("-------------------Codigo de Huffman------------------------")
    huffman()
    print("-------------------Codigo de Shannon-Fano-------------------")
    print_shannon()

    # Print the binary tree (original code)
    print_tree()
    

if __name__ == '__main__':
    main()