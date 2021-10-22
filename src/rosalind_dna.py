from load_args import get_args
import sys

class Solution:
    
    # Actual solution
    def count_dna(self) -> list:
        return [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data





if __name__ == '__main__':
    args = get_args()

    if args.testing:
        dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    else:
        dna = load_data(args.data_file)

    solution = Solution()
    result = solution.count_dna()
    print(*result)

