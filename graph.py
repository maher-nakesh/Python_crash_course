class DirectedGraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, src, dest):
        if src not in self.nodes:
            self.add_node(src)

        if dest not in self.nodes:
            self.add_node(dest)

        adjacent_nodes = self.edges[src]

        if dest in adjacent_nodes:
            return

        self.edges[src].append(dest)
    
    def adjacent_nodes(self, node):
        return self.edges.get(node, [])
    
    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del(self.edges[node])
        
        for _, adjacent_nodes in self.edges.items():
            if node in adjacent_nodes:
                adjacent_nodes.remove(node)
				
#-----------------------------------------------------------
def dfs(graph,start,end,path,shortest):
path=path+[start]
if start== end :
	return path
for node in graph.adjacent_nodes(start):
	if node in path:
		countinue
	if shortest in None or len(path) + 1 <len(shortest):
		new_path = Dfs(graph,node,end,path,shortest)
		if new_path is not None:
			shortest-=new_path
	return shortest
#________________________________________________
def bfs (graph, start,end):
    init_path=[start]
    path_queue=[init_path]
    while len(path_queue) != 0 :
        path= path_queue.pop(0)
        last_node=path[-1]
        if last_node == end :
            return path
        for next_node in graph.adjacent_nodes(last_node):
            if next_node in path :
                continue
            new_path= path +[next_node]
            path_queue.append(new_path)
    return None