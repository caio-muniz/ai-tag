import random

import torch
import torch.nn as nn
import torch.optim as optim

from dqn import DQN
from replay_buffer import ReplayBuffer


class DQNTrainer:
    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = DQN().to(self.device)
        self.target_model = DQN().to(self.device)

        self.target_model.load_state_dict(
            self.model.state_dict()
        )

        self.target_model.eval()

        self.memory = ReplayBuffer(10000)

        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=0.001
        )

        self.loss_function = nn.MSELoss()

        self.gamma = 0.99

        self.epsilon = 1.0
        self.epsilon_min = 0.05
        self.epsilon_decay = 0.995

        self.batch_size = 64

        self.update_counter = 0
        self.target_update_frequency = 100

    def select_action(self, state):

        if random.random() < self.epsilon:
            return random.randint(0, 3)

        state_tensor = torch.tensor(
            state,
            dtype=torch.float32,
            device=self.device
        ).unsqueeze(0)

        with torch.no_grad():
            q_values = self.model(state_tensor)

        return q_values.argmax(dim=1).item()

    def train_step(self):

        if len(self.memory) < self.batch_size:
            return

        batch = self.memory.sample(self.batch_size)

        states, actions, rewards, next_states, dones = zip(*batch)

        states = torch.tensor(
            states,
            dtype=torch.float32,
            device=self.device
        )

        actions = torch.tensor(
            actions,
            dtype=torch.long,
            device=self.device
        ).unsqueeze(1)

        rewards = torch.tensor(
            rewards,
            dtype=torch.float32,
            device=self.device
        )

        next_states = torch.tensor(
            next_states,
            dtype=torch.float32,
            device=self.device
        )

        dones = torch.tensor(
            dones,
            dtype=torch.float32,
            device=self.device
        )

        current_q_values = self.model(states).gather(
            1,
            actions
        ).squeeze(1)

        with torch.no_grad():

            next_q_values = self.target_model(
                next_states
            ).max(1)[0]

            target_q_values = (
                rewards
                + self.gamma * next_q_values * (1 - dones)
            )

        loss = self.loss_function(
            current_q_values,
            target_q_values
        )

        self.optimizer.zero_grad()

        loss.backward()

        torch.nn.utils.clip_grad_norm_(
            self.model.parameters(),
            1.0
        )

        self.optimizer.step()

        self.update_counter += 1

        if self.update_counter % self.target_update_frequency == 0:
            self.target_model.load_state_dict(
                self.model.state_dict()
            )

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self, path):
        torch.save(
            self.model.state_dict(),
            path
        )

    def load(self, path):
        self.model.load_state_dict(
            torch.load(
                path,
                map_location=self.device
            )
        )

        self.target_model.load_state_dict(
            self.model.state_dict()
        )
