from rosalind_functions import get_args



def solution(aaaa, aaab, aabb, abab, abbb, bbbb):


    return 2* (aaaa + aaab + aabb + abab * 3/4 + abbb * 1/2+ bbbb*0)
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        aaaa, aaab, aabb, abab, abbb, bbbb = [int(x) for x in '1 0 0 1 0 1'.split()]
    else:
        data = load_data(args.data_file)
        aaaa, aaab, aabb, abab, abbb, bbbb = [int(x) for x in data.split()]

    result = solution(aaaa, aaab, aabb, abab, abbb, bbbb)
    print(f'{result:.1f}')




if __name__ == '__main__':
    main()