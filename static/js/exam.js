
//uncomment to block right click
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
//uncomment to detect tab change
$(window).focus(function() {
    window.location.href = "/caughtcheating";
    console.log('you left change');
});
$(document).ready(function(){
    $.get( "/testengine", function( data ) {
        $( "#form" ).html( data );
    });
});