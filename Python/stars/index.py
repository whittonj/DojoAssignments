x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


for i in range (0,len(x)):
    if isinstance(x[i], int) or isinstance(x[i], float) or isinstance(x[i], long):  
        stars=""
        for n in range(0,(x[i])):
            stars=stars + "*"
        print stars
    elif isinstance(x[i], str):
        letter = ""
        for n in range(0,len(x[i])):
            letter = letter + (x[i][0])
        print letter.lower()
    

