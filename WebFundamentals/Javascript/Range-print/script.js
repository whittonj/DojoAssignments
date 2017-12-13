function ranger(x,y,z)
{
    if (z == undefined)
    {
        z = 1;
    }
    if (y == undefined)
    {
        y = x;
        x = 0;
    }    
    
        for (i = x; i < y; i = i + z)
    console.log(i);
}
ranger(40);
