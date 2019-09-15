from graph import Graph

def kruskal(graph):
    new = sorted(graph.edges, key=lambda x: x.value, reverse=False)
    mst = Graph()
    print(mst.nodes)
    print(graph.nodes)
    i=0
    n=len(graph.nodes)-1
    while(len(mst.edges)!=n):
        print(i)
        #print(len(graph.nodes)-1)
        print(len(mst.edges))
        edge = new[i]
        mst.insert_edge(edge.value,edge.node_from,edge.node_to)
        i=i+1
    mst.adjacency_list()

graph = Graph()
graph.insert_edge(100, 'B', 'A')
graph.insert_edge(101, 'B', 'D')
graph.insert_edge(102, 'B', 'E')
graph.insert_edge(103, 'A', 'C')
graph.insert_edge(109, 'A', 'F')
graph.insert_edge(105, 'C', 'F')
graph.insert_edge(104, 'F', 'E')
kruskal(graph)