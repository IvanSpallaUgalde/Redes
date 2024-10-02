import math


# List of forward probs
fwd_probs = [
    [0.72, 0.04, 0.15, 0.09],
    [0.12, 0.75, 0.00, 0.13],
    [0.07, 0.08, 0.82, 0.03]
]

# List of backward probs
bck_probs = [
]

# List of x probs
x_probs = []

# List of y probs
y_probs = []

def error_term_fwd():
    H = entropy()
    I = mean_info_mutua_fwd()
    return H - I

def entropy():
    H = 0
    for i in range(len(x_probs)):
        H += x_probs[i] * math.log2(1 / x_probs[i])
    return H

def get_prob_succes():
    s = 0
    for i in range(len(x_probs)):
        s += x_probs[i] * fwd_probs[i][i]

def get_y_prob():
    for j in range(len(fwd_probs[0])):
        y_prob = 0
        for i in range(len(x_probs)):
            y_prob += x_probs[i] * fwd_probs[i][j]
        y_probs.append(y_prob)

def bayes_back_to_fwd():
    pass

def mean_info_mutua_fwd():
    for i in range(len(x_probs)):
        for j in range(len(y_probs)):
            I += x_probs[i] * fwd_probs[i][j] * math.log2(fwd_probs[i][j] / y_probs[j])
    return I


def main():
    pass
    

if __name__ == '__main__':
    main()