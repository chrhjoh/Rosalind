from load_args import get_args

class Solution:
    
    # Actual solution
    def count_dna(self, dna) -> list:
        return [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    else:
        dna = load_data(args.data_file)

    solution = Solution()
    result = solution.count_dna(dna)
    print(*result)




if __name__ == '__main__':
    main()

