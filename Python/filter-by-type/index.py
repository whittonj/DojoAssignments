sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def what(anything):
    if isinstance(anything, int):
        if anything >=100:
            print "long intiger baby"
        else :
            print "short inty"  
    elif isinstance(anything, str):
        if len(anything) >=50:
            print "long sentence"
        else :
            print "short sentence"
    elif isinstance(anything, list): 
        if len(anything) >=10:
            print "long list"
        else :
            print "short list"

what([1,2,3,4,5,6,7,8,9])