import gymnasium as gym
import matplotlib.pyplot as plt
import cv2
import numpy as np

env = gym.make("FrozenLake-v1", render_mode="rgb_array")
env.reset()

while True:
    action = np.random.choice([0,1,2,3], 1)
    action = int(np.asarray(action).item())

    next_state, reward, term, _, _ = env.step(action)
    img = env.render()

    cv2.imshow("Image", img)
    cv2.waitKey(1000)
    
    if term == True:
        break

cv2.destroyAllWindows()

