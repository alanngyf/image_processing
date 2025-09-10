import numpy as np
import torch
import random
import os

def seed_everything(seed: int):
    """
    To make sure the training process is reproducible, set a fixed random seed.
    Use the same seed for torch, numpy, and the random library.
    :param seed:
    :return:
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed) # CPU
    torch.cuda.manual_seed(seed) # GPU
    torch.backends.cudnn.deterministic = True # PyTorch to use deterministic algorithms on the GPU
    torch.backends.cudnn.benchmark = False # PyTorch will run a short benchmark at the start of training to find the fastest algorithm for your specific model architecture and input size.
