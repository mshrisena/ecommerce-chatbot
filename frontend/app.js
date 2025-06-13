let userId = null;

window.addEventListener("DOMContentLoaded", () => {
  userId = localStorage.getItem("userId");
  if (userId) {
    document.getElementById("chat-container").style.display = "block";
    loadHistory(); // ✅ Load history on reload
  }

  document.getElementById("chat-form").addEventListener("submit", function (e) {
    e.preventDefault();
    sendMessage();
  });
});

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch("http://127.0.0.1:5001/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();

  if (res.ok) {
    userId = data.user_id;
    localStorage.setItem("userId", userId);
    alert("Login successful!");
    document.getElementById("chat-container").style.display = "block";
    loadHistory(); // ✅ Load messages after login
  } else {
    alert("Login failed.");
  }
}

function logout() {
  localStorage.removeItem("userId");
  location.reload();
}

async function sendMessage() {
  console.log("🟡 sendMessage triggered");

  const messageInput = document.getElementById("message");
  const message = messageInput.value.trim();
  if (!message) {
    console.log("⛔ No message to send.");
    return;
  }

  if (!userId) {
    alert("Please log in first.");
    return;
  }

  const chatBox = document.getElementById("chat-box");

  const userMsg = document.createElement("div");
  userMsg.className = "user-msg";
  userMsg.innerHTML = `🧑‍💻 <span>${message}</span>`;
  chatBox.appendChild(userMsg);
  messageInput.value = "";

  const typingEl = document.createElement("div");
  typingEl.className = "bot-msg typing";
  typingEl.innerHTML = `🤖 <span>Typing</span><span class="dots">...</span>`;
  chatBox.appendChild(typingEl);
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const res = await fetch("http://127.0.0.1:5001/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, user_id: userId })
    });

    const data = await res.json();
    typingEl.remove();

    if (data && data.response) {
      const botMsg = document.createElement("div");
      botMsg.className = "bot-msg";
      botMsg.innerHTML = `🤖 <span>${data.response}</span>`;
      chatBox.appendChild(botMsg);
    } else {
      chatBox.innerHTML += `<div class="bot-msg">🤖 <span>⚠️ Bot did not respond.</span></div>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    console.error("SendMessage error:", err);
    typingEl.remove();
    chatBox.innerHTML += `<div class="bot-msg">🤖 <span>⚠️ Failed to connect to server.</span></div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  }
}

async function loadHistory() {
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML = `<div class="bot-msg">Loading previous chats...</div>`;

  const res = await fetch(`http://127.0.0.1:5001/chat/history?user_id=${userId}`);
  const data = await res.json();

  chatBox.innerHTML = "";
  data.reverse().forEach(chat => {
    const userMsg = document.createElement("div");
    userMsg.className = "user-msg";
    userMsg.innerHTML = `🧑‍💻 <span>${chat.message}</span>`;

    const botMsg = document.createElement("div");
    botMsg.className = "bot-msg";
    botMsg.innerHTML = `🤖 <span>${chat.response}</span>`;

    chatBox.appendChild(userMsg);
    chatBox.appendChild(botMsg);
  });

  chatBox.scrollTop = chatBox.scrollHeight;
}

function startVoice() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onresult = function (event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("message").value = transcript;
    sendMessage();
  };

  recognition.onerror = function (event) {
    alert("Voice input error: " + event.error);
  };

  recognition.start();
}