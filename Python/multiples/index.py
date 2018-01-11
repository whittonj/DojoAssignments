#Odd numbers from 1 - 1000
for i in range(1,1000,2):
    print i

#5 to 1,000,000 by 5- actually 100,000 for now- code runner exits before it gets to 1mil
for i in range(5, 100000, 5):
    print i

#sum a list of numbers
def sumlist(list):
    ttl = 0
    for i in range(0, len(list)):
        ttl = ttl + list[i]      
    print ttl
        
sumlist([2,3,4,5,6,8,9])

#Avg a list of numbers
def avglist(list):
    ttl = 0.0
    for i in range(0, len(list)):
        ttl = ttl + list[i]      
    print ttl/(len(list))
        
avglist([2,3,4,5,6,8,9])