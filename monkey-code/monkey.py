class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = int(strength)
        self.int = int(intelligence)
        self.agi = int(agility)
        self.id = id
        
    def __repr__(self) -> str:
        return f'{self.id}-{self.name}'
    
    def getAttr(self,attr):
        return eval(f'self.{attr}')

def compare(m1,m2,priority,order):
    n = len(priority)
    for i in range(n):
        if order == 'D':
            if m1.getAttr(priority[i]) > m2.getAttr(priority[i]):
                return True
            elif m1.getAttr(priority[i]) < m2.getAttr(priority[i]):
                return False
        elif order == 'A':
            if m1.getAttr(priority[i]) > m2.getAttr(priority[i]):
                return False
            elif m1.getAttr(priority[i]) < m2.getAttr(priority[i]):
                return True
    return True

def mergeSort(arr,priority,order):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
        # print(L,end='')
 
        # Into 2 halves
        R = arr[mid:]
        # print(R)
        
        # Sorting the first half
        mergeSort(L,priority,order)
 
        # Sorting the second half
        mergeSort(R,priority,order)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if compare(L[i],R[j],priority,order):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    order,priority,monkeys = input('Enter Input: ').split('/')
    priority = priority.split(',')
    monkeys = monkeys.split(',')
    monkeys_lst = []
    for i,m in list(enumerate(monkeys)):
        monkeys_lst.append(Monkey(*(m.split()),i))
    # for i in monkeys_lst:
    #     print(i.name,i.str,i.int,i.agi,i.id)
    if priority != ['']:
        mergeSort(monkeys_lst,priority,order)
    print(monkeys_lst)
if __name__ == '__main__':
    main()