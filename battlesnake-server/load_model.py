from stable_baselines3 import PPO
import numpy as np

def load_model(path):
    return PPO.load(path)

def choose_move(game_state, model):
    # Hier musst du echte Features aus game_state extrahieren
    # → Aktuell nur Dummy-State
    state = np.zeros((11,), dtype=np.float32)
    action, _ = model.predict(state)
    return ["up", "down", "left", "right"][action]

