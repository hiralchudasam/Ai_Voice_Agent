const recordBtn = document.getElementById("record-btn");
const personaSelect = document.getElementById("persona-select");
const personaStatus = document.getElementById("persona-status");
const status = document.getElementById("status");
const loader = document.getElementById("loader");
const chatHistory = document.getElementById("chat-history");
const clearChatBtn = document.getElementById("clear-chat-btn");

let mediaRecorder;
let audioChunks = [];
let isRecording = false;
let currentPersona = "default";

// Update persona status display
function updatePersonaStatus() {
    const selectedOption = personaSelect.options[personaSelect.selectedIndex];
    personaStatus.textContent = "Current: " + selectedOption.text;
    currentPersona = personaSelect.value;
}

// Initialize persona status
updatePersonaStatus();

// Listen for persona changes
personaSelect.addEventListener("change", updatePersonaStatus);

recordBtn.addEventListener("click", async () => {
    if (isRecording) {
        mediaRecorder.stop();
        recordBtn.disabled = true;
        recordBtn.textContent = "Start Recording..";
        status.textContent = "Processing...";
        loader.style.display = "inline";
        recordBtn.classList.remove("pulse");
        isRecording = false;
        return;
    }

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream, { mimeType: "audio/webm" });
        audioChunks = [];

        mediaRecorder.ondataavailable = (e) => {
            audioChunks.push(e.data);
        };

        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
            const formData = new FormData();
            formData.append("audio", audioBlob, "recording.webm");

            try {
                // First set the persona for this session
                await fetch("/persona", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ persona_name: currentPersona })
                });

                // Then send the audio query
                const response = await fetch("/llm/query", {
                    method: "POST",
                    body: formData,
                });

                if (!response.ok) throw new Error("Server error");

                const data = await response.json();

                const entry = document.createElement("div");
                entry.className = "chat-entry";

                const inputBox = document.createElement("div");
                inputBox.className = "input-box";
                inputBox.innerHTML = "<strong>You said:</strong><br>" + data.transcript;

                const outputBox = document.createElement("div");
                outputBox.className = "output-box";
                outputBox.innerHTML = "<strong>" + personaSelect.options[personaSelect.selectedIndex].text + " replied:</strong><br>" + data.llm_text;

                const timestamp = new Date().toLocaleTimeString();
                const timeBox = document.createElement("div");
                timeBox.className = "timestamp";
                timeBox.textContent = timestamp;

                entry.appendChild(inputBox);
                entry.appendChild(outputBox);
                entry.appendChild(timeBox);
                chatHistory.prepend(entry);
                entry.scrollIntoView({ behavior: "smooth" });

                try {
                    const audio = new Audio(data.audio_url);
                    await audio.play();
                } catch (e) {
                    console.warn("Audio playback failed:", e);
                    status.textContent += " Audio playback issue.";
                }

                status.textContent = data.error ? " " + data.error : " Response is ready!";
            } catch (err) {
                console.error(err);
                status.textContent = " " + (err.message || "Unknown error");
            } finally {
                recordBtn.disabled = false;
                recordBtn.textContent = "Start Recording";
                recordBtn.classList.add("pulse");
                loader.style.display = "none";
            }
        };

        mediaRecorder.start();
        recordBtn.textContent = "Stop Recording";
        status.textContent = "Recording...";
        loader.style.display = "none";
        recordBtn.classList.remove("pulse");
        isRecording = true;
    } catch (err) {
        console.error("Mic access failed:", err);
        status.textContent = "Microphone access denied.";
    }
});

// Clear chat functionality
clearChatBtn.addEventListener("click", () => {
    if (chatHistory.children.length > 0) {
        // Confirm before clearing
        if (confirm("Are you sure you want to clear all chat history?")) {
            chatHistory.innerHTML = '';
            status.textContent = "Chat history cleared!";
            
            // Clear status message after 2 seconds
            setTimeout(() => {
                status.textContent = "Ready to record";
            }, 2000);
        }
    } else {
        status.textContent = "Chat history is already empty!";
        setTimeout(() => {
            status.textContent = "Ready to record";
        }, 2000);
    }
});
