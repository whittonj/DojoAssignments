'use strict';
$(document).ready(function() {
    

      $('img').click(function(){
          console.log('data-alt-src value is', $(this).attr('data-alt-src'));
          var temp= $(this).attr("data-alt-src");
          console.log(temp);
          $(this).attr("data-alt-src", $(this).attr("src"));
          $(this).attr("src", temp); 
          console.log($(this).attr("src"));       
    });

     
    });


