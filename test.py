class Graph: 
	def __init__(self,v): 
		self.graph = [None]*v
	def addEdge(self,u,v): 
		if self.graph[u] is not None:
			self.graph[u].append(v) 
		else:
			self.graph[u]=[]
			self.graph[u].append(v)
	def BFS(self, s): 
		visited = [False] * (len(self.graph)) 
		queue = [] 
		queue.append(s) 
		visited[s] = True
		while queue: 
			s = queue.pop(0) 
			print (s, end = " ") 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
print ("Following is Breadth First Traversal (starting from vertex 2)") 
g.BFS(2) 