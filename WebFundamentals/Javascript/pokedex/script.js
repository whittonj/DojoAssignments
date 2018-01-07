'use strict';

$(document).ready(function() {


for (var i=1; i <=10; i++) { 
$.get("https://pokeapi.co/api/v2/pokemon/"+i+"/", function(response) {
      console.log(response);
      var string = `<img src="${response.sprites.front_default}"id="${response.id}">`;
      console.log(response.id);
      var idpi = (response.id);
      console.log(idpi);
      $(".main_content .left").append(string);
});
}

$(document).on('click', 'img', function(){
      var idnow = $(this).attr("id");   
      console.log(idnow); 
      $.get("https://pokeapi.co/api/v2/pokemon/"+idnow+"/", function(response) {
            var stats =`
            <h1>${response.name}</h1>
            <p>Height : ${response.height} m</p>
            <p>Weight  :${response.weight} kg</p>
            <p>Species : ${response.species.name} </p>
            <p><div id = "abilities" alt="${idnow}">Abilities : ${response.abilities.length}</div> </p>
            `;
            console.log($("#abilities").attr("alt"));
            $(".card").html(stats); 
            $(".card2").html("");     
      });

$(document).on('click', '#abilities', function(){
      /*var ability = $(this).attr("abilities");   */
      var idnow = $(this).attr("alt");
      console.log($(idnow));
            $.get("https://pokeapi.co/api/v2/pokemon/"+ idnow +"/", function(response) {
            var abils =`${response.abilities[0].ability.name}`;
            var abils2 =`${response.abilities[1].ability.name}`;
            $(".card2").html("<p>" + abils + "</p><p>" + abils2 + "</p>");
      });

});});

});
