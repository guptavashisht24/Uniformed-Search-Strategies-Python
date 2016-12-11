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
      #NON_RECURSIVE DFS
      def dfs_col(self,s):
          G = self.adjacency_list
          color = {u:"white" for u in G}
          color[s] = "grey"
          pie[s] = "None"
          d[s] = 0
          traversal = []
          stack = [s]
          while(len(stack)!=0):
               u = stack.pop()
               traversal.append(u)
               for v in G[u]:
                   if color[v]=="white":
                      pie[v] = u
                      d[v] = d[u]+1
                      color[v] = "grey"
                      stack.append(v)
               color[u] = "black"
          return traversal
      #Generates the path discovered in RECURSIVE_DFS using pie[!!!!RUN RECURSIVE_DFS atleast once before executing this!!!!]
      def print_path(self,G,s,v): 
          if v==s:
             print s
          elif pie[v]=="None":
               print "NO PATH EXISTS"
          else:
               self.print_path(G,s,pie[v])
               print v
      #RECURSIVE_DFS
      def graph_cormen_rec(self,s):
          G = self.adjacency_list
          color = {u:"white" for u in G}
          for u in G:
              
              if color[u] == "white":
                 p=self.dfs_visit(u,color,G)
      #Helper for RECURSIVE_DFS
      def dfs_visit(self,u,color,G):
           color[u] = "grey"
           for v in G[u]:
               pie[v] = u
               if color[v]=="white":
                   pie[v] = u
                   self.dfs_visit(v,color,G)
               
                 
           color[u] = "black"
           
p = Graphs_lx()
p.add_edge("4","6")
p.add_edge("1","2")
p.add_edge("2","3")
p.add_edge("3","4")
p.add_edge("2","4")
p.add_edge("4","1")
p.add_edge("4","3")
p.graph_cormen_rec("1")
p.print_path(p.adjacency_list,"1","4")
