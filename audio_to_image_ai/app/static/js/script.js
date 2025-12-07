const chat = document.getElementById('chat');
const actionBar = document.getElementById('actionBar');
const recordBtn = document.getElementById('recordBtn');
let currentPrompt = "";

function addMessage(text, sender, isImage = false) {
    const div = document.createElement('div');
    div.className = `bubble ${sender}`;

    if (isImage) {
        div.innerHTML = `<img src="${text}" class="generated-img" onclick="window.open('${text}')">`;
    } else {
        div.innerText = text;
    }

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

function showLoading() {
    const div = document.createElement('div');
    div.id = "loading";
    div.className = "bubble ai typing";
    div.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

function removeLoading() {
    const el = document.getElementById('loading');
    if (el) el.remove();
}

async function handleAudioUpload() {
    const fileInput = document.getElementById('audioInput');
    const file = fileInput.files[0];
    if (!file) return;

    // 1. Show User Audio Bubble
    addMessage(`🎤 Uploaded: ${file.name}`, 'user');

    // 2. Hide Mic, Show Loading
    recordBtn.style.display = 'none';
    showLoading();

    // 3. Send to Backend
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/process-audio', { method: 'POST', body: formData });
        if (!response.ok) throw new Error("Processing failed");
        const data = await response.json();

        removeLoading();

        // 4. Show Transcription & Prompt
        addMessage(`Transcription: "${data.transcribed_text}"`, 'ai');
        addMessage(`✨ Proposed Prompt:\n\n${data.generated_prompt}`, 'ai');

        currentPrompt = data.generated_prompt;

        // 5. Show Controls
        actionBar.style.display = 'flex';

    } catch (error) {
        removeLoading();
        addMessage("❌ Error: " + error.message, 'ai');
        recordBtn.style.display = 'flex';
    }

    // Reset input so same file can be selected again
    fileInput.value = '';
}

async function confirmGeneration() {
    actionBar.style.display = 'none';
    addMessage("Looks good! Generating image...", 'user');
    showLoading();

    try {
        const response = await fetch('/generate-image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: currentPrompt })
        });

        if (!response.ok) throw new Error("Generation failed");
        const data = await response.json();

        removeLoading();
        addMessage(data.image_url, 'ai', true);

        // Bring back Mic for new round
        recordBtn.style.display = 'flex';

    } catch (error) {
        removeLoading();
        addMessage("❌ Error: " + error.message, 'ai');
        recordBtn.style.display = 'flex';
    }
}

function resetProcess() {
    actionBar.style.display = 'none';
    recordBtn.style.display = 'flex';
    addMessage("Okay, let's try recording again.", 'user');
    document.getElementById('audioInput').click();
}

function retryPrompt() {
    alert("To refine the prompt, please record/upload again with more specific details!");
    resetProcess();
}
