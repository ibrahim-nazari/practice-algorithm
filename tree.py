class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None



class Tree:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,val):
        node=Node(val)
        if not self.head:
            self.head=node
            self.tail=node
        cur=self.head
        while True:
            if cur.val==val:return True
            if cur.val > val:
                if not cur.left:
                    cur.left=Node(val)
                    return True
                cur=cur.left
            else:
                if not cur.right:
                    cur.right=Node(val)
                    return True
                cur=cur.right
    def printTree(self):
        cur=self.head
        result=[]
        def dfs(root):
            if not root:
                return
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(cur)
        print("result ---- ",result)

        



tree1=Tree()
tree1.insert(15)
tree1.insert(22)
tree1.insert(12)
tree1.insert(18)
tree1.insert(20)
tree1.insert(13)
tree1.insert(10)
tree1.insert(11)
tree1.insert(5)
tree1.insert(7)
tree1.insert(2)
tree1.printTree()

                
                
                


        
            