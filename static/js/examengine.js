var currentquestion=0;
var totalquestions=0;
var status={
    name:"test",
    class:12,
    section:"A",
    answers:[]
}
var questions;
var answers=[];
function questionselect(quesno){
    $.post( "/getquestions", JSON.stringify({"qno": quesno}))
        .done(function( data ) {
            document.getElementById("questiontext").innerHTML=data['question'];
            var s="<option disabled selected>Select Your Answer</option>";
            for(var i=0; i<data['options'].length; i++) {
                s=s+'<option value="'+i+'">'+data['options'][i]+'</option>';
            }
            document.getElementById("answeroption").innerHTML=s;
    });
    currentquestion=quesno;
    var s="Question "+(parseInt(currentquestion)+1)+" of "+totalquestions;
    document.getElementById("questionnoviewer").innerHTML=s;
}
$(document).ready(function(){
    $.post( "/getquestions", JSON.stringify({"qno": "all"}))
        .done(function( data ) {
            questions=data;
            var s="";
            var arr;
            for(var i=0; i<data.length; i++) {
                s=s+'<span value="'+i+'" class="questionlist" onclick=\'questionselect(this.getAttribute("value"))\'>Question '+(parseInt(i)+1)+'</span><br>';
                answers.push(parseInt(-1));
            }
            document.getElementById("questionselectarea").innerHTML=s;
            totalquestions=data.length;
            status['answers']=answers;
    });
    questionselect(0);
    var s="Question "+(parseInt(currentquestion)+1)+" of "+totalquestions;
    document.getElementById("questionnoviewer").innerHTML=s;
});
function previous(){
    if(currentquestion==0)
    {
        currentquestion=totalquestions;
    }
    questionselect(parseInt(currentquestion)-1);
}

function next(){
    questionselect((parseInt(currentquestion)+1)%totalquestions);
}

function updateanswer(){
    window.answers[currentquestion]=parseInt(document.getElementById("answeroption").value);
    console.log(answers);
}