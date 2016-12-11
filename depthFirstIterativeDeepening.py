class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None


class TreeDLS:
      def __init__(self,root):
          self.root = root
      def maxDepth(self, A):
        if A==None:
            return 0
        l = self.maxDepth(A.left)
        r = self.maxDepth(A.right)
        if l>r:
            return l+1
        return r+1
      
      def search(self,target):
         f = 0
         for i in xrange(0,self.maxDepth(self.root)+1):
          if f==1:
            break
          level = 0
          levelt = i
          stack = [[self.root,level]]
          while(stack):
              k =  stack.pop()
              i = k[1]
              if k[0].val==target and i<levelt:
                 print "Found"
                 f=1
                 break
              if k[0].left and k[1] < levelt-1:
                 stack.append([k[0].left,k[1]+1])
              if k[0].right and k[1] < levelt-1:
                 stack.append([k[0].right,k[1]+1])
         if f==0:
             print "Not Found"
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(6)
G = TreeNode(7)
B.left = D
B.right = E
C.left = F
C.right = G
A.left = B
A.right = C
p = TreeDLS(A)
p.search(9)
p.search(4)
