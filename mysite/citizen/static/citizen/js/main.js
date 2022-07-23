$(document).ready(function() {

    $('.education__title').click(function(event){
        $(this).toggleClass('active').next().slideToggle(300);
    });
 });

