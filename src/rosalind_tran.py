from rosalind_functions import fasta_reader, get_args


def solution(sequences: 'list[str]'):
    seq1 = sequences[0]
    seq2 = sequences[1]
    transversion = 0
    transition = 0
    for b1, b2 in zip(seq1, seq2):
        if (b1 == 'A' and b2 == 'G') or (b1 == 'G' and b2 == 'A'):
            transition += 1
        elif (b1 == 'C' and b2 == 'T') or (b1 == 'T' and b2 == 'C'):
            transition += 1
        elif (b1 == 'A' and b2 == 'T') or (b1 == 'T' and b2 == 'A'):
            transversion += 1
        elif (b1 == 'A' and b2 == 'C') or (b1 == 'C' and b2 == 'A'):
            transversion += 1
        elif (b1 == 'G' and b2 == 'C') or (b1 == 'C' and b2 == 'G'):
            transversion += 1
        elif (b1 == 'G' and b2 == 'T') or (b1 == 'T' and b2 == 'G'):
            transversion += 1
        
    return transition / transversion

        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)

    result = solution(sequences)

    print(f'{result:.8}')




if __name__ == '__main__':
    main()