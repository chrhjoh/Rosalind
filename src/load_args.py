from argparse import ArgumentParser, Namespace

def get_args() -> Namespace:
    '''
    Get commandline arguments for the rosalind programs regarding data positions 
    '''
    parser = ArgumentParser()
    parser.add_argument('-dat', action='store', dest='data_file', type=str,  help='File containing data')
    parser.add_argument('-test', action='store_true', dest='testing', default=False, help='Whether to use testing data or real data')

    return parser.parse_args()

    