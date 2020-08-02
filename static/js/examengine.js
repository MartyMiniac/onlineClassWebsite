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
var totaltime;
var currenttime;
var timerstring='';
var timeup=false;
function questionselect(quesno){
    var data=questions[quesno];
    document.getElementById("questiontext").innerHTML=data['question'];
    var s="<option disabled selected>Select Your Answer</option>";
    for(var i=0; i<data['options'].length; i++) {
        s=s+'<option value="'+i+'">'+data['options'][i]+'</option>';
    }
    document.getElementById("answeroption").innerHTML=s;
    
    currentquestion=quesno;
    var s="Question "+(parseInt(currentquestion)+1)+" of "+totalquestions;
    document.getElementById("questionnoviewer").innerHTML=s;
}
$(document).ready(function(){
    $.post( "/getquestions", JSON.stringify({"qno": "all"}))
        .done(function( data ) {
            questions=data.data;
            var s="";
            var arr;
            for(var i=0; i<data.data.length; i++) {
                s=s+'<span value="'+i+'" class="questionlist" onclick=\'questionselect(this.getAttribute("value"))\'>Question '+(parseInt(i)+1)+'</span><br>';
                answers.push(parseInt(-1));
            }
            document.getElementById("questionselectarea").innerHTML=s;
            totalquestions=data.data.length;
            status['answers']=answers;
            totaltime=data.timelimit;
            console.log(totaltime);
            console.log(questions);
            currenttime=totaltime;
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


function updatetimerstring(t){
    var h=Math.floor(parseInt(t)/3600);
    t=t-3600*h;
    var m=Math.floor(parseInt(t)/60);
    t=t-60*m;
    var s=t;
    timerstring=h+' H '+m+' M '+s+' S'
    document.getElementById("timerviewer").innerHTML=timerstring;
}

setInterval(myTimer, 1000);

function myTimer() {
    if(timeup==false){
        if(totaltime-currenttime==1){
            questionselect(0);
        }
        currenttime=parseInt(currenttime)-1;
        updatetimerstring(currenttime)
        console.log(timerstring);
        if(currenttime==0){
            timeup=true;
            timerstring='Time Up';
            console.log('Time Up');
            document.getElementById("timerviewer").innerHTML=timerstring;
            finishsubmit();
        }
    }
}



function finishsubmit() {
    alert('Timeup');
}