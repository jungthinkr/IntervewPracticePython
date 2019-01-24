"""
Given a directed graph, design an algorithm to find out whether there is a route between
two nodes.
"""

class Graph:
  def __init__(self, val):
    self.val = val
    self.edges = []

def hasRoute(a, b):
  s = a.edges
  while s:
    nxt = s.pop()
    if nxt == b:
      return True
    s.extend(nxt.edges)
  return False
    
if __name__ == '__main__':
  a = Graph(1)
  b = Graph(2)
  c = Graph(3)
  d = Graph(4)
  e = Graph(5)
  f = Graph(6)

  a.edges = [b,c,d]
  b.edges = [d]
  c.edges = [f]
  d.edges = [e]
  e.edges = [f]
  f.edges = []

  #find a to f
  print(hasRoute(a, f))

  

