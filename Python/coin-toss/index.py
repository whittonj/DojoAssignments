heads = 0
tails = 0
result = ""
for i in range (1,5000):
    import random
    random_num = random.random()
    score = round(random_num)
    
    if score == 0:
        heads = heads + 1
        result = "heads"

    if score == 1:
        tails = tails + 1
        result = "tails"
    
    print "attempt #:", i, " - you got a ", result, "TOTAL: Heads -", heads, " | Tails - ", tails
    

