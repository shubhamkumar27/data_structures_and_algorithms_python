class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)

    def insert_edge(self,value,node_from, node_to):
        from_node = to_node = None
        for n in self.nodes:
            if node_from == n.value:
                from_node = n
            if node_to == n.value:
                to_node = n
        if from_node == None:
            from_node = Node(node_from)
            self.nodes.append(from_node)
        if to_node == None:
            to_node = Node(node_to)
            self.nodes.append(to_node)
        edge = Edge(value,from_node,to_node)
        from_node.edges.append(edge)
        to_node.edges.append(edge)
        self.edges.append(edge)

    def adjacency_matrix(self):
        pass

    def bfs(self,node):
        snode = None
        for nod in self.nodes:
            if nod.value == node:
                snode = nod
        if snode == None:
            return 'Node not found'
        v = []
        q = [snode]
        while q:
            n = q.pop(0)
            if n not in v:
                v.append(n)
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
l = graph.bfs('B')
for i in l:
    print(i.value)


