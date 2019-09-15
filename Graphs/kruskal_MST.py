from graph import Graph

def kruskal(graph):
    new = sorted(graph.edges, key=lambda x: x.value, reverse=False)
    mst = Graph()
    i=0
    n=len(graph.nodes)-1
    while(len(mst.edges)!=n):
        edge = new[i]
        #print(edge.value,edge.node_from.value,edge.node_to.value)
        mst.insert_edge(edge.value,edge.node_from,edge.node_to)
        i=i+1
    return mst

graph = Graph()
graph.insert_edge(100, 'B', 'A')
graph.insert_edge(101, 'B', 'D')
graph.insert_edge(102, 'B', 'E')
graph.insert_edge(103, 'A', 'C')
graph.insert_edge(109, 'A', 'F')
graph.insert_edge(105, 'C', 'F')
graph.insert_edge(104, 'F', 'E')
graph.adjacency_list()
m=kruskal(graph)
m.adjacency_list()