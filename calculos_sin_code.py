import math
import os

# list of symbols (Example: [0.5, 0.25, 0.125, 0.125])
list=[0.5, 0.25, 0.125, 0.125]

def entropy():
    global list
    H = 0
    for prob in list:
        H += prob * math.log2(1 / prob)
    return H

if __name__ == "__main__":
    os.system('cls')

    H = entropy()
    print(f"H(X) = {H}\n")