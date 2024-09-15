n = int(input('Enter Input : '))
size = 2*(n) + 4 
for j in range(size):
    for i in range(size):
        if j <= n - i or j >= (3*n+6) - i:
            print('.',end='')
        elif j in range(1,2*n+3) and not j in range(size//2 - 1,size//2+1) and i in range(1,2*n+3) and not i in range(size//2 - 1,size//2+1):
            if i > size//2 and j < size//2:
                print('#',end='')
            elif j > size//2 and i < size//2:
                print('+',end='')
            else:
                if i < size//2:
                    print('#',end='')
                elif i >= size//2:
                    print('+',end='')
        elif i < size//2:
            print('#',end='')
        elif i >= size//2:
            print('+',end='')
        
    print('')