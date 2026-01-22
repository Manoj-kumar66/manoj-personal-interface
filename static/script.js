function login() {
    const pin = document.getElementById("pin").value;

    if (pin === "1234") {   // change your pin
        window.location.href = "/dashboard";
    } else {
        alert("ACCESS DENIED");
    }
}
