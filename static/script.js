function toggleDark() {
    document.body.classList.toggle("light-mode");
}

// Fake wallet login
function login() {
    let wallet = document.getElementById("wallet").value;

    if (wallet === "") {
        alert("Enter wallet ID");
        return;
    }

    document.getElementById("user").innerText =
        "Connected: " + wallet;
}
