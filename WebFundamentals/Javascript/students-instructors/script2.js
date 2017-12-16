'use strict';
var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    }
console.log("Students");
    for (var n = 0; n < users.Students.length; n++)
    {
        console.log(n+1 + " - ", users.Students[n].first_name, users.Students[n].last_name + " - " + (users.Students[n].first_name.length + users.Students[n].last_name.length));
    }
console.log("Instructors");
    for (var n = 0; n < users.Instructors.length; n++)
    {
        console.log(n+1 + " - ", users.Instructors[n].first_name, users.Instructors[n].last_name + " - " + (users.Instructors[n].first_name.length + users.Instructors[n].last_name.length));
    }
       
   
