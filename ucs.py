import heapq
import sys
pie = {}
d = {}
class Graphs_lx:
      """
       Generates a graph 
      """
      adjacency_list = {}
      
      def __init__(self):
          self.edge_list = []
      def add_edge(self,src,dest,weight):
          if src in self.adjacency_list and dest not in self.adjacency_list[src] :
                 self.adjacency_list[src].append([dest,weight])
          else:
                 self.adjacency_list[src] = [[dest,weight]]
          if dest not in self.adjacency_list:
                 self.adjacency_list[dest] = []
      
            
      def ucs(self,start,goal):
          p = []
          heapq.heappush(p,[0,[start]])
          G = self.adjacency_list
          print G
          sol = []
          curr = sys.maxint 
          while(p):
               k = heapq.heappop(p)
               u = k[1][-1]
               if k[0] < curr and u==goal:
                  curr = k[0]
                  sol = k[1]
               if k[0]>curr:
                  break
               for v in G[u]:
                   x = []
                   t = k[1][:]
                   t.append(v[0])
                   heapq.heappush(p,[k[0]+v[1],t])
                   print p
          print sol
                   
p = Graphs_lx()
p.add_edge("S","A",1)
p.add_edge("S","G",12)
p.add_edge("A","B",3)
p.add_edge("B","D",3)
p.add_edge("D","G",3)
p.add_edge("A","C",1)
p.add_edge("C","D",1)
p.add_edge("C","G",2)
print p.adjacency_list
p.ucs("S","G")
