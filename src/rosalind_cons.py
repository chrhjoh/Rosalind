from rosalind_functions import get_args, fasta_reader


def solution(sequences):
    counts = {'A' : [0]*len(sequences[0]),
              'C' : [0]*len(sequences[0]),
              'G' : [0]*len(sequences[0]),
              'T' : [0]*len(sequences[0])
    }
    for seq in sequences:
        for i, base in enumerate(seq):
            counts[base][i] += 1

    # Make mode string
    mode_str = ''
    for i in range(len(sequences[0])):
        max_count = 0
        for base in counts.keys():
            if counts[base][i] > max_count:
                max_count = counts[base][i]
                max_base = base
        mode_str += max_base
    print(mode_str)
    return counts
        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)


    result = solution(sequences)
    for base in result.keys():
        print(base+':',end=' ')
        print(*result[base])





if __name__ == '__main__':
    main()

