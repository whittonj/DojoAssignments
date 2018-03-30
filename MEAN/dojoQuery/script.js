  
$(document).ready(
            
function(button){
      $('button').click(function(){
            console.log('getting');
      $.get('https://api.github.com/users/whittonj', displayName);
      });
            
function displayName(data){
      if (data.login){
      console.log('got '+data.login);
      $('body').append("<p>"+data.login+"</p>");
      }
      }
});