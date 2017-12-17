'use strict';
$(document).ready(function() {
 
  $('img').click(function(){
    $(this).hide();
});


    $( ".button[value ='Show All']").click(function() {
        $( 'img' ).show( "slow", function() {
          // Animation complete
        });
      });

    
    });


