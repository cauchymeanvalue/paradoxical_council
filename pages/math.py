import streamlit as st

st.set_page_config(page_title="The Mathematical Model", page_icon="🐸", layout="centered")

with open("style.css") as f:
	st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("The Model")
st.markdown("""
<h3>
1. How comes?
</h3>

<div class="description">
<p>
We are describing a paradoxical logic. So first of all = we need to imagine it as a mathematical function with some 
input and some output. In this case, we would like to input some different opinions and output after some time how the opinions changed, but also see
the general state of the system.
</p>
<p>
Let's start.
</p>
</div>
""", unsafe_allow_html=True )

st.markdown("""
---
### 1. Opinion update rule

Each member \( i )\ updates their opinion at every time step \( t )\ according to:

$$
x_i(t+1) = (1 - \alpha)x_i(t) + \alpha(1-R) + varepsilon_i(t)
$$

where

- \( x_i(t) \in [0,1] \) - opinion of member \( i )\ at the time \( t )\;
- \( \alpha \in [0,1] \) - conformity coefficient;
- \( \R )\ - the result of the previous voting, truth value of the system;
- \( \varepsilon_i(t) \sim U(-\text{noise}, \text{noise}) \) - random disturbances.

---

### 2. Paradoxical feedback

The system's truth value \( R \) inverts the majority’s view:

$$
R =
\begin{cases}
1, & \text{if } \bar{x}(t) < 0.5, \\
0, & \text{if } \bar{x}(t) \ge 0.5,
\end{cases}
$$

where \( \bar{x}(t) = \frac{1}{N}\sum_{i=1}^N x_i(t) \) is the average opinion.

Thus, when the majority believes “YES” (average \( >0.5 \)),  
the system forces the next step toward “NO”, and vice versa.

Now we have it - throw into our function all you know and wait.

---

### 3. Dynamical behavior

Depending on \( \alpha \) and the noise level, three regimes appear:

1. Stable consensus (group converges to 0 or 1)  
2. Oscillation (opinions swing between extremes)  
3. Chaotic behavior (no stable pattern emerges)

---

""")

st.markdown(r"""
### Model equations

$$
\begin{cases}
x_i(t+1) = (1 - \alpha)x_i(t) + \alpha(1 - R) + \varepsilon_i(t) \\
R =
\begin{cases}
1, & \text{if } \bar{x}(t) < 0.5 \\
0, & \text{if } \bar{x}(t) \ge 0.5
\end{cases}
\end{cases}
$$
""")

st.page_link("paradox.py", label="⬅️ Back to simulation", icon="🏠")











