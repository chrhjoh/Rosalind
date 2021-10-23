from tables import n_codons
from rosalind_functions import get_args


def solution(peptide):
    combinations = 1
    for aa in peptide:
       combinations *= n_codons[aa]
    combinations *= n_codons['']
    return combinations
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return data

def main():
    args = get_args()

    if args.testing:
        peptide = 'MA'
    else:
        peptide = load_data(args.data_file)

    result = solution(peptide)
    print(result % 1000000)




if __name__ == '__main__':
    main()

