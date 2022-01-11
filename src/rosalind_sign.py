from rosalind_functions import get_args
from itertools import permutations, product


def solution(n : int):
    result = []
    for perm in permutations([x + 1 for x in range(n)]):
        for sign in product([1, -1], repeat=n):
            result.append([s * p for s, p in zip(sign, perm)])
    return result

        
def load_data(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        
    return n

def main():
    args = get_args()

    if args.testing:
        n = load_data('data/rosalind_test.txt')
    else:
        n = load_data(args.data_file)

    result = solution(n)
    print(len(result))
    [print(*res) for res in result]




if __name__ == '__main__':
    main()