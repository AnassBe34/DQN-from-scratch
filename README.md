# Deep Q-Learning (DQN) from scratch on LunarLander

Overview
- This repository contains a from-scratch implementation of Deep Q-Learning (DQN) applied to the OpenAI Gym LunarLander environment and a small script to load and run a trained model.

Contents
- [dqn.ipynb](dqn.ipynb) — Jupyter notebook implementing DQN from scratch, Q-network, replay buffer, epsilon-greedy policy,target network synchronization, and training loop.
- [main.py](main.py) — script that loads a saved trained model using dqn implemented in dqn.ipynb and runs the agent in the environment.
- [lunar_lander_model.h5](lunar_lander_model.h5) — the trained model saved by the notebook (expected by main.py).
- [requirements.txt](requirements.txt) — project dependencies.

Quick start
1. Install dependencies:
```sh
pip install -r requirements.txt
```
2. Run the viewer script:
```sh
python main.py
```

How to use
- The notebook [dqn.ipynb](dqn.ipynb) trains the agent and saves the model to `lunar_lander_model.h5`.
- The script [main.py](main.py) loads the saved model using the symbol [`main.model_path`](main.py) and selects actions with the loaded model.

Core idea
- The DQN update uses the Bellman optimality target:  
Q(s, a) = r + γ * max_{a'} Q(s', a')


Notes
- Rendering: [main.py](main.py) uses Gymnasium with `render_mode='human'` and expects a graphical display.
- Ensure `lunar_lander_model.h5` is present at the repository root before running [main.py](main.py).
- Tweak hyperparameters in [dqn.ipynb](dqn.ipynb) to retrain or improve performance.
