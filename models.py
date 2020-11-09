import torch
import torch.nn as nn

class Embedding(nn.Module):
    def __init__(self, vocab_size=10000, encoding_size=512):
        super(Embedding, self).__init__()

        self.encode = nn.Sequential(
            torch.nn.Linear(vocab_size, encoding_size)
            # torch.nn.Linear(vocab_size // 2, vocab_size // 4),
            # torch.nn.Linear(vocab_size // 4, vocab_size // 8),
            # torch.nn.Linear(vocab_size // 2, encoding_size)
        )

        self.decode = nn.Sequential(
            torch.nn.Linear(encoding_size, vocab_size)
            # torch.nn.Linear(vocab_size // 8, vocab_size // 4),
            # torch.nn.Linear(vocab_size // 4, vocab_size // 2),
            # torch.nn.Linear(vocab_size // 2, vocab_size)
        )

    def forward(self, x):
        y = self.encode(x)
        y = self.decode(y)
        return y
