class Node:
    def __init__(self,x):
        self.val = x
        self.l = None
        self.r = None

class BST:
    def __init__(self):
        self.head = None

    def insert(self,x):
        n = Node(x)
        if self.head == None:
            self.head = n
            return 0
        curr = self.head

        while True:
            if n.val > curr.val:
                if curr.r is None:
                    curr.r = n
                    break
                else:
                    curr = curr.r
            else:
                if curr.l is None:
                    curr.l = n
                    break
                else:
                    curr = curr.l
            
    def traverseInorder(self,tree,arr):
        if tree is not None:
            self.traverseInorder(tree.l,arr)
            arr.append(tree.val)
            self.traverseInorder(tree.r,arr)
        return arr

    def traversePreorder(self,tree,arr):
        if tree is not None:
            arr.append(tree.val)
            self.traversePreorder(tree.l,arr)
            self.traversePreorder(tree.r,arr)
        return arr

    def traversePostorder(self,tree,arr):
        if tree is not None:
            self.traversePostorder(tree.l,arr) 
            self.traversePostorder(tree.r,arr)
            arr.append(tree.val)
            
        return arr



bst = BST()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(22)
bst.insert(5)
bst.insert(1)
arr = []
print(bst.traverseInorder(bst.head,arr))
arr= []
print(bst.traversePreorder(bst.head,arr))
arr= []
print(bst.traversePostorder(bst.head,arr))
