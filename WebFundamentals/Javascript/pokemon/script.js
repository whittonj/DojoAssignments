'use strict';

$(document).ready(function() {



  for (var i=1; i <=151; i++) { 
  dataType: 'jsonp';
$.get("https://pokeapi.co/api/v2/pokemon/"+i+"/", function(response) {
      console.log(response);
var string = (response.sprites.front_default);
console.log(string);
$(".main_content").append("<img src = " + string + " id = " + i + ">");
console.log(i);

});
}
    
});
