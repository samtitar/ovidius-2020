import torch
import torch.nn as nn
import torch.optim

import numpy as np

from tqdm import trange
from models import Embedding
from torch.utils.data import DataLoader

N_EPOCHS = 1000
BATCH_SIZE = 256
LEARNING_RATE = 0.001

with open('data/structured/voacb_lemma.txt', 'r') as f:
    vocab = f.read().splitlines()
vocab_size = len(vocab)
data = np.identity(vocab_size)

dataloader = DataLoader(data, batch_size=BATCH_SIZE, shuffle=False)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

embedding = Embedding(vocab_size=vocab_size).to(device)
optimizer = torch.optim.Adam(embedding.parameters(), lr=LEARNING_RATE)
criterion = nn.MSELoss()

n_params = sum(p.numel() for p in embedding.parameters() if p.requires_grad)
print(f'n_params={n_params}')

iterator = trange(N_EPOCHS)
for epoch in iterator:
    for batch in dataloader:
        optimizer.zero_grad()

        batch = batch.float().to(device)

        y_hat = embedding(batch)

        loss = criterion(y_hat, batch)
        loss.backward()

        optimizer.step()
    iterator.set_description(f'L={loss.item()}')
