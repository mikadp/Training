class Vertex:
# Uses a dictionary as an adjacency list to store connected vertices.
  def __init__(self, value):
    self.value = value
    self.edges = {}

# Connected vertex names are keys and the edge weights are values.
  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight
    
# Has methods to add edges and return a list of connected vertices.
  def get_edges(self):
    return list(self.edges.keys())
