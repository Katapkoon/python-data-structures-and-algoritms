class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)
    
    
class TreeNode(object):
    def __init__(self, data):
        # Code Here
        self.data = data
        self.left = None
        self.right = None
        self.height = self.setHeight()
        self.parent = None

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
    
    def __str__(self):
        return str(self.data)
    
    def siblings(self):
        return (self.left,self.right,self.parent)
    
class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        # Code Here
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.setHeight()

        bf = root.getBalance()

        if bf > 1 and data < root.left.data:
            return self.rightRotate(root)
        
        if bf < -1 and data > root.right.data:
            return self.leftRotate(root)
        
        if bf > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bf < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def delete(self, root, data):
        # Code Here
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
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
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

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
    
    def printTree(self, node,level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node,f'({node.parent})')
            self.printTree(node.left, level + 1)

    def search(self, root, key):
        if not root or root.data == key:
            return root
        
        if root.data < key:
            return self.search(root.right, key)
        
        return self.search(root.left, key)

    def parenting(self,root):
        if root != None:
            self.parenting(root.left)
            if root.left:
                root.left.parent = root
            if root.right:
                root.right.parent = root
            self.parenting(root.right)
    def burn(self,key):
        node = self.search(self.root,key)
        lst = []
        lst.append(node)

        visited = []
        visited.append(node)
        print(node)
        def _burn(lst):
            
            new_lst = []
            for i in lst:
                for j in i.siblings():
                    if j and j not in visited:
                        new_lst.append(j)
                        visited.append(j)
            if not new_lst:
                return            
            print(' '.join([str(i)for i in new_lst]))
            
            _burn(new_lst)
            
        _burn(lst)
def main():
    avl_tree = AVL_Tree()
    inp,burn = input('Enter node and burn node : ').split('/')
    nodes = inp.split()
    for i in nodes:
        avl_tree.root = avl_tree.insert(avl_tree.root,int(i))

    avl_tree.parenting(avl_tree.root)
    # avl_tree.printTree(avl_tree.root)

    if avl_tree.search(avl_tree.root,int(burn)) is None:
        print(f'There is no {burn} in the tree.')
        return 
    
    avl_tree.burn(int(burn))


if __name__ == '__main__':
    main()