word_list = ['hello','world','my','name','is','Anna']
char = 'o'
list = []

for i in range(0, len(word_list)):
   if word_list[i].find(char) > 0:
       list.append(word_list[i])

print list