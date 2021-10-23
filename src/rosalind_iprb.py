from rosalind_functions import get_args



def solution(k, m, n):
    pop = k + m + n

    rec_rec = n / pop * (n - 1)/(pop -1)
    het_rec = m / pop * n /(pop - 1) + n / pop * m /(pop - 1)
    het_het = m / pop * (m - 1)/(pop -1)

    return 1 - (rec_rec + 1/4 * het_het + 1/2 * het_rec)
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        n = 2
        m = 2
        k = 2
    else:
        data = load_data(args.data_file)
        (k, m, n) = [int(x) for x in data.split()]

    result = solution(k, m, n)
    print(f'{result:.5f}')




if __name__ == '__main__':
    main()