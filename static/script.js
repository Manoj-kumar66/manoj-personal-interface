let started = false;

document.addEventListener("click", () => {
    if (!started) {
        started = true;

        const sound = new Audio("/static/startup.mp3");
        sound.volume = 0.7;
        sound.play().catch(err => console.log(err));

        startTyping();
    }
});

function startTyping() {
    const text = "SYSTEM BOOTING...\nAI CORE ONLINE\nWELCOME MANOJ";
    let i = 0;
    const speed = 50;

    const output = document.getElementById("terminal");

    function type() {
        if (i < text.length) {
            output.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}
