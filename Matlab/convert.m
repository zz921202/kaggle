function greyX = convert(X)
% convert RGB design matrix to grey scale matrix
R = X(:, 1: 1024);
G = X(:, 1025: 2048);
B = X(:, 2049: 3072);
greyX = 0.2989 * R + 0.5870 * G + 0.1140 * B ;
end



