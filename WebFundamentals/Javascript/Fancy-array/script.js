var names = [ "James", "Jill", "Jane", "Jack" ];

function nameList(reverse,sep)
{
    if (reverse == true)
        {
        for ( i = names.length - 1; i >= 0 ; i--)
        {
            console.log(i + sep + names[i]); 
        }
    }
    else  
        {
        for ( i = 0; i < names.length; i++)
        {
            console.log(i + sep + names[i]); 
        }
    }
}
