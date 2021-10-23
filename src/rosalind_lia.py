from rosalind_functions import get_args
from scipy.stats import binom
import math


def solution(n, k):
    pop = 2**k
    prob = 0
    for i in range(n):
        bin_coef = math.factorial(pop) / (math.factorial(i)* math.factorial(pop - i))
        prob += bin_coef * 0.25** i *0.75**(pop-i)
    return 1-prob

        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        n = 1
        k = 2
    else:
        data = load_data(args.data_file)
        (k, n) = [int(x) for x in data.split()]

    result = solution(n, k)
    print(result)




if __name__ == '__main__':
    main()