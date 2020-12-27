import numpy as np
import random
import copy

X = [[1,2,3],[4,5,6],[1,3,4],[2,7,8],[9,5,10],[0,0,1],[4,7,9],[3,3,6],[4,2,1],[1,5,9],[7,7,8],[8,3,9],[16,5,2],[10,10,1],[0,9,7]]
X = np.array(X)
K = 2
m, n = X.shape[0], X.shape[1]
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
Xb = (X - mean[np.newaxis, :])/(std[np.newaxis, :]+0.01)

random_indices = np.random.choice(m, K, replace=False)
centers = Xb[random_indices, :]

idx = np.zeros(m)
distances = np.zeros((m,K))


max_iterations = 10
tolerance = 1e-6

for _ in range(max_iterations):
    centers_old = copy.deepcopy(centers)
    
    for i in range(K):
        distances[:, i] = np.linalg.norm(X - centers[i, :], axis=1)
    clusters = np.argmin(distances, axis = 1)
    
    
    for i in range(K):
        sample = Xb[clusters==i]
        if sample.size == 0:
            centers[i, :] = np.zeros(n)
        else:
            centers[i, :] = np.mean(Xb[clusters==i], axis=0)
    
    loss = np.mean(np.linalg.norm(Xb - centers[clusters], axis=1))   
    print('loss is {0}'.format(loss))
    
    center_change = np.sum(np.linalg.norm(centers - centers_old, axis=1))
    print('center change is {0}'.format(center_change))