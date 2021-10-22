from load_args import get_args



def solution(n, k, sequence=[]):
    
    
    if len(sequence) < 2:
        sequence += [1, 1]

    else:
        sequence += [sequence[-2] * k + sequence[-1]]
    
    if len(sequence) < n:
        solution(n, k, sequence)
  
    return sequence

        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        n = 5
        k = 3
    else:
        data = load_data(args.data_file)
        (n, k) = [int(x) for x in data.split()]

    result = solution(n, k)
    print(result[-1])




if __name__ == '__main__':
    main()