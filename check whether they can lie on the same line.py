def collinear(x1, y1, x2, y2, x3, y3): 
	
	a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 

	if (a == 0): 
		print ("yes")
	else: 
		print ("no")

x1, y1=input().split()
x2, y2=input().split()
x3, y3=input().split()
collinear(int(x1),int(y1),int(x2), int(y2), int(x3), int(y3)) 
