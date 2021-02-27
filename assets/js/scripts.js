$(document).ready(function() {
   $('#mycarousel').carousel({interval:2000});

   $("#loginbtn").click(function(){
     $("#loginmodal").modal('toggle');
   });
   $("#cancellogin").click(function(){
     $("#loginmodal").modal('hide');
   });
   $("#crosslogin").click(function(){
     $("#loginmodal").modal('hide');
   });

   $("#registerbtn").click(function(){
     $("#registermodal").modal('toggle');
   });
   $("#cancelregister").click(function(){
     $("#registermodal").modal('hide');
   });
   $("#crossregister").click(function(){
     $("#registermodal").modal('hide');
   });

 });
