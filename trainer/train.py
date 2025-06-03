import os
from environment import SnakeEnv
from stable_baselines3 import PPO

# 1. Environment
env = SnakeEnv()

# 2. Model
model = PPO('MlpPolicy', env, verbose=1)

# 3. Train
model.learn(total_timesteps=100_000)

# 4. Save model
model.save("snake_model")
print("Model saved to snake_model.zip")

