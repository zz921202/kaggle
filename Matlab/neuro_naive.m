load data_sbatch_1.mat
% load train.mat
% load label.mat

inputs = data;%data_x
inputs = double(inputs');


for iter = 1: 9
    if iter== 1
        target = (labels == iter); %label_x
    end
    target = [target, (labels == iter)];
end
targets = target';

hiddenLayerSize = [ 200, 60, 40, 40, 25];
net = patternnet(hiddenLayerSize);

net.divideParam.trainRatio = 0.7;
net.divideParam.valRatio = 0.15;
net.divideParam.testRatio = 0.15;

[net,tr] = train(net, inputs, targets);

outputs = net(inputs);
errors = gsubtract(targets,outputs);
performance = perform(net,targets,outputs);

% View the Network
view(net)
