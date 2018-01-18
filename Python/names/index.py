students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in range (0, len(students)):
    print students[i]["first_name"],students[i]["last_name"]

print "-------------------------"

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students:"
for n in range (0, len(users["Students"])):
    print n+1,"-", users["Students"][n]["first_name"],users["Students"][n]["last_name"],"-",len(users["Students"][n]["first_name"]) + len(users["Students"][n]["last_name"])

print "Instructors"
for q in range (0, len(users["Instructors"])):
    print q+1,"-", users["Instructors"][q]["first_name"],users["Instructors"][q]["last_name"],"-",len(users["Instructors"][q]["first_name"]) + len(users["Instructors"][q]["last_name"])