'use strict';
$(document).ready(function() {
 
    $('form').submit(function(){
      var firstnm = $("input#fn").val();
      var lstnm = $("input#ln").val();
      var descr = $("textarea#de").val();
      console.log(firstnm);
      console.log(lstnm);
      console.log(descr);
      $(".right").append("<div class ='card'>" + "<h1>" +firstnm + " " + lstnm + "</h1>" + "<p>" + descr + "</p>" + "</div>");
      return false;
    });

    $(document).on('click', '.card', function(){
      console.log($(this));
      $(this).children("p").show("slow");
      $(this).children("h1").hide("slow");
      });
  });
  



