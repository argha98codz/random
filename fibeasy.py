def helper(n):
	#for i in range(1,n+1):
	#	print(i, end=" ")
	print ()
	s,l,d = 1,n,1
	while (n>1):
		n=n//2
		
		s+=d
		d*=2
		l=s+(n-1)*d
	return s
def fib(f, n): 
  
    f[0] = 0
    f[1] = 1 
  
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10
  
    return f; 
  
def findLastDigit(n): 
    f = [0] * 61
    f = fib(f, 60)
  
    return f[n % 60]

t = int(input())
while (t > 0):
	n = int(input())
	k = (helper(n))
	print (findLastDigit(k-1))
	t-=1
