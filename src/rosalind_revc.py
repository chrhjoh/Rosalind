from rosalind_functions import get_args


def solution(dna):
    trans = str.maketrans('ACTG', 'TGAC')

    return dna.translate(trans)[::-1]
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        dna = 'AAAACCCGGT'
    else:
        dna = load_data(args.data_file)

    result = solution(dna)
    print(result)




if __name__ == '__main__':
    main()