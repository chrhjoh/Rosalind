from rosalind_functions import get_args



def solution(seq1, seq2):
    mutation = 0
    for b1, b2 in zip(seq1, seq2):
        if b1 != b2:
            mutation += 1

    hamm = mutation
  
    return hamm

        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        (seq1, seq2) = 'GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT'.split()
    else:
        data = load_data(args.data_file)
        (seq1, seq2) = data.split()

    result = solution(seq1, seq2)
    print(result)




if __name__ == '__main__':
    main()