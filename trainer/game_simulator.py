import numpy as np

def simulate_game(state, action):
    # Einfache Dummy-Logik: Zustand leicht verändern
    next_state = state + (np.random.rand(11) - 0.5) * 0.1
    next_state = np.clip(next_state, 0, 1)

    reward = 1.0
    done = np.random.rand() < 0.01  # 1% Chance, dass Spiel vorbei ist

    return next_state, reward, done

