
//uncomment to block right click
/*
document.oncontextmenu = function(e){
    var evt = new Object({keyCode:93});
    stopEvent(e);
    keyboardUp(evt);
}
function stopEvent(event){
    if(event.preventDefault != undefined)
     event.preventDefault();
    if(event.stopPropagation != undefined)
     event.stopPropagation();
}
*/
//uncomment to detect tab change
/*
$(window).focus(function() {
    console.log('you left');
    document.write('');
});
*/
$(document).ready(function(){
    $.get( "/testengine", function( data ) {
        $( "#form" ).html( data );
    });
});