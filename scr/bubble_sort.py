import numpy as np

n=[]
for i in range(10,0,-1):
    #n.append(i);
    n.append(np.random.randint(15) +1);

print(n)

print('Arr[0]:\t\t', n, sep='')
for i in range(0, len(n) -1, 1):
    for j in range(len(n) -1, i, -1):
        if n[j] < n[j -1]:
            temp = n[j]
            n[j] = n[j -1]
            n[j -1] = temp
        print('Arr ', i, ':\t\t', n, sep='')
    print('\n')

print(n, '\n')
