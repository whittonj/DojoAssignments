//If a number is divisible by 3 write fizz//
//if a number is evenly divisibly by 5 write Buzz//
//if both write FizzBuzz - if neither print the number//

for (var i =1; i < 100; i++)
{
    if (i % 3 == 0 && i % 5 == 0)
    {
        console.log("FizzBuzz");
    }
    else if (i % 3 == 0)
    {
        console.log("Fizz");
    }
    else if (i % 5 ==0)
    {
        console.log("Buzz");
    }
    else
    {
        console.log(i);
    }
}