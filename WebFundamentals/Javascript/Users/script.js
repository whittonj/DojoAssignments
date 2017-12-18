'use strict';
$(document).ready(function() {
    /*$('h1').css ("color", "red");*/
    //$('.para1').hide(); /* .remove - completely removes it from page & code */
    /*$('.para2').click (function() {
        $("h1").css ("color", "#333333");
    })
    $('h2').click (function() {
        $(this).fadeOut(5000, function(){ console.log("Done!")});
        $("body").append("<h1>Hello stuff</h1");
    })
    $("body").on ("click", "h1", function(){ 
        $("body").append("<h1>Hello stuff</h1");
    })
    $('h3').attr("class", "classname");
    console.log($('h3').attr("class"));//
    */
    $('form').submit(function(){
      var firstnm = $("input#fn").val();
      console.log(firstnm);
      return false;
      
      
    });
    
    

      $( ".button[value ='Try html']").click(function() {
        $( "div.demo" ).html("<h3>Goodbye world</h3>" ); 
      });

      $( ".button[value ='Try text']").click(function() {
        $( "div.demo" ).text("<h3>Goodbye world</h3>" ); 
      });

      $( ".button[value ='Try Before']").click(function() {
        $( "div.demo-before").before("+ + + " ); 
      });

      $( ".button[value ='Try After']").click(function() {
        $( "div.demo-before").after("- - - " ); 
      });

      $( ".button[value ='Try attr']").click(function() {
        var alt = $( "#cat" ).attr( "alt" );
        $( "altthis" ).text( alt );
      });

      $( ".button[value ='Try val']").click(function() {
        var alt = $( "#cat" ).attr( "alt" );
        $( "input#valbox" ).val( "You tried .val" );
      });

      $( ".button[value ='Store Data']").click(function() {
        $("body").data("First Item", 42 ); 
        console.log("Data stored");
      });
  
      $( ".button[value ='Get Data']").click(function() {
        console.log($("body").data()); 
      });

      

      $( ".button[value ='Try Append']").click(function() {
        $( "h1" ).append( "> " ); 
      });

    

    });


