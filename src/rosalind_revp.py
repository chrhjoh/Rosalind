from rosalind_functions import get_args, fasta_reader, rev_comp


def solution(sequences):
    idxs = []
    for i in range(len(sequences[0])):
        for j in range(4, min(13,len(sequences[0])-i + 1)):
            motif = sequences[0][i:i+j]
            if motif == rev_comp(motif):
                idxs.append([i+1,j])
    return idxs
        
def load_data(filename):
    
    return fasta_reader(filename)

def main():
    args = get_args()

    if args.testing:
        headers, sequences = load_data('data/rosalind_test.txt')
        
    else:
        headers, sequences = load_data(args.data_file)

    
    result = solution(sequences)
    for res in result:
        print(*res)

if __name__ == '__main__':
    main()