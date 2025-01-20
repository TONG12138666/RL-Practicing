import numpy as np
import gym
import time 

env = gym.make('CartPole-v1', render_mode='human')
state = env.reset()
done = False

while not done:
    env.render()
    action = np.random.choice([0, 1])
    next_state, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    time.sleep(0.2)  

env.close()
