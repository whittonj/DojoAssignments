var penniesDue = 1; 
var pennies = 0 ;

for (var i = 1; i < 31; i++)
{ 
    pennies = pennies + penniesDue;
    penniesDue = penniesDue * 2; 
    console.log("Day " + i);
    console.log("total " + pennies);
    console.log("due " + penniesDue);
}
console.log("$" + (pennies / 100))
console.log(i);
