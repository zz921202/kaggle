load test2
load test3
[M, I_1] = max(net(double(test_x_1')));
I_1 = I_1';
[M, I_2] = max(net(double(test_x_2')));
I_2 = I_2';
[M, I_3] = max(net(double(test_x_3')));
I_3 = I_3';