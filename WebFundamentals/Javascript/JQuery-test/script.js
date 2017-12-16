'use strict';
var start = [1, "apple", -3, "orange", 0.5];
var numbersOnly = [];
var i=0;
// newArray is [1, -3, 0.5]

for (i = 0; i < start.length; i++)
{
    if (typeof start[i] ==="number")
    {
        numbersOnly.push(start[i]);
    }
}
console.log(numbersOnly);