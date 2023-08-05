import numpy as np

n=[]
for i in range(10,0,-1):
    n.append(i);
    #n.append(np.random.randint(15));

for i in range(0,len(n)):
    print(n[i], flush=True, end=' ' )

print('\n')

def merge(n, p, q, r):
    n1 = q -p +1
    n2 = r -q

    L = [0] *n1
    R = [0] *n2

    for i in range(0,n1,1):
        L[i] = n[p +i]
    for j in range(0,n2,1):
        R[j] = n[q +j +1]

    print('=' *30)
    print("High: ", r, '\tMid: ', q,'\tLow ', p)
    print('L(len): ', n1, '\tR(len): ', n2)
    print('Arr: ',n)
    print('L(arr): ', L)
    print('R(arr): ', R)

    i = 0
    j = 0
    k = p

    print('=' *30)
    print('k: ', k, "\n", '=' *30, sep='')
    print('Start|\tL:',i,'R:',j)
    print('Start|\tArr::', n)
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            n[k] = L[i]
            i += 1
        else:
            n[k] = R[j]
            j += 1
        k += 1
    print('end|\tL:',i,'R:',j)
    print('end|\tArr::', n)

    print('=' *30)
    print('k: ', k, "\n", '=' *30, sep='')
    print('Start|\tL:',i)
    print('start|\tArr::', n)
    while i < n1:
        n[k] = L[i]
        i += 1
        k += 1
    print('end|\tL:',i)
    print('end|\tArr::', n)

    print('=' *30)
    print('k: ', k, "\n", '=' *30, sep='')
    print('Start|\tR:',j)
    print('Start|\tArr::', n)
    while j < n2:
        n[k] = R[j]
        j += 1
        k += 1
    print('end|\tR:',j)
    print('end|\tArr::', n)

    print(n)
    print('\nNext\n')

def merge_sort(n, p, r):
    if p < r:
        q = p +(r -p) //2
        merge_sort(n, p, q)
        merge_sort(n, q +1, r)
        merge(n, p ,q ,r)

merge_sort(n, 0, len(n) -1)

print('\n')
for i in range(0,len(n)):
    print(n[i], flush=True, end=' ')
