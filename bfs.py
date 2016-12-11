pie = {}
d = {}
class Graphs_lx:
      adjacency_list = {}
      
      def __init__(self):
          self.edge_list = []
      def add_edge(self,src,dest):
          if src in self.adjacency_list and dest not in self.adjacency_list[src] :
                 self.adjacency_list[src].append(dest)
          else:
                 self.adjacency_list[src] = [dest]
          if dest not in self.adjacency_list:
                 self.adjacency_list[dest] = []
      
      

             
      
      def bfs_col(self,s):
          G = self.adjacency_list
          color = {u:"white" for u in G}
          color[s] = "grey"
          pie[s] = "None"
          d[s] = 0
          q = [s]
          traversal = []
          while(len(q)!=0):
               u = q.pop(0)
               traversal.append(u)
               for v in G[u]:
                   if color[v]=="white":
                      color[v]="grey"
                      q.append(v)
                      d[v] = d[u]+1
                      pie[v] = u
                   
               color[u]="black"
          return traversal
      
      

p = Graphs_lx()
p.add_edge("4","6")
p.add_edge("1","2")
p.add_edge("2","3")
p.add_edge("3","4")
p.add_edge("2","4")
p.add_edge("4","1")
p.add_edge("4","3")

p.bfs_col("1")

