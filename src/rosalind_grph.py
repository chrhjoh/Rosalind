from rosalind_functions import get_args, fasta_reader
import numpy as np



def solution(headers, sequences):
    k = 3
    adjacency = []
    for i, seq1 in enumerate(sequences):
        for j , seq2 in enumerate(sequences):
            if i <= j:
                break
            
            if seq1[:k] == seq2[-k:]:
                
                adjacency.append([headers[j], headers[i]])

            if seq2[:k] == seq1[-k:]:
                adjacency.append([headers[i], headers[j]])

    return adjacency

        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:

        headers, sequences = fasta_reader('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)
        
    adjacent = solution(headers, sequences)

    for edge in adjacent:
        print(*edge)


if __name__ == '__main__':
    main()