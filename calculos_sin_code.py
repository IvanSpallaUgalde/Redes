import math
import os

from huffman import get_sorted_huffman_codes
from shannon_fano import calculations, shannon_fano

# list of symbols (Example: [0.5, 0.25, 0.125, 0.125])
list=[(0.36, 'x1'), (0.14, 'x2'), (0.13, 'x3'), (0.12, 'x4'), (0.1, 'x5'), (0.09, 'x6'), (0.04, 'x7'), (0.02, 'x8'), (0.01, 'x9'), (0.01, 'x10')]

def entropy():
    global list
    H = 0
    for prob in list:
        H += prob[0] * math.log2(1 / prob[0])
    return H

def shannon_fano_list():
    global list
    shannon = []
    for symbol in list:
        shannon.append(symbol[0])
    list = shannon_fano(shannon)
    return list

def print_shannon():
    shannon = shannon_fano_list()
    H_s, L_s, n_s, K_s = calculations(shannon)
    print(shannon)
    print(f"\nH(X) = {H_s}")
    print(f"L = {L_s}")
    print(f"n = {n_s}")
    print(f"K = {K_s}")

def huffman():
    global list
    if list[0] is not None:
        huffman_code = get_sorted_huffman_codes(list)
        for item in huffman_code:
            print(item)


if __name__ == "__main__":
    os.system('cls')

    H = entropy()
    print('-------------------Entropy----------------------\n')
    print(f"H(X) = {H}\n")

    print('-------------------Huffman----------------------\n')
    huffman()

    print('-----------------Shannon-Fano-------------------\n')
    print_shannon()