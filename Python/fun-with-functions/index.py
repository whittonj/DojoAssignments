def oddeven():
    for n in range(1,2000):
        if n % 2 == 0:  
            print n, "is even."
        else:    
            print n, "is odd."

a = [2,4,10,16]
c=[]
b=0
pe=[]
newarr =[]

for n in range(0,len(a)):
    b = a[n] * 5
    c.append(b)

def layered_multiples(arr):
    for i in range (0, len(arr[0])):
        for q in range (0,(arr[0][i])*arr[1]):
            pe.append(1)   
        print pe
        newarr.insert(i, pe)

arr = layered_multiples(([2,4,5],3))
print newarr

#oddeven()
#print c