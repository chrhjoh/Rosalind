from tables import codon_table
from rosalind_functions import get_args


def solution(rna):
    peptide = ''
    for i in range(0,len(rna), 3):
        peptide += codon_table[rna[i:i+3]]

    return peptide
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return data

def main():
    args = get_args()

    if args.testing:
        rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    else:
        rna = load_data(args.data_file)

    result = solution(rna)
    print(result)




if __name__ == '__main__':
    main()

