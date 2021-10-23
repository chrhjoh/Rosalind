from rosalind_functions import get_args, fasta_reader
import numpy as np



def solution(headers, sequences):
    gc_content = np.zeros((len(sequences)))
    for i, seq in enumerate(sequences):
        for base in seq:
            if base in ['G', 'C']:
                gc_content[i] += 1

        gc_content[i] = gc_content[i] / len(seq) * 100

    idx = np.argmax(gc_content)

    return headers[idx], gc_content[idx]

        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing: # Not implemented

        headers, sequences = fasta_reader('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)
        
    header, sequence = solution(headers, sequences)
    print(header, sequence, sep='\n')




if __name__ == '__main__':
    main()