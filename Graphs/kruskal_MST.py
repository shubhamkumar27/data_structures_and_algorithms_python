from graph import Graph

def kruskal(graph):
    new = sorted(graph.edges, key=lambda x: x.value, reverse=False)
    # for q in new:
    #     print(q.value,q.node_from.value,q.node_to.value)
    mst = Graph()
    i=0
    n=len(graph.nodes)-1
    while(len(mst.edges)!=n):
        edge = new[i]
        ans = is_connected(mst,edge.node_from.value,edge.node_to.value)
        #print(ans)
        if not ans:
            mst.insert_edge(edge.value,edge.node_from.value,edge.node_to.value)
        i=i+1
    return mst

def is_connected(graph, n1,n2):
    #print(n1,n2)
    snode=None
    for nod in graph.nodes:
        #print(nod.value,n1)
        if nod.value == n1:
            snode = nod
            break
        if nod.value == n2:
            n1,n2=n2,n1
            snode = nod
            break
    if snode == None:
        return False
    v = []
    q = [snode]
    while q:
        ### Only this line changes ###
        n = q.pop(0)
        #print(n.value,'here')
        if n.value == n2:
            return True
        ###############################
        if n not in v:
            v.append(n)
            for nnode in n.edges:
                if nnode.node_to not in v:
                    q.append(nnode.node_to)
                if nnode.node_from not in v:
                    q.append(nnode.node_from)
    return False

graph = Graph()
graph.insert_edge(4, 'B', 'A')
graph.insert_edge(8, 'B', 'C')
graph.insert_edge(7, 'C', 'D')
graph.insert_edge(9, 'D', 'E')
graph.insert_edge(10, 'E', 'F')
graph.insert_edge(2, 'F', 'G')
graph.insert_edge(1, 'G', 'H')
graph.insert_edge(11, 'B', 'H')
graph.insert_edge(8, 'H', 'A')
graph.insert_edge(7, 'H', 'I')
graph.insert_edge(6, 'G', 'I')
graph.insert_edge(2, 'C', 'I')
graph.insert_edge(4, 'C', 'F')
graph.insert_edge(14, 'D', 'F')
#graph.adjacency_list()
m=kruskal(graph)
m.adjacency_list()