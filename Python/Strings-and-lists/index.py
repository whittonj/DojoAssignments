words = "It's thanksgiving day. It's my birthday,too!" #print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

minmax = [2,54,-2,7,12,98] #Print the min and max values in a list like this one:

firstlast = ["hello",2,54,-2,7,12,98,"world"]#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

x = [19,2,54,-2,7,12,98,32,10,-3,6] #Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

applist = []
newx = []

print words.find("day")
wordchange = words.replace("day","month")
print wordchange

print min(minmax)
print max(minmax)

print firstlast[0]
print firstlast[(len(firstlast)-1)]

newlist = [firstlast[0],firstlast[(len(firstlast)-1)]]
print newlist

print x
x.sort()
print x

n = (len(x)/2)
print n

for i in range(0,n):
    print i
    applist.append(x[i])
    
print applist
x[0] = applist
print x

for i in range(1,n):
    x.pop(1)

print x