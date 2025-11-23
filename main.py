from tensorflow.keras.models import load_model
import gymnasium as gym
import numpy as np

model_path = 'lunar_lander_model.h5'

q_model = load_model(model_path)

env = gym.make('LunarLander-v3', render_mode= 'human')
obs, info = env.reset()
done = False
while not done:
    action = np.argmax(q_model(obs.reshape(1,-1)).numpy()[0])
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    print(reward)
print(reward)

