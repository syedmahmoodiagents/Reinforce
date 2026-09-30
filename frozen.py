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
    
    policy = [1, 3, 0, 3, 0, 0, 1, 0, 3, 1, 0, 0, 0, 2, 1, 0]
    state = 0
    while not done:
        action = policy[state]
        action = int(np.asarray(action).item())

        next_state, reward, term, truncated, _ = env.step(action)
        img = env.render()
        state = next_state
        frame_placeholder.image(img, width=400)
        
        time.sleep(1.0)
        done = term or truncated
        
    env.close()
