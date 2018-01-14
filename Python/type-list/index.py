list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
boo= True

if len(list_one) != len(list_two):
    print "Not the same length"
    boo = False

else:
    for i in range(0, len(list_one)):
        if list_one[i] != list_two[i]: 
            boo = False
            break
        else:
            boo = True

if boo == True:
    print " The lists are the same"

else:
    print "The lists are not the same"