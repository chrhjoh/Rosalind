from rosalind_functions import get_args, fasta_reader
from tables import codon_table


def solution(sequences):
    max_length = 0
    for i in range(len(sequences[0])):
        for j in range(max_length+i, len(sequences[0])):
            motif = sequences[0][i:j+1]
            
            present = True
            for seq in sequences[1:]:
                if seq.find(motif) == -1:
                    present = False
                    break
            if present:
                max_motif = motif
                max_length = len(motif)


    return max_motif
        
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