import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.markdown(
	"""
	### Model description: Each member has an opinion (0 - No, 1 - Yes). But the system is build strangely - an opinion is considered true only if the majority (<50%) disbelieves. Alpha controlls conformity, noise - chaotic elements. """

	"""
	<style>
	body {background-color: #000066; color: #FFFFFF;}
	h1 {color: #FFFFFF;}
	<\style>
	""",
	unsafe_allow_html=True
)


# --- настройки страницы ---
st.set_page_config(page_title="Paradoxical Council", layout="centered")
st.title("Paradoxical Council Simulation")

# --- параметры интерфейса ---
n = st.slider("Number of members", 2, 50, 10)
alpha = st.slider("Readiness to change opinion (α)", 0.0, 1.0, 0.5, 0.01)
noise = st.slider("Noise level", 0.0, 1.0, 0.1, 0.01)
steps = st.slider("Simulation steps", 10, 500, 100)
speed = st.slider("Animation speed (sec per step)", 0.01, 0.3, 0.05)

# --- элементы управления ---
col1, col2 = st.columns(2)
start = col1.button("▶️ Start / Resume")
pause = col2.button("⏸️ Pause")

# --- внутренние переменные ---
x = np.random.rand(n)
matrix = np.zeros((steps, n))
history = []
plot_placeholder = st.empty()

# --- выполнение симуляции ---
if "running" not in st.session_state:
    st.session_state.running = False

if start:
    st.session_state.running = True
if pause:
    st.session_state.running = False

message = st.empty()

# --- основной цикл ---
for t in range(steps):
    if not st.session_state.running:
        break  # останавливаем симуляцию

    R = 1.0 if np.mean(x) < 0.5 else 0.0
    eps = np.random.uniform(-noise, noise, n)
    x = (1 - alpha) * x + alpha * (1 - R) + eps
    x = np.clip(x, 0, 1)

    matrix[t, :] = x
    history.append(np.mean(x))

    # --- визуализация ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    im = ax1.imshow(matrix[:t+1, :], aspect='auto', cmap='coolwarm',
                    origin='lower', vmin=0, vmax=1)
    ax1.set_title("Member opinions over time")
    ax1.set_ylabel("Time")
    ax1.set_xlabel("Members")
    plt.colorbar(im, ax=ax1, orientation='vertical', fraction=0.03)
    ax2.plot(history, color='black', linewidth=2)
    ax2.set_ylim(0, 1)
    ax2.set_title("Average YES fraction")
    ax2.set_xlabel("Step")
    plt.tight_layout()
    if np.mean(x) > 0.7:
        message.info("Majority says yes")
    elif np.mean(x) < 0.2:
        message.info("Majority says no")
    else:
        message.text("Debate in progress")
    time.sleep(1)
    message.empty()
    plot_placeholder.pyplot(fig)
    time.sleep(speed)

st.info("Adjust parameters and press ▶️ Start to run simulation again.")