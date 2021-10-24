from rosalind_functions import get_args
import math



def solution(dna, gc_contents):
    print(dna)
    probs = []
    for gc_prob in gc_contents:
        at_prob = (1-gc_prob) / 2 
        gc_prob = gc_prob / 2
        
        at_count = dna.count('A') + dna.count('T')
        gc_count = dna.count('C') + dna.count('G')
        
        prob = at_count * math.log10(at_prob) + gc_count * math.log10(gc_prob)
        probs.append(prob)
    return probs

        
def load_data(filename):
    with open(filename, 'r') as infile:
        dna = infile.readline()
        gc_contents = [float(x) for x in infile.readline().split()]
    return dna, gc_contents

def main():
    args = get_args()

    if args.testing:
        dna, gc_contents = load_data('data/rosalind_test.txt')
    else:
        dna, gc_contents = load_data(args.data_file)

    result = solution(dna, gc_contents)

    print(*result)




if __name__ == '__main__':
    main()