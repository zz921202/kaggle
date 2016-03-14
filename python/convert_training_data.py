import os
import numpy as np
import scipy.misc
import scipy.io as sio
import csv

mapping = {'airplane': 1, 'automobile': 2, 'bird': 3, 'cat': 4, 'deer': 5, 'dog': 6, 'frog': 7, 
           'horse': 8, 'ship': 9, 'truck': 10}

data_path = '/Users/Zhe/Documents/Kaggle_Project_Matlab/test_data/'

t = open(data_path + 'trainLabels.csv', 'r')
reader = list(csv.DictReader(t))

allfiles = os.listdir('%s/sample' % data_path)
num_imgs = len(allfiles) - 1

design_mat = np.zeros([num_imgs, 3072])
labels = np.zeros([num_imgs, 1])


for index in range(0, num_imgs):
    design_mat[index, :] = scipy.misc.imread('%s/train/%s.png' % (data_path, index + 1)).flatten()
    labels[index] = mapping[reader[index]['label']]


d1 = {'data': design_mat, 'labels': labels}

sio.savemat(data_path + '/train_head.mat', d1)