import numpy as np

n=[]
for i in range(15,0,-1):
    #n.append(i);
    n.append(np.random.randint(15)+1);

print(n)

print('\n', '=' *75, sep='')
print('Arr 0:\t\t', n, sep='')
for j in range(1,len(n),1):
   key = n[j]
   i = j -1
   while i >= 0 and n[i] > key:
       n[i +1] = n[i]
       i = i -1
   n[i +1] = key
   print('Arr ', j,':  \t', n, sep='')
print('=' *75, '\n', sep='')

print(n,'\n')
