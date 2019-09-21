from graph import Graph

def topological_sort(graph):
    visited=[]
    stack=[]
    for i in graph.nodes:
        print(i.value)
        if i not in visited:
            topological_util(i,graph,visited,stack)
    return stack


def topological_util(j,graph,vis,stack):
    vis.append(j)
    for edge in j.edges:
        if edge.node_to not in vis:
            topological_util(edge.node_to,graph,vis,stack)
    stack.insert(0,j)


graph = Graph()
graph.insert_edge(100, 5, 0)
graph.insert_edge(101, 5, 2)
graph.insert_edge(103, 4, 0)
graph.insert_edge(103, 4, 1)
graph.insert_edge(102, 2, 3)
graph.insert_edge(103, 3, 1)
graph.insert_edge(103, 1, 5)
#graph.insert_edge(103, 'F', 'E')
lis = topological_sort(graph)
print('############')
for i in lis:
    print(i.value)
