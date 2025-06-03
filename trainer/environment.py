import gym
from gym import spaces
import numpy as np
from game_simulator import simulate_game

class SnakeEnv(gym.Env):
    def __init__(self):
        super(SnakeEnv, self).__init__()
        self.action_space = spaces.Discrete(4)  # 0=up, 1=down, 2=left, 3=right
        self.observation_space = spaces.Box(low=0, high=1, shape=(11,), dtype=np.float32)
        self.state = None

    def reset(self):
        self.state = np.zeros(11, dtype=np.float32)
        return self.state

    def step(self, action):
        next_state, reward, done = simulate_game(self.state, action)
        self.state = next_state
        return next_state, reward, done, {}

    def render(self, mode="human"):
        print("State:", self.state)

