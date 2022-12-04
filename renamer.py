# read file in dataset
import glob
import os
from tqdm import tqdm

root = './datasets'
naming_rule = 'charin_polpanumas ([index]).jpg'
file_name = os.listdir(root)
for index in range(1, len(file_name) + 1):
    path = os.path.join(root, file_name[index - 1])
    # rename file
    os.rename(path, os.path.join(root, naming_rule.replace('[index]', str(index))))