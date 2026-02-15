async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = inputField.value;
    if (!message) return;

    // Show user message
    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

    inputField.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Show Gemini reply
    chatBox.innerHTML += `<p><b>Gemini:</b> ${data.reply}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
