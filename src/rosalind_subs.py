from rosalind_functions import get_args


def solution(seq, motif):
    idx = 0
    indexes = []
    while idx != -1:
        idx = seq.find(motif,idx+1)
        if idx != -1:
            indexes.append(idx+1)


    return indexes
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        seq, motif = 'GATATATGCATATACTT\nATAT'.split()
    else:
        seq, motif = load_data(args.data_file).split()

    result = solution(seq, motif)
    print(*result)




if __name__ == '__main__':
    main()