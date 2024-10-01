import heapq
import math
from collections import defaultdict

class HuffmanNode:
    def __init__(self, probability, symbol=None, left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right

    # Define comparison operators for the priority queue
    def __lt__(self, other):
        return self.probability < other.probability

def create_huffman_tree(symbol_list):
    # Create a priority queue (min-heap)
    heap = [HuffmanNode(probability, symbol) for probability, symbol in symbol_list]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.probability + right.probability, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}

    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        generate_huffman_codes(node.left, prefix + '0', codebook)
        generate_huffman_codes(node.right, prefix + '1', codebook)

    return codebook


def get_sorted_huffman_codes(symbol_list):
    # Create the Huffman tree
    huffman_tree = create_huffman_tree(symbol_list)

    # Generate the Huffman codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Sort the Huffman codes alphabetically by symbol
    sorted_huffman_codes = sorted(huffman_codes.items())

    return sorted_huffman_codes
