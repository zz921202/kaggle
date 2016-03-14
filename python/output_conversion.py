import os
import numpy as np
import scipy.misc
import scipy.io as sio
import csv

curdir = os.path.dirname(os.path.realpath(__file__))
data_path = '/Users/Zhe/Documents/Kaggle_Project_Matlab/test_data'


mapping = {'airplane': 1, 'automobile': 2, 'bird': 3, 'cat': 4, 'deer': 5, 'dog': 6, 'frog': 7, 
           'horse': 8, 'ship': 9, 'truck': 10}

reverse_mapping = dict((v, k) for k, v in mapping.items())

# convert result back to cs

mat_data = sio.loadmat('test_out.mat')
with open('test_out.csv', 'w') as f:
    a = csv.writer(f)
    a.writerow(['id', 'label'])
    print mat_data
    for (row, label) in enumerate(mat_data['labels'].flatten()):
        to_write = [str(row + 1), str(reverse_mapping[label ])]
        a.writerow(to_write)

