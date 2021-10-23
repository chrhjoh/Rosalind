from rosalind_functions import get_args
import math


def solution(n, k):
    return int(math.factorial(n) / math.factorial(n-k))

        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        n = 21
        k = 7
    else:
        data = load_data(args.data_file)
        (n, k) = [int(x) for x in data.split()]

    result = solution(n, k)
    print(result % 1000000)




if __name__ == '__main__':
    main()