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
            
    def search(self,x):
        curr = self.head
        dirs = [] 
        while curr:
            if x == curr.val:
                print(dirs)
                break
            elif x > curr.val:
                curr = curr.r
                dirs.append("r")
            elif x < curr.val:
                curr = curr.l
                dirs.append("l")


bst = BST()

bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(11)
bst.insert(7)
bst.insert(9)

bst.search(6)
