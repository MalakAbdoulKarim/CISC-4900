const chatBody = document.querySelector(".chat-body"); 
const messageInput = document.querySelector(".message-input"); 
const sendMessageButton = document.querySelector("#send-message"); 
const uploadFileButton = document.querySelector("#file-upload");

const userData = {
    message : null
}

// or url here API_URL
const API_KEY = ``;


const createMessageElement = (content, ...classes) => {
    const div = document.createElement("div");
    div.classList.add("message", ...classes); 
    div.innerHTML = content; 
    return div;
}

const handleOutgoingMessage = (e) => {
    e.preventDefault();
    userData.message = messageInput.value.trim();
    messageInput.value = "";

    // Create and append outgoing message element   
    const messageContent = `<div class="message-text">${userData.message}</div>`;

    const outgoingMessageDiv = createMessageElement( messageContent,"user-message");
    outgoingMessageDiv.querySelector(".message-text").textContent = userData.message;
    chatBody.appendChild(outgoingMessageDiv);

    // Simulate bot response after a delay 
    setTimeout(() => {
        const messageContent = `<div class="message bot-message thinking">
                <div class="message-text">
                    <div class ="thinking-dots">
                        <div class="dot"></div>
                        <div class="dot"></div>
                        <div class="dot"></div>`;

    const incomingMessageDiv = createMessageElement( messageContent,"bot-message", "thinking");
    chatBody.appendChild(incomingMessageDiv);
    }, 600);
}

// Enter key press for sending message 
messageInput.addEventListener("keydown", (e) => {
    const userMessage = e.target.value.trim();
    if(e.key === "Enter" && userMessage) {
        handleOutgoingMessage(e); 
    }
}); 

sendMessageButton.addEventListener("click", (e) => handleOutgoingMessage(e))
document.querySelector("#file-upload").addEventListener("click", () => fileInput.click);

