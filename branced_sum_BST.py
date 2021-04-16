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
            

    def branch_sum(self,curr,summ,sums):
        if curr is None:
            return
        nsumm = summ + curr.val
        if curr.l is None and curr.r is None:
            sums.append(nsumm)
            return
        self.branch_sum(curr.l, nsumm, sums)
        self.branch_sum(curr.r, nsumm, sums)
        

    def branched_sum(self,x):
        curr = self.head
        sums = []
        while True:
            if x == curr.val:
                print(x)
                t = curr
                sumb = 0
                self.branch_sum(curr,sumb,sums)     
                print(sums)              
                break              
            if x > curr.val:
                    curr = curr.r
            elif x < curr.val:
                    curr = curr.l


bst = BST()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(9)
bst.insert(6)
bst.insert(1)
bst.insert(4)
bst.insert(12)



bst.branched_sum(12)