import torch
import torch.nn as nn


class DQN(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(2, 64)
        self.layer2 = nn.Linear(64, 64)
        self.output = nn.Linear(64, 4)

    def forward(self, state):
        x = torch.relu(self.layer1(state))
        x = torch.relu(self.layer2(x))
        return self.output(x)
