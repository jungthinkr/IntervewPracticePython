"""
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second
project is dependent on teh frist project). All of the project's dependencies must be build before the project is.
Find a build order that will allow the projects to be built. If there is not valid build order, return an error.

EXAMPLE
input:
  projects: a,b,c,d,e,f
  dependencies: (a,d),(f,b),(b,d),(f,a),(d,c)
output: f,e,a,b,d,c
"""
#topological sort

class Graph:
  def __init__(self):
    self.edges= {}

  def addEdge(self, a, b):
    if not self.edges.get(a):
      self.edges[a] = [b]
    else:
      self.edges[a].append(b)

  def getEdgesForNode(self, a):
    return self.edges.values()[a]

  def getNodes(self):
    return self.edges.keys()
  
  def size(self):
    return len(self.edges.values())

def util(ptr, visited, stack, graph):
  visited[ptr] = True

  edges = graph.getEdgesForNode(ptr)
  for i in range(len(edges)):
    if not visited[i]:
      util(i, visited, stack, graph)
  stack.insert(0, graph.getNodes()[ptr])

#return arr
def topSort(graph):
  visited = [False]*graph.size()
  stack = []
  
  for i in range(graph.size()):
    if not visited[i]:
      util(i, visited, stack, graph)

  print(stack)
  return stack

if __name__ == '__main__':
  #setup
  graph = Graph()
  graph.addEdge('a', 'd')
  graph.addEdge('f', 'b')
  graph.addEdge('b', 'd')
  graph.addEdge('f', 'a')
  graph.addEdge('d', 'c')

  topSort(graph)
  
  