import math 
y=int(input())
def Log2(x): 
    return (math.log10(x) / math.log10(2)); 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 
if(isPowerOfTwo(y)): 
    print("yes"); 
else: 
    print("no"); 
