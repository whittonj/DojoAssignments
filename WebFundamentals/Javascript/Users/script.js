'use strict';
$(document).ready(function() {
 
    $('form').submit(function(){
      var firstnm = $("input#fn").val();
      var lstnm = $("input#ln").val();
      var email = $("input#em").val();
      var phn = $("input#ph").val();
      console.log(firstnm);
      $("table#dataset").append("<tr><td>"+firstnm + "<td>" + lstnm + "<td>" + email + "<td>" + phn);
      return false;
    });
  
});


