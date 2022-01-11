from rosalind_functions import get_args, fasta_reader
from collections import Counter
from math import factorial



def solution(sequence):
    c = Counter(sequence)

    au_pair = factorial(max(c['A'], c['U'])) / factorial(max(c['A'], c['U']) - min(c['A'], c['U']))
    gc_pair = factorial(max(c['G'], c['C'])) / factorial(max(c['G'], c['C']) - min(c['G'], c['C']))
    return au_pair * gc_pair

        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing: # Not implemented

        headers, sequences = fasta_reader('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)
        
    result = solution(sequences[0])
    print(int(result))




if __name__ == '__main__':
    main()