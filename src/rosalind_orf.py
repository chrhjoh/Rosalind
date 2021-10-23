from rosalind_functions import get_args, fasta_reader
from tables import codon_table


def solution(sequences):
    peptides = set()
    for seq in sequences:
        seq = seq.replace('T', 'U')
        start_idx = seq.find('AUG')
        productive = False
        while start_idx != -1:
            peptide = ''
            for i in range(start_idx, len(seq), 3):
                codon = seq[i:i+3]
                if len(codon) < 3:
                    break
                elif codon_table[codon] == '':
                    productive = True
                    break
                peptide += codon_table[codon]
            
            if productive:
                peptides.add(peptide)

            start_idx = seq.find('AUG', start_idx+1)
            productive = False

    return peptides
        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
    else:
        headers, sequences = load_data(args.data_file)

    rev_seqs = []
    trans_table = str.maketrans('ACTG', 'TGAC')
    for seq in sequences:
        rev_seqs.append(seq.translate(trans_table)[::-1])
    sequences += rev_seqs
        
    result = solution(sequences)
    print(*result, sep='\n')





if __name__ == '__main__':
    main()
