from rosalind_functions import fasta_reader, get_args


def solution(sequences: list):
    idxs = []
    dna = sequences[0]
    motif = sequences[1]
    current_pos = 0
    for m in motif:
        for i in range(current_pos, len(dna)):
            if m == dna[i]:
                idxs.append(i+1)
                current_pos = i+1
                break


    return idxs

        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)

    result = solution(sequences)

    print(*result)




if __name__ == '__main__':
    main()