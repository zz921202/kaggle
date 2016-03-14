import os
import numpy as np
import scipy.misc
import scipy.io as sio
import csv

curdir = os.path.dirname(os.path.realpath(__file__))
data_path = '/Users/Zhe/Documents/Kaggle_Project_Matlab/test_data/'
allfiles = os.listdir('%s/test' % data_path)
num_imgs = len(allfiles) - 1

design_mat = np.zeros([num_imgs, 3072])

for index in range(0, num_imgs):
    design_mat[index, :] = scipy.misc.imread('%s/test/%s.png' % (data_path, index + 1)).flatten()


d1 = {'data': design_mat[0: 100000, :]}
sio.savemat(data_path + 'test1.mat', d1)

d2 = {'data': design_mat[100000: 200000, :]}
sio.savemat(data_path + 'test2.mat', d2)

d3 = {'data': design_mat[200000: 300000, :]}
sio.savemat(data_path + 'test3.mat', d3)

