import streamlit as st
import streamlit.components.v1 as components

def render_flip_clock(focus_mins, break_mins):
    raw_html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: "Times New Roman", Times, serif; background-color: transparent; margin: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }
            .container { text-align: center; background: #FFFFFF; border: 1px solid #EADFC8; border-radius: 24px; padding: 2rem; box-shadow: 0 12px 28px rgba(43, 26, 16, 0.08); width: 90%; max-width: 500px; }
            .status-label { font-size: 1.5rem; font-weight: 800; color: #2B1A10; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 0.05em; }
            .clock { display: flex; justify-content: center; gap: 15px; margin-bottom: 2rem; }
            .flip-card { position: relative; display: inline-flex; flex-direction: column; width: 90px; height: 120px; box-shadow: 0 6px 12px rgba(0,0,0,0.15); border-radius: 12px; font-size: 4rem; font-weight: 800; line-height: 120px; color: #FFFFFF; background: #B34A29; }
            .flip-card::before { content: ""; position: absolute; left: 0; top: 50%; width: 100%; height: 2px; background: rgba(43, 26, 16, 0.2); z-index: 2; }
            .card-segment { text-align: center; width: 100%; }
            .label { font-size: 0.85rem; color: #7A6A5C; font-weight: bold; margin-top: 0.5rem; text-transform: uppercase; }
            .group { display: flex; flex-direction: column; align-items: center; }
            .colon { font-size: 4rem; line-height: 110px; color: #B34A29; font-weight: 800; }
            .controls { display: flex; justify-content: center; gap: 12px; }
            button { font-family: inherit; background: #FFFFFF; border: 1.5px solid #DCCDB0; border-radius: 12px; padding: 0.6rem 1.4rem; font-size: 1rem; font-weight: 600; color: #2B1A10; cursor: pointer; transition: all 0.2s ease; }
            button:hover { border-color: #B34A29; color: #B34A29; }
            button.primary { background: #B34A29; border-color: #B34A29; color: #FFFFFF; }
            button.primary:hover { background: #8D2D00; border-color: #8D2D00; color: #FFFFFF; }
        </style>
    </head>
    <body>
        <div class="container">
            <div id="status" class="status-label">Tiempo de Enfoque</div>
            <div class="clock">
                <div class="group"><div id="m-card" class="flip-card"><div class="card-segment" id="minutes">00</div></div><div class="label">Minutos</div></div>
                <div class="colon">:</div>
                <div class="group"><div id="s-card" class="flip-card"><div class="card-segment" id="seconds">00</div></div><div class="label">Segundos</div></div>
            </div>
            <div class="controls">
                <button id="startBtn" class="primary" onclick="toggleTimer()">Iniciar</button>
                <button id="resetBtn" onclick="resetTimer()">Reiniciar</button>
            </div>
        </div>
        <script>
            let focusTime = __FOCUS_MINS__ * 60;
            let breakTime = __BREAK_MINS__ * 60;
            let currentTime = focusTime; let isFocusMode = true; let timerId = null;
            const minutesDisplay = document.getElementById("minutes"); const secondsDisplay = document.getElementById("seconds"); const statusDisplay = document.getElementById("status"); const startBtn = document.getElementById("startBtn");
            function updateDisplay() { let mins = Math.floor(currentTime / 60); let secs = currentTime % 60; minutesDisplay.innerText = mins.toString().padStart(2, "0"); secondsDisplay.innerText = secs.toString().padStart(2, "0"); }
            function toggleTimer() { if (timerId) { clearInterval(timerId); timerId = null; startBtn.innerText = "Iniciar"; startBtn.classList.add("primary"); } else { startBtn.innerText = "Pausar"; startBtn.classList.remove("primary"); timerId = setInterval(() => { if (currentTime > 0) { currentTime--; } else { isFocusMode = !isFocusMode; currentTime = isFocusMode ? focusTime : breakTime; statusDisplay.innerText = isFocusMode ? "Tiempo de Enfoque" : "Descanso"; document.getElementById("m-card").style.background = isFocusMode ? "#B34A29" : "#4A8C67"; document.getElementById("s-card").style.background = isFocusMode ? "#B34A29" : "#4A8C67"; } updateDisplay(); }, 1000); } }
            function resetTimer() { clearInterval(timerId); timerId = null; isFocusMode = true; currentTime = focusTime; statusDisplay.innerText = "Tiempo de Enfoque"; startBtn.innerText = "Iniciar"; startBtn.classList.add("primary"); document.getElementById("m-card").style.background = "#B34A29"; document.getElementById("s-card").style.background = "#B34A29"; updateDisplay(); }
            updateDisplay();
        </script>
    </body>
    </html>
    '''
    final_html = raw_html.replace("__FOCUS_MINS__", str(focus_mins)).replace("__BREAK_MINS__", str(break_mins))
    components.html(final_html, height=350)
