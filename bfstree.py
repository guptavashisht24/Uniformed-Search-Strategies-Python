class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None


class Tree:
      def __init__(self,root):
          self.root = root
      
      def search(self,target):
          level = 0
          f = 0
          stack = [self.root]
          while(stack):
              k =  stack.pop(0)
              print k.val
              
              if k.val==target:
                 print "Found"
                 f=1
                 break
              if k.left:
                 stack.append(k.left)
              if k.right:
                 stack.append(k.right)
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
p = Tree(A)
p.search(7)
          
