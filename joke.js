var button = document.getElementById("click")
var select = document.getElementById("options");
let synth = speechSynthesis;
speaking = true;
voices = null;
function generate_joke() {
    JokeAPI.getJokes({
        jokeType: "single"
      })
        .then((r) => r.json())
        .then((data) => {
            document.getElementById("joke").innerHTML = data.joke;
            let utterance = new SpeechSynthesisUtterance(document.getElementById("joke").innerHTML);
            utterance.voice = voices[select.selectedIndex];
            speechSynthesis.speak(utterance);
      });
}

button.onclick = function() {
    if (!synth.speaking) {
        generate_joke();
    }
}

window.speechSynthesis.onvoiceschanged = function() {
    voices = window.speechSynthesis.getVoices();
    for (let i = 0; i < voices.length; i++) {
        var opt = document.createElement('option');
        opt.value = i;
        opt.innerHTML = voices[i].lang;
        console.log(voices[i]);
        select.appendChild(opt);
    }
};
function giveInfo(evt,infoName){
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for(i = 0;i < tabcontent.length;i++){
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for(i = 0;i < tablinks.length;i++){
        tablinks[i].className = tablinks[i].className.replace(" active","");
    }
    document.getElementById(infoName).style.display = "block";
    evt.currentTarget.className += " active";
}
