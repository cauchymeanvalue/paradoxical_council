import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- настройки страницы ---
st.set_page_config(page_title="Paradoxical Council", layout="centered", page_icon="❓")

with open("style.css") as f:
	st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Paradoxical Council Simulation")

# --- параметры интерфейса ---
n = st.slider("Number of members", 1, 50, 10)
alpha = st.slider("Readiness to change opinion (α)", 0.0, 1.0, 0.5, 0.01)
noise = st.slider("Noise level", 0.0, 1.0, 0.1, 0.01)
steps = st.slider("Simulation steps", 2, 100, 30)
speed = st.slider("Animation speed (sec per step)", 0.01, 0.3, 0.05)

col1, col2 = st.columns(2)
start = col1.button("▶️ Start / Resume")
pause = col2.button("⏸️ Pause")

# --- состояние ---
if "running" not in st.session_state:
    st.session_state.running = False
if start:
    st.session_state.running = True
if pause:
    st.session_state.running = False

# --- инициализация ---
x = np.random.rand(n)
matrix = np.zeros((steps, n))
history = []
plot_placeholder = st.empty()
status_placeholder = st.empty()

# --- подготовка графики ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
im = ax1.imshow(np.zeros((steps, n)), aspect='auto', cmap='coolwarm',
                origin='lower', vmin=0, vmax=1)
line, = ax2.plot([], [], color='black', linewidth=2)
ax1.set_title("Member opinions over time")
ax1.set_ylabel("Time")
ax1.set_xlabel("Members")
plt.colorbar(im, ax=ax1, orientation='vertical', fraction=0.03)
ax2.set_ylim(0, 1)
ax2.set_xlim(0, steps)
ax2.set_title("Average YES fraction")
ax2.set_xlabel("Step")
plt.tight_layout()

# --- основной цикл ---
for t in range(steps):
    if not st.session_state.running:
        break

    R = 1.0 if np.mean(x) < 0.5 else 0.0
    eps = np.random.uniform(-noise, noise, n)
    x = (1 - alpha) * x + alpha * (1 - R) + eps
    x = np.clip(x, 0, 1)

    matrix[t, :] = x
    history.append(np.mean(x))

    
    im.set_data(matrix[:t+1, :])
    line.set_data(range(len(history)), history)

    plot_placeholder.pyplot(fig, clear_figure=False)

    mean_val = np.mean(x)
    if mean_val > 0.7:
        status_placeholder.info("Majority says YES")
    elif mean_val < 0.2:
        status_placeholder.info("Majority says NO")
    else:
        status_placeholder.text("Debate in progress")
    time.sleep(0.05)

final = np.mean(x)

if final > 0.7:
	result_text = "Consensus on YES"
elif final < 0.3:
	result_text = "Consensus on NO"
else:
	result_text = "Oscillation or chaos in the end"

st.markdown("---")
st.markdown("Simulation End State")
st.markdown("Final average opinion", f"{final:.2f}")
st.info("Outcome: {result_text}")

st.info("Adjust parameters and press ▶️ Start to run simulation again.")

st.markdown("""
---
<p>
Each member has an opinion (0 - No, 1 - Yes). But the system is build strangely - an opinion is considered true only if the majority (>50%) disbelieves. <b>Alpha</b> controlls conformity, <b>noise</b> - chaotic elements.
</p> """ , unsafe_allow_html=True)

st.markdown("""
---
<div class="description">
<p>
This is a simple model-game (well, almost) that shows paradoxical decision-making: if the majority says <b>yes</b>, the system considers the correct answer to be <b>no</b>.
The cycle rules are simple: the system calculates the average opinion, flips it (if most are for, it outputs no), makes everyone adjust their opinion accordingly, adds a bit of randomness to keep things lively, and shows the results of the votes in real time.
In essence, it’s both a model of social feedback — like Instagram, where popularity can undermine belief — and a purely logical philosophical paradox. It also illustrates how even rational groups can behave chaotically when hidden internal rules exist, and what happens when a circle of decision-makers collectively refuses to follow the majority — when everyone rejects at once.
</p>
<p>
You may even see it as an illustration of what happens, when everyone believes he is the smartest and has great <i>critival thinking skills</i>.
</p>
<p>
The parameters are straightforward: the number of participants and the number of voting rounds; noise,me aning the random mood swings; and alpha, which is simply the willingness to change one’s mind depending on the crowd — the higher it is, the more conformist the group; the lower, the more stubborn the members.
Over time, the model can exhibit three main states: chaotic fluctuation, stabilization in one direction, or oscillation between the two. 
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
---
<h3>
To learn more about the math behind: 
</h3>
""", unsafe_allow_html=True )

st.page_link("pages/math.py", label="look...", icon="🐸") 
