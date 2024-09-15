class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def children(self):
        return (self.left,self.right)
    
    def __str__(self):
        return str(self.data)   

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert(root,data):
            if not root:
                return Node(data)
            else:
                if root.data > data:
                    root.left = _insert(root.left,data)
                else:
                    root.right = _insert(root.right,data)

            return root
        self.root = _insert(self.root,data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

class AVL(BST):
    class AVLNode:
        def __init__(self,data,frequency = 0):
            self.data = data
            self.left = None
            self.right = None 
            self.frequency = frequency
            self.height = self.setHeight()
        
        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            return 1 + max(a,b)
        
        def getHeight(self,node):
            return -1 if not node else node.height
        
        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)
        
        def getFrequency(self):
            return self.frequency
        
        def children(self):
            return (self.left,self.right)
        
        def __str__(self):
            return str(self.data)
        
    def __init__(self):
        self.root = None
    
def huffman(node,binString=''):
    if type(node.data) is str and node.data != '*':
        return {node.data: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman(r, binString + '1'))
    d.update(huffman(l, binString + '0'))
    
    return d


def findLeastFrequent(lst):
    min = lst[0]
    for i in lst:
        if i.frequency < min.frequency or (i.frequency == min.frequency and i.height > min.height):
            min = i

    lst.remove(min)
    return min


def removeDuplicate(lst, n):
    return [i for i in lst if i != n]

def encode(string : str, d : dict):
    encoded = ''
    for s in string:
        encoded += d[s]
    return f'Encoded! : {encoded}'
    

def main():
    avl = AVL()
    inp = [i for i in input('Enter Input : ')]
    new_inp = inp[:]
    new_inp.sort()

    for i in new_inp:
        new_inp = removeDuplicate(new_inp,i)
        new_inp.append(i)
    freqs = [inp.count(i) for i in new_inp]
    new_inp = [avl.AVLNode(new_inp[i],freqs[i]) for i in range(len(new_inp))]
    
    for i in range(len(new_inp)-1):
        node = avl.AVLNode('*')
        node.left = findLeastFrequent(new_inp)
        node.right = findLeastFrequent(new_inp)
        node.frequency = node.right.frequency + node.left.frequency
        new_inp.append(node)
        node.height = node.setHeight()
    
    avl.root = new_inp.pop()
    encode_dict = huffman(avl.root)
    print(encode_dict)
    avl.printTree(avl.root)
    print(encode(inp,encode_dict))

if __name__ == '__main__':
    main()