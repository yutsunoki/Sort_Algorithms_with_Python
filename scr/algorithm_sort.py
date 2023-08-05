#!/usr/bin/python3
import os
import matplotlib.pyplot as plt
import numpy as np
import random
import time

os.system("echo [m &cls")

n=[]
for i in range(15, 0, -1):
    n.append(random.randint(0, 100))
    #n.append(i)

x = range(len(n))

color=[]
for i in range(102, 231, 1):
    color.append("[" + "38;5;" + str(i) + "m")

for i in n:
    print(i, sep="", end="\t", flush=True)

plt.bar(x, n, color = 'r', width = 0.4)
plt.pause(0.5)
plt.clf()
plt.title("insertion sort")

print("[38;5;196m", end="")
print("\n")
plt.title("insertion sort")
for j in range(0, len(n)):
    key = n[j]
    i = j -1
    while i > -1 and n[i] > key:
        plt.bar(x, n, color = 'r', width = 0.4)
        plt.pause(0.00001)
        plt.clf()
        plt.title("insertion sort")
        n[i+1] = n[i]
        for a in range(len(n)):
            print(color[n[a]], n[a], sep="", end="\t", flush=True)
        print("")
        i = i -1
    n[i+1] = key
    for a in range(len(n)):
        print(color[n[a]], n[a], sep="", end="\t", flush=True)
    print("")

print("[38;5;46m", end="\n")
for i in n:
    print(i, sep="", end="\t", flush=True)
print("\n[m")

plt.bar(x, n, color = 'r', width = 0.4)
plt.pause(0.1)
plt.clf()
plt.title("bubble sort")

for i in range(len(n)):
    for j in range(0, len(n) -i -1):
        plt.bar(x, n, color = 'r', width = 0.4)
        plt.pause(0.00001)
        plt.clf()
        plt.title("bubble sort")
        if n[j] < n[j+1]:
            temp = n[j+1]
            n[j+1] = n[j]
            n[j] = temp
        for a in range(len(n)):
            print(color[n[a]], n[a], sep="", end="\t", flush=True)
        print("\n")
    for a in range(len(n)):
        print(color[n[a]], n[a], sep="", end="\t", flush=True)
    print("\n")

print("[38;5;46m", end="\n")
for i in n:
    print(i, sep="", end="\t", flush=True)
print("[m\n\n")
plt.bar(x, n, color = 'r', width = 0.4)
plt.pause(0.1)
plt.clf()
plt.title("bubble sort")

def merge(arr, p, q, r):
    n1 = q -p +1
    n2 = r -q

    L = [0] *n1
    R = [0] *n2

    for i in range(0, n1):
        L[i] = arr[p +i]
    for j in range(0, n2):
        R[j] = arr[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
        for a in range(len(n)):
            print(color[n[a]], n[a], sep="", end="\t", flush=True)
        print("")
        plt.bar(x, n, color = 'r', width = 0.4)
        plt.pause(0.00001)
        plt.clf()
        plt.title("merge sort")

    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1
        for a in range(len(n)):
            print(color[n[a]], n[a], sep="", end="\t", flush=True)
        print("")
        plt.bar(x, n, color = 'r', width = 0.4)
        plt.pause(0.00001)
        plt.clf()
        plt.title("merge sort")

    while j < n2:
        arr[k] = R[j]
        j+=1
        k+=1
        for a in range(len(n)):
            print(color[n[a]], n[a], sep="", end="\t", flush=True)
        print("")
        plt.bar(x, n, color = 'r', width = 0.4)
        plt.pause(0.00001)
        plt.clf()
        plt.title("merge sort")

def mergesort(arr, p, r):
    if p < r:
        q = p+(r-p)//2
        mergesort(arr, p, q)
        mergesort(arr, q+1, r)
        merge(arr, p, q, r)

nlen=len(n)
mergesort(n,0,nlen-1)

print("[38;5;46m\n", end="\n")
for i in n:
    print(i, sep="", end="\t", flush=True)
print("[m")

plt.bar(x, n, color = 'g', width = 0.4)
plt.show()
