import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# 1. Environment
env = make_vec_env('battlesnake-v0', n_envs=4)

# 2. Model
model = PPO('MlpPolicy', env, verbose=1)

# 3. Train
model.learn(total_timesteps=100_000)

# 4. Save model
model.save("snake_model")
print("Model saved to snake_model.zip")

