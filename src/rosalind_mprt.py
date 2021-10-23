from rosalind_functions import get_args
import re
from urllib.request import urlopen





def solution(id):
    n_glyc = re.compile(b'(?=(N[^P][ST][^P]))')
    
    link = f"https://www.uniprot.org/uniprot/{id}.fasta"
    with urlopen(link) as f:
        fasta = f.read().strip()
    seq = fasta.split(b'\n')[1:]
    result = n_glyc.finditer(b''.join(seq))
    idxs = [x.start() + 1 for x in result]

    if len(idxs) > 0:
        print(id)
        print(*idxs)
        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read()
    return data

def main():
    args = get_args()

    if args.testing:
        u_id = 'A2Z669\nB5ZC00\nP07204_TRBM_HUMAN\nP20840_SAG1_YEAST'.split()
    else:
        u_id = load_data(args.data_file).split()

    for id in u_id:
        solution(id)




if __name__ == '__main__':
    main()


