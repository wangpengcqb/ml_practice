import random
import copy

X = [[1,2,3],[4,5,6],[1,3,4],[2,7,8],[9,5,10],[0,0,1],[4,7,9],[3,3,6],[4,2,1],[1,5,9],[7,7,8],[8,3,9],[16,5,2],[10,10,1],[0,9,7]]
K = 4

m, n = len(X), len(X[0])
temp = [0]*n

for i in range(m):
    for j in range(n):
        temp[j] += X[i][j]

mean = [i/m for i in temp]

temp = [0]*n
for i in range(m):
    for j in range(n):
        temp[j] += (X[i][j] - mean[j])**2
        
std = [(i/(m-1))**(0.5) for i in temp]

Xb = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        Xb[i][j] = (X[i][j] - mean[j])/(std[j]+0.01)

idx = list(range(m))
# random_indices = random.shuffle(idx)
# idx = idx[:K]
idx = random.sample(idx, K) 
centers = []
for i in idx:
    centers.append(Xb[i])

# centers = []
# for i in range(K):
#     center = []
#     for j in range(n):
#         center.append(std[j]*random.random()+mean[j])
#     centers.append(center)
    
distances = [[0]*K for _ in range(m)]
clusters = [-1]*m

max_iterations = 10
tolerance = 1e-6

def dis(a1, a2):
    temp = [i-j for i in a1 for j in a2]
    return sum(i**2 for i in temp)**(0.5)
    

for _ in range(max_iterations):
    centers_old = copy.deepcopy(centers)
    
    for i in range(m):
        min_dis = float('inf')
        for j in range(K):
            distances[i][j] = dis(Xb[i], centers[j])
            if distances[i][j] < min_dis:
                min_dis = distances[i][j]
                clusters[i] = j
    
              
    for j in range(K):
        temp = [0]*n
        cnt = 0
        for i in range(m):
            if clusters[i] == j:
                for k in range(n):
                    temp[k] += Xb[i][k]
                cnt += 1
        
        if cnt == 0:
            centers[j] = centers_old[j]
        else:
            centers[j] = [val/cnt for val in temp]
    
    loss = 0        
    for i in range(m):
        loss += dis(Xb[i], centers[clusters[i]])
    loss /= m
    print('loss is {0}'.format(loss))
    
    center_change = 0
    for j in range(K):
        center_change += dis(centers[j], centers_old[j])
    print('center change is {0}'.format(center_change))