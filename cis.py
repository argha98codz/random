def binomialCoeff(n , k): 
	C = [0 for i in range(k+1)] 
	C[0] = 1 
	
	for i in range(1,n+1): 
		j = min(i ,k) 
		while (j>0): 
			C[j] = C[j] + C[j-1] 
			j -= 1

	return C[k] 
t = int(input())

while(t>0):
	n,k = map(int, input().split())
	arr = list(map(int, input().split()))
	marr, msarr = {}, {} 
	sarr = sorted(arr)
	for i in range(k):
		if sarr[i] in msarr:
			msarr[sarr[i]]+=1
		else:
			msarr[sarr[i]] = 1
			marr[sarr[i]] = 0
	for i in range(n):
		if arr[i] in marr:
			marr[arr[i]]+=1
	c = 1
	for key,value in msarr.items():
		if value != marr[key]:
			
			c*=binomialCoeff(marr[key], value)
			#print(marr[key], value)
	print(c)
	
	t-=1
