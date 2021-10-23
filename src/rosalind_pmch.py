from rosalind_functions import get_args, fasta_reader
import math


def solution(rna):
    au_count = rna.count('A') 
    cg_count = rna.count('C')

    return math.factorial(au_count)* math.factorial(cg_count)

    
        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
        
    else:
        headers, sequences = load_data(args.data_file)

    
    result = solution(sequences[0])

    print(result)

if __name__ == '__main__':
    main()