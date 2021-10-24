from rosalind_functions import fasta_reader, get_args


def solution(sequences: list, super_str : str = '' ):
    if len(super_str) == 0:
        super_str = sequences.pop(0)
        return solution(sequences, super_str)
    
    elif len(sequences) == 0:
        return super_str
    else:
        for i, seq in enumerate(sequences):
            for overlap in range(len(seq) // 2):
                q = len(seq) - overlap
                if super_str.startswith(seq[overlap:]):
                    sequences.pop(i)
                    return solution(sequences,seq[:overlap]+super_str)

                if super_str.endswith(seq[:q]):
                    sequences.pop(i)
                    return solution(sequences,super_str+seq[q:])
        return super_str

        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)

    result = solution(sequences)

    print(result)




if __name__ == '__main__':
    main()