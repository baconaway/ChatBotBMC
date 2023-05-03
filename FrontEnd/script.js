document.addEventListener("DOMContentLoaded", () => {
    const chatHistory = document.getElementById("chat-history");
    const messageInput = document.getElementById("message-input");
    const sendButton = document.getElementById("send-button");
    const clearButton = document.getElementById("clear-button");

    function displayMessage(role, message) {
      const messageElement = document.createElement("div");
      messageElement.className = role;
      messageElement.textContent = `${role}: ${message}`;
      chatHistory.appendChild(messageElement);
      chatHistory.scrollTop = chatHistory.scrollHeight;
    }
  
    sendButton.addEventListener("click", async () => {
      const userMessage = messageInput.value.trim();
  
      if (userMessage) {
          displayMessage("You", userMessage);
          messageInput.value = "";
  
          // Fetch chatbot response (replace the URL with your backend API endpoint)
          const response = await fetch("http://localhost:5000/chat", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify({ message: userMessage }),
          });
  
          if (response.ok) {
              const responseData = await response.json();
              displayMessage("Chatbot", responseData.assistant_message);
          } else {
              displayMessage("Error", "Unable to fetch chatbot response. Please try again later.");
          }
         }
      function clearChat() {
        chatHistory.innerHTML = "";
        }
    
    clearButton.addEventListener("click", clearChat);
  
    // Add an event listener for the Enter key
    sendButton.addEventListener("keydown", (event) => {
          if (event.key === "Enter") {
              const userMessage = messageInput.value.trim();
          }
    });
   });
});
