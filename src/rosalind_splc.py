from rosalind_functions import get_args, fasta_reader
from tables import codon_table


def solution(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    rna = dna.replace('T', 'U')
    start = rna.find('AUG')
    peptide = ''
    for i in range(start, len(dna), 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            if codon_table[codon] == '':
                break
            peptide += codon_table[codon]

    return peptide
        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)

    dna = sequences[0]
    introns = sequences[1:]
        
    result = solution(dna, introns)
    print(result)





if __name__ == '__main__':
    main()