var HOUR = 11;
var MINUTE = 33;
var PERIOD = "AM";
var minutes="";
var TIME;
var daypart="";

if (MINUTE < 30)
{   
    minutes = "just after";
    TIME = HOUR;
}
if (MINUTE > 30)
{   
    minutes = "almost";
    TIME = HOUR + 1;
}
if (MINUTE == 30)
{
    minutes = "half past";
    TIME = HOUR;
}
if (PERIOD == "PM")
{
    daypart ="evening";
}
else
{
    daypart = "morning";
}

if ( TIME > 12 )
{
    TIME  = 1;
}
console.log("It is " + minutes + " " + TIME + " o'clock in the " + daypart)