from sys import stdin
from sys import stdout

def find(x, p):
    while x!=p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x
    

n,m = map(int, stdin.readline().split())
g = [i for i in range(n)]
for i in range(m):
    arr = list(map(int, stdin.readline().split()))
    for j in range(2,len(arr)):
        g[find(arr[j]-1,g)] = find(arr[1]-1, g)

#print (g)
freq = [0]*n
for i in range(n):
    freq[find(i,g)]+=1
count = [0]*n
for i in range(n):
    count[i] = freq[find(i,g)]
print (' '.join([str(i) for i in count]))

#print (g,freq)
