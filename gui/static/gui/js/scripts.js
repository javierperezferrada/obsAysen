(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  	$('.carousel.carousel-slider').carousel({fullWidth: true});
  	$('.carousel').carousel({dist:0});
        window.setInterval(function(){$('.carousel').carousel('next')},6000)
        
    $('.tooltipped').tooltip({delay: 50});    
  }); // end of document ready
})(jQuery); // end of jQuery name space
$( document ).ready(function() {
    console.log( "ready!" );
});