#problem6______________________:
class DirectedGraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def getVertices(self):
        return list(self.edges.keys())

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

    def getEdges(self):
        edgename = []
        for vrtx in self.edges:
            for nxtvrtx in self.edges[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append([vrtx, nxtvrtx])
        return edgename

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del(self.edges[node])


def find_edge(edges):
 
    q= []#//error is here should be defaultdict(list)
    for c, t in edges:
        q[c].append(t)
        q[t].append(c)

    visited = set()
    group = set()
    parents = {}
    down = {}

    def dfs(id, node, parent):
        visited.add(node)
        parents[node] = parent
        numEdges = 0
        down[node] = id

        for o in q[node]:
            if o == parent:
                continue
            if o not in visited:
                parents[o] = node
                numEdges += 1
                dfs(id + 1, o, node)

            down[node] = min(down[node], down[o])

            if id <= down[o]:
                if parents[node] != -1:
                    group.add(node)

        if (parents[node] == -1 and numEdges >= 2):
            group.add(node)

    dfs(0, 0, -1)
    return group

graph =  [[1,0], [0,2], [2,1], [0,3], [3,4]]

g = DirectedGraph()
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)


g.add_edge(1,0)
g.add_edge(0,2)
g.add_edge(2,1)
g.add_edge(0,3)
g.add_edge(3,4)


f=g.getEdges()
print(f)
print(find_edge(f))
#=============================================================================
#problem4______________________:
def restricted_permutations(s):
    if(len(s)==1):
        return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in restricted_permutations(s[:i]+s[i+1:])]

    return result

print('\n'.join(restricted_permutations('abc')))
#==============================================================================
#problem5______________________:
def minimum_path(start, destination, maze):
    num_rows = len(maze)
    num_cols = len(maze[0])
    end_pt = (num_cols - 1, destination)
    start_pt = (start, num_rows - 1)
    visited = {end_pt: None}
    queue = [end_pt]
    
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []

        current_col, current_row = current
        #will go up here
        if current_row > 0:
            if maze[current_row - 1][current_col] == " ":
                adj_points.append((current_col, current_row - 1))
        #will go RIGHT
        if current_col < (len(maze[0])-1):
            if maze[current_row][current_col + 1] == " ": 
                adj_points.append((current_col + 1, current_row))
        #will go DOWN
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == " ":
                adj_points.append((current_col, current_row + 1))
        #will go LEFT
        if current_col > 0:
            if maze[current_row][current_col - 1] == " ":
                adj_points.append((current_col - 1, current_row))

        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)

maze = [[' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '], 
        [' ', '#', ' ', '#', ' '], 
        [' ', '#', ' ', '#', ' '], 
        [' ', '#', ' ', '#', ' '], 
        [' ', '#', ' ', '#', ' '], 
        [' ', '#', ' ', '#', ' '], 
        [' ', ' ', ' ', ' ', ' '], 
        ['#', ' ', '#', ' ', ' '], 
        [' ', ' ', '#', '#', '#']]

print(minimum_path(0,4,maze))
#====================================================================================
problem3______________________:
def max_nested(intervals):
    #make combination of all tuples
    v = list(comb2(intervals))
    #check if in the range
    k = []
    for i in range(0, len(v)):
        if v[i][0][0] < v[i][1][1] and v[i][0][1] > v[i][1][1]:
            k.append(v[i])
	print(v)
	print(k)



def comb2(s):
    for i, v1 in enumerate(s):
         for j in range(i + 1, len(s)):
             yield [v1, s[j]]


I1 = (0, 19)
I2 = (3, 11)
I3 = (9, 16)
I4 = (5, 10)
I5 = (8, 27)
intervals = [I1, I2, I3, I4, I5]





 


