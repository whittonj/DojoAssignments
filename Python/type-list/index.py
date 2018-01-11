x = ['magical','unicorns']


def what(x):
    ttl = 0
    newstring =""
    for i in range(0, len(x)):
        if isinstance(x[i], int) or isinstance(x[i], float) or isinstance(x[i], long):   
            ttl = ttl + x[i]
        elif isinstance(x[i], str):
            newstring = newstring + " " + x[i]

    if ttl > 0 and newstring == "":
        print "All numbers"
        print "Sum:", ttl

    elif ttl > 0 and newstring != "":
        print "Mixed"
        print "Sum:", ttl
        print newstring

    elif ttl == 0 and newstring != "":
        print "All wordy"
        print newstring
   

what(x)
