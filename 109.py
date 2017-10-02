

# Binary Tree node implementation

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, key):
        self.key = key

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print r.getRootVal()
r.insertLeft('b')
r.insertRight('c')

print r.getLeftChild().getRootVal()
print r.getRightChild().getRootVal()

r.getLeftChild().setRootVal('hello')
print r.getLeftChild().getRootVal()
