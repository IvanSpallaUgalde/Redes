import math

def shannon_fano(probabilities):
    # Sort probabilities in descending order
    probabilities = sorted(probabilities, reverse=True)
    
    # Calculate the code lengths
    lengths = [math.ceil(-math.log2(p)) for p in probabilities]
    
    # Assign code words
    codes = []
    current_code = 0
    for length in lengths:
        code = format(current_code, f'0{length}b')
        codes.append(code)
        current_code += 1
    
    # Generate the list of (probability, length, code) tuples
    result = [(prob, length, code) for prob, length, code in zip(probabilities, lengths, codes)]
    return result

def calculations(shannon):
    # Entropy
    H=0
    for symbol in shannon:
        H += symbol[0] * math.log2(1 / symbol[0])
    
    # Average length
    L=0
    for symbol in shannon:
        L += symbol[0] * len(symbol[2])
    
    # Efficiency
    E = H / L

    # Kraft inequality
    K=0
    for symbol in shannon:
        K += 2 ** -len(symbol[2])

    return H, L, E, K