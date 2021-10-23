from rosalind_functions import get_args



def solution(nodes, edges):
    clusters = [{x} for x in nodes]

    for edge in edges:
        updated_clusts = []
        for i, cluster in enumerate(clusters):
            # Update all clusters and note which clusters are updated
            if edge[0] in cluster or edge[1] in cluster:
                cluster.add(edge[1])
                updated_clusts.append(i)

        # generate new cluster by combining the updated clusters and then remove them
        new_clust = set()
        for i in updated_clusts:
            new_clust = new_clust.union(clusters[i])
        for index in sorted(updated_clusts, reverse=True):
            del clusters[index]
        clusters.append(new_clust)
    # minimum number of edges is number of clusters - 1
    return len(clusters) - 1

                
                
    
    print(clusters)
            



        
def load_data(filename):
    with open(filename, 'r') as infile:
        data = infile.read().split('\n')
    return data[0], data[1:]

def main():
    args = get_args()

    if args.testing:
        n, edges = load_data('data/rosalind_test.txt')
    else:
        n, edges = load_data(args.data_file)

    nodes = [x+1 for x in range(int(n))]
    edges = [list(map(int, edge.split())) for edge in edges]
    result = solution(nodes, edges)
    print(result)




if __name__ == '__main__':
    main()