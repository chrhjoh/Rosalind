from rosalind_functions import get_args



def solution_inc(seq : 'list[int]', n : int):

    p = [None] * n
    m = [None] * n
    m[0] = 0
    l = 1

    for i in range(n):
        low = 0
        high = l
        
        if seq[m[high-1]] < seq[i]:
            j = high
        
        else:
            while high - low > 1:
                mid = (high + low) // 2
                if seq[m[mid-1]] < seq[i]:
                    low = mid
                else:
                    high = mid

            j = low

        p[i] = m[j-1]
        if j == l or seq[i] < seq[m[j]]:
            m[j] = i
            l = max(l, j+1)

        result = []
        pos = m[l-1]
        for _ in range(l):
            result.append(seq[pos])
            pos = p[pos]

        
    return result[::-1]

def solution_dec(seq : 'list[int]', n : int):

    p = [None] * n
    m = [None] * n
    m[0] = 0
    l = 1

    for i in range(n):
        low = 0
        high = l
        
        if seq[m[high-1]] > seq[i]:
            j = high
        
        else:
            while high - low > 1:
                mid = (high + low) // 2
                if seq[m[mid-1]] > seq[i]:
                    low = mid
                else:
                    high = mid

            j = low

        p[i] = m[j-1]
        if j == l or seq[i] > seq[m[j]]:
            m[j] = i
            l = max(l, j+1)

        result = []
        pos = m[l-1]
        for _ in range(l):
            result.append(seq[pos])
            pos = p[pos]

        
    return result[::-1]


        
def load_data(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        sequence = [int(x) for x in f.readline().strip().split()]
        
    return sequence, n

def main():
    args = get_args()

    if args.testing:
        sequence, n = load_data('data/rosalind_test.txt')
    else:
        sequence, n = load_data(args.data_file)

    forward = solution_inc(sequence, n)
    reverse = solution_dec(sequence, n)
    
 
    print(*forward)
    print(*reverse)




if __name__ == '__main__':
    main()