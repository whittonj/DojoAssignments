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
    $( ".button[value ='Try Fade In']").click(function() {
        $( "#fadein" ).fadeIn( "slow", function() {
            // Animation complete
          });
      });
    
      $( ".button[value ='Try Fade Out']").click(function() {
        $( "#fadein" ).fadeOut( "slow", function() {
            // Animation complete
          });
      });
      
      $( ".button[value ='Try Hide']").click(function() {
      $( "#hider" ).hide( "slow", function() {
        // Animation complete
      });
    });

    $( ".button[value ='Try Show']").click(function() {
        $( "#hider" ).show( "slow", function() {
          // Animation complete
        });
      });

      $( ".button[value ='Try Slide Up']").click(function() {
        $( "#slider" ).slideUp( "slow", function() {
          // Animation complete
        });
      });

      $( ".button[value ='Try Slide Down']").click(function() {
        $( "#slider" ).slideDown( "slow", function() {
          // Animation complete
        });
      });

      $( ".button[value ='Try Slide Toggle']").click(function() {
        $( "#slidetog" ).slideToggle( "slow", function() {
          // Animation complete
        });
      });

      $( ".button[value ='Try Toggle']").click(function() {
        $( "img#toggle" ).toggle();
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

      $( ".button[value ='Add Serifs']").click(function() {
        $( "p" ).removeClass( "sans" ); 
        $( "p" ).addClass( "serif" ); 
       });

      $( ".button[value ='Sans Serifs']").click(function() {
        $( "p" ).removeClass( "serif" ); 
        $( "p" ).addClass( "sans" ); 
      });

      $( ".button[value ='Try Append']").click(function() {
        $( "h1" ).append( "> " ); 
      });

      $( ".button[value ='DO NOT CLICK']").click(function() {
        for (var i=10; i<500; i++) {        
        $( ".button" ).css( "padding", i);
        console.log(i);
        }
      });

    });


