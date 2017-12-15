'use strict';
var bank = 0;
var win =0;

function slot(startDollars){
    
    for (bank =(startDollars * 4); bank > 0; bank = bank -1)
    {
    console.log(bank + " quarters");
    console.log("Drop one in");
    
    if (Math.trunc(Math.random()*100) == 1)
    {
        console.log("WINNER!");
        win = (Math.floor(Math.random()*50) + 50);
        console.log("You won " + win);
        bank = bank + win;
        break;
        }
    }
console.log(bank + " total quarters = $" + (bank/4))
}
slot(100)

//pass the DOLLAR amount to slot () to start//