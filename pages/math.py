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
We are describing a paradoxical logic. So first of all — we need to imagine it as a mathematical function with some 
input and some output. In this case, we would like to input some different opinions and output after some time how the opinions changed, but also see
the general state of the system.
</p>
<p>
Let's start.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown(r"""
---
### 1. Opinion update rule

Each member \( i \) updates their opinion at every time step \( t \) according to:

$$
x_i(t+1) = (1 - \alpha)x_i(t) + \alpha(1-R) + \varepsilon_i(t)
$$

where:
</p>

""")

st.write(r"$x_i(t) \in [0,1]$ — opinion of member $i$ at time $t$;")

st.write(r"$\alpha \in [0,1]$ — conformity coefficient;")

st.write(r"$R$ — result of the previous voting (truth value of the system);")

st.write(r"$\varepsilon_i(t) \sim U(-\text{noise}, \text{noise})$ — random disturbances.")


st.markdown("---")

st.markdown(r"""



### 2. Paradoxical feedback

The system's truth value \( R \) inverts the majority’s view:

$$
R =
\begin{cases}
1, & \text{if } \bar{x}(t) < 0.5, \\
0, & \text{if } \bar{x}(t) \ge 0.5
\end{cases}
$$

where  

$$
\bar{x}(t) = \frac{1}{N}\sum_{i=1}^N x_i(t)
$$

is the average opinion.

Thus, when the majority believes “YES” (average \( > 0.5 \)),  
the system forces the next step toward “NO”, and vice versa.

Now we have it — throw into our function all you know and wait.

---

### 3. Dynamical behavior

Depending on \( \alpha \) and the noise level, three regimes appear:

1. Stable consensus (group converges to 0 or 1);  
2. Oscillation (opinions swing between extremes);  
3. Chaotic behavior (no stable pattern emerges).

---
""")

st.markdown(r"""
### Model equations

$$
\begin{cases}
x_i(t+1) = (1 - \alpha)x_i(t) + \alpha(1 - R) + \varepsilon_i(t), \\
R =
\begin{cases}
1, & \text{if } \bar{x}(t) < 0.5, \\
0, & \text{if } \bar{x}(t) \ge 0.5
\end{cases}
\end{cases}
$$
""")

st.markdown("""

<p>
This system is a <b>nonlinear map</b> with a discontinuous feedback function. 
The discontinuity at $\\bar{x} = 0.5$ creates a <b>bifurcation</b> that can lead 
to complex dynamics including limit cycles and chaos.
</p>
<p>
The interplay between deterministic feedback (the paradox) and stochastic noise 
($\\varepsilon$) determines whether the system converges, oscillates, or exhibits 
chaotic behavior.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""

<div class="description">
   <h3> 
   The Lyapunov exponent measures sensitivity to initial conditions:
   </h3>

   <p>
   The Lyapunov exponent in itself shows how fast do two very, <i>very</i> close trajectories diverge. Here is it:
   </p>

   <p>
   {\displaystyle |{\boldsymbol {\delta }}(t)|\approx e^{\lambda t}|{\boldsymbol {\delta }}_{0}|}
   </p>
   <p>
   I'm sure doesn't look like anything that makes sence to you. That's ok. 
   </p>
   
   <p>
    - λ > 0: Chaotic regime (exponential divergence)
    - λ = 0: Periodic or quasi-periodic behavior
    - λ < 0: Stable convergence
   </p>
    <p>
    For this system, λ depends critically on α and noise.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.page_link("paradox.py", label="⬅️ Back to simulation", icon="🏠")
