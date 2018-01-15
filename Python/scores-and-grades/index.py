for i in range (1,10):
    import random
    random_num = random.random()
    random_num = random_num*100
    score = int(random_num)
    if score <= 59:
        grade = "F"
    if score >59 and score <70:
        grade = "D"
    if score >69 and score <80:
        grade = "C"
    if score >79 and score <90:
        grade = "B"
    if score >= 90:
        grade = "A"

    print "Score:", score, "; Your grade is", grade
    print "End of program, bye!"

