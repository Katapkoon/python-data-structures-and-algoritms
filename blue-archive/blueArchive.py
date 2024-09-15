def nameValue(val):
    # Code Here
    total = sum([ord(c) for c in val])
    return total

class TreeNode(object):
    def __init__(self, val):
        # Code Here
        self.name = val
        self.data = nameValue(val)
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def getHeight(self, root):
        # Code here
        return -1 if root == None else root.height
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def getBalance(self):
        # Code here
        return  self.getHeight(self.left) - self.getHeight(self.right)

class AVL_Tree(object):
    def __init__(self):
        self.root = None
    def insert(self, root, data):
        # Code Here
        if not root:
            return TreeNode(data)
        elif nameValue(data) < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.setHeight()

        bf = root.getBalance()

        if bf > 1 and nameValue(data) < root.left.data:
            return self.rightRotate(root)
        
        if bf < -1 and nameValue(data) > root.right.data:
            return self.leftRotate(root)
        
        if bf > 1 and nameValue(data) > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bf < -1 and nameValue(data) < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def delete(self, root, data):
        # Code Here
        if not root:
            return root
        elif nameValue(data) < root.data:
            root.left = self.delete(root.left, data)
        elif nameValue(data) > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
        
            temp = self.getMinValueNode(root.right)
            root.name = temp.name
            root.data = temp.data
            root.right = self.delete(root.right, temp.name)

        root.setHeight()

        bf = root.getBalance()

        if bf > 1 and root.left.getBalance() >= 0:
            return self.rightRotate(root)
        
        if bf < -1 and root.right.getBalance() <= 0:
            return self.leftRotate(root)
        
        if bf > 1 and root.left.getBalance() < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bf < -1 and root.right.getBalance() > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)  
        
        return root

    def leftRotate(self, z):
        # Code here
        b = z.right
        bLeftChild = b.left

        b.left  = z
        z.right = bLeftChild

        z.setHeight()
        b.setHeight()

        return b
 
    def rightRotate(self, z):
        # Code here
        b = z.left
        bRightChild = b.right

        b.right = z
        z.left = bRightChild

        z.setHeight()
        b.setHeight()

        return b 
    
    def getMinValueNode(self, root):
        # Code here
        return root if not root or not root.left else self.getMinValueNode(root.left)
    
    def printTree(self, root,level = 0):
        # Code here
        if root != None:
            print('    ' * level + f'{root.name} ({root.data})')

            if not root.left and not root.right and  root.getHeight(root) != 0:
                return
            if root.left:
                self.printTree(root.left,level+1)
            elif not root.left and root.getHeight(root) != 0:
                print('    ' * (level + 1) + '*')

            if root.right:    
                self.printTree(root.right,level+1)
            elif not root.right and root.getHeight(root) != 0:
                print('    ' * (level + 1) + '*')
        
            
avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        # print(data)
        root = avl_tree.insert(root, data)
        avl_tree.root = root
        
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")
