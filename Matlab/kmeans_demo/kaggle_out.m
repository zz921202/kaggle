%% Load CIFAR test data, predict result 

CIFAR_DIR='/Users/Zhe/Documents/Kaggle_Project_Matlab/Matlab';
data_path = '/Users/Zhe/Documents/Kaggle_Project_Matlab/test_data/';
to_dir_file = '/Users/Zhe/Documents/Kaggle_Project_Matlab/python/test_out.mat';
% fprintf('Loading test data...\n'); % change 300k images to desired format 32x32x3
% labels = [];
for curfile = 2:3
    fh=load([data_path '/test' num2str(curfile) '.mat']);
    % f20=load([data_path '/test2.mat']);
    % f30=load([data_path '/test3.mat']);
    testX = double([fh.data]);
    clear fh;

    if (whitening)
      testXC = extract_features(testX, centroids, rfSize, CIFAR_DIM, M,P);
    else
      testXC = extract_features(testX, centroids, rfSize, CIFAR_DIM);
    end
    testXCs = bsxfun(@rdivide, bsxfun(@minus, testXC, trainXC_mean), trainXC_sd);
    testXCs = [testXCs, ones(size(testXCs,1),1)];

    % test and print result
    [val,curlabels] = max(testXCs*theta, [], 2);
    labels = [labels' curlabels']';
end
save(to_dir_file,'labels')