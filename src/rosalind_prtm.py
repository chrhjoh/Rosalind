from tables import aa_weight
from rosalind_functions import get_args


def solution(peptide):
    _sum = 0
    for aa in peptide:
        _sum += aa_weight[aa]
    return _sum
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return data

def main():
    args = get_args()

    if args.testing:
        peptide = 'SKADYEK'
    else:
        peptide = load_data(args.data_file)

    result = solution(peptide)
    print(f'{result:.3f}')




if __name__ == '__main__':
    main()
