n=int(input())
arr = list(map(int, input().split()))
a=arr[0]
for i in range(n+1):
	a|=arr[i]
print(a)
