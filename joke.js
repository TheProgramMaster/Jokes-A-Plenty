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
    for (let i = 0; i < voice_options.length; i++) {
        var opt = document.createElement('option');
        opt.value = i;
        opt.innerHTML = voice_options[i];
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

voice_options = [
    "American",
    "Italian",
    "Swiss",
    "Canadian",
    "German",
    "Isreali",
    "Indonesia",
    "British",
    "Argentinian",
    "Belgian",
    "English",
    "American",
    "Romanian",
    "Portugal",
    "Spanish",
    "Mexican",
    "Thai",
    "Australian",
    "Japanese",
    "Slovakian",
    "Indian",
    "Italian",
    "Brazilian",
    "South African",
    "Hungarian",
    "Taiwanese",
    "Greek",
    "Russian",
    "Irish",
    "Spanish",
    "Norwegian",
    "Mexican",
    "Indian",
    "American",
    "Danish",
    "Finnish",
    "Cantonese",
    "South African",
    "French",
    "Chinese",
    "Indonesian",
    "American",
    "Nordic",
    "Turkish",
    "Korean",
    "Russian",
    "Polish",
    "Czech",
    "German",
    "American",
    "British",
    "English",
    "Spanish",
    "Spanish-American",
    "French",
    "Indian",
    "Indonesian",
    "Italian",
    "Japanese",
    "Korean",
    "Dutch",
    "Polish",
    "Brazilian",
    "Russian",
    "Chinese",
    "Cantonese",
    "Taiwanese"
]
