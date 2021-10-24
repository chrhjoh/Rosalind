from rosalind_functions import get_args
from itertools import product


def solution(alphabet : 'list[str]', n : int):

    return product(alphabet,repeat=n)

        
def load_data(filename):
    with open(filename, 'r') as f:
        alphabet = f.readline().split()
        n = int(f.readline().strip())
        
    return alphabet, n

def main():
    args = get_args()

    if args.testing:
        alphabet, n = load_data('data/rosalind_test.txt')
    else:
        alphabet, n = load_data(args.data_file)

    result = solution(alphabet, n)
    result = [''.join(res) for res in result]
    result.sort()
    print(*result, sep='\n')




if __name__ == '__main__':
    main()