var i = 0;
var txt = 'Never Lose a Connection Again! Connect with anyone, any wallet, and send transactions through an image of one\'s face!';
var speed = 50;

function typeWriter() {
    if (i < txt.length) {
        document.querySelector("#dynamic-content").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

typeWriter();