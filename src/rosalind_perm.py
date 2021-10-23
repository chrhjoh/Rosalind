from rosalind_functions import get_args
from itertools import permutations



def solution(nums):
    return [x for x in permutations(nums, len(nums))]

    return 
        
def load_data(filename):
    with open(filename, 'r') as infile:
        n = int(infile.read())
    return n

def main():
    args = get_args()

    if args.testing:
        n = 3
    else:
        n = load_data(args.data_file)

    nums = [x+1 for x in range(n)]
        
    result = solution(nums)
    print(len(result))
    for perm in result:
        print(*perm)




if __name__ == '__main__':
    main()