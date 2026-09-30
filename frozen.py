import gymnasium as gym
import streamlit as st
import numpy as np
import time

st.title("Frozen Lake")
env = gym.make("FrozenLake-v1", render_mode="rgb_array")

frame_placeholder = st.empty()
if st.button("Run Simulation"):
    env.reset()
    done = False
    policy = [0, 3, 3, 3, 0, 0, 0, 0, 3, 1, 0, 0, 0, 2, 1, 0]
    while not done:
        
        action = np.random.choice([0, 1, 2, 3], 1)
        action = int(np.asarray(action).item())

        next_state, reward, term, truncated, _ = env.step(action)
        img = env.render()

        frame_placeholder.image(img, width=400)
        
        time.sleep(1.0)
        done = term or truncated
        
    env.close()
