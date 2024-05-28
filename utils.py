import torch
from torch.utils.data as data


class CharTokenizer:
    def __init__(self):
        f = open("input.txt", "r")
        text = f.read()

        self.unique_chars = sorted(list(set(text)))
        self.itos = {i: char for i, char in enumerate(self.unique_chars)}
        self.stoi = {char: i for i, char in enumerate(self.unique_chars)}

    def encode(self, chars):
        return [self.stoi[c] for c in chars]

    def decode(self, ints):
        return "".join([self.itos[i] for i in ints])


class ShakespeareDataset(data.Dataset)


def test():
    tok = CharTokenizer()

    print("".join(tok.unique_chars))

    encoded_chars = tok.encode("hey there")

    print(encoded_chars)
    print(tok.decode(encoded_chars))


if __name__ == "__main__":
    test()
