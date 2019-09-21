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
        ### Only this line changes ###
        n = q.pop(0)
        ###############################
        if n not in v:
            v.append(n)
            print(n.value)
            for nnode in n.edges:
                if nnode.node_to not in v:
                    q.append(nnode.node_to)
                if nnode.node_from not in v:
                    q.append(nnode.node_from)
    return

def dfs(graph, node):
    snode = None
    for nod in graph.nodes:
        if nod.value == node:
            snode = nod
    if snode == None:
        return print('Node not found')
    v = []
    q = [snode]
    while q:
        ### Only this line changes ###
        n = q.pop()
        ##############################
        if n not in v:
            v.append(n)
            #print(n.value)
            for nnode in n.edges:
                if nnode.node_to not in v:
                    print(nnode.node_to.value)
                    q.append(nnode.node_to)
                # if nnode.node_from not in v:
                #     q.append(nnode.node_from)
    return


graph = Graph()
graph.insert_edge(100, 'B', 'A')
graph.insert_edge(101, 'B', 'D')
graph.insert_edge(102, 'B', 'E')
graph.insert_edge(103, 'A', 'C')
graph.insert_edge(103, 'A', 'F')
graph.insert_edge(103, 'C', 'F')
graph.insert_edge(103, 'F', 'E')
for i in graph.nodes:
    print(i.value)
print('##########################')
bfs(graph, 'B')
print('##########################')
dfs(graph, 'B')