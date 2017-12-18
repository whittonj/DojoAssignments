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
      var lstnm = $("input#ln").val();
      var email = $("input#em").val();
      var phn = $("input#ph").val();
      console.log(firstnm);
      $("table#dataset").append("<tr><td>"+firstnm + "<td>" + lstnm + "<td>" + email + "<td>" + phn);
      return false;
    });
  
});


