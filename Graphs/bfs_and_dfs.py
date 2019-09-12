from graph import Graph


def bfs(graph, node):
    snode = None
    for nod in graph.nodes:
        if nod.value == node:
            snode = nod
    if snode == None:
        return print('Node not found')
    v = []
    q = [snode]
    while q:
        n = q.pop(0)
        if n not in v:
            v.append(n)
            print(n.value)
            for nnode in n.edges:
                if nnode.node_to not in v:
                    q.append(nnode.node_to)
    return v


graph = Graph()
graph.insert_edge(100, 'B', 'A')
graph.insert_edge(101, 'B', 'D')
graph.insert_edge(102, 'B', 'E')
graph.insert_edge(103, 'A', 'C')
graph.insert_edge(103, 'A', 'F')
graph.insert_edge(103, 'C', 'F')
graph.insert_edge(103, 'F', 'E')
bfs(graph, 'B')