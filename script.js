const messageInput = document.querySelector(".message-input"); 

const handleOutgoingMessage = (userMessage) => {
    const messageContent = `<div class="message-text">${}</div>`;

}

messageInput.addEventListener("keydown", (e) => {
    const userMessage = e.target.value.trim();
    if(e.key === "Enter" && userMessage) {
        console.log("User message:", userMessage);
        handleOutgoingMessage(userMessage)
    }
}); 
