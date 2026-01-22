// Typing effect for futuristic feel
const text = "MANOJ SYSTEM INTERFACE :: ONLINE";
let i = 0;

function typeEffect() {
    if (i < text.length) {
        document.getElementById("type-text").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeEffect, 60);
    }
}

window.onload = typeEffect;
