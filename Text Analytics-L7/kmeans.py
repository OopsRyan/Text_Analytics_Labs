#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0], points1[1], 'ro')
    points2 = change_coords(clusters[1])
    plt.plot(points2[0], points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1], 'kx')
    plt.axis([-1.0, 1, -1.0, 1])
    # plt.axis([0, 15, 0, 150])
    plt.show()
    return centroids


# ********* question_1 *********
data = init_board(15)
data = [[-0.90984662, 0.7490675], [-0.28534063, -0.35868282], [-0.51243724, 0.5167752 ], [ 0.82104191, 0.00880982], [-0.51297971, -0.17132431],
        [-0.71296446, -0.51679771], [-0.75158251, 0.9723092], [-0.44642651, 0.02573734], [ 0.85981944, 0.59843169], [-0.7900795, -0.38639262],
        [-0.86015581, 0.07643797], [-0.53006354, -0.00498541], [ 0.29847866, 0.90584279], [ 0.12119778, -0.07323537], [0.54534747, -0.20246888]]
data = np.array(data)
out = find_centers(list(data), 3)
centroids_result = parse_output(out)
print(centroids_result)
# ****************************

# *** question 2 ***
# x = [0.5, 1, 1.5, 1.8, 2.2, 6, 6.23, 6.67, 6.5, 6.82, 10, 10.25, 10.11, 10.5, 10.34]
# y = list(map(lambda x: x**2+1, x))
# data = list()
# for i in range(len(x)):
#     data.append(x[i])
#     data.append(y[i])
#
# data = np.array(data).reshape(-1, 2)
# out = find_centers(list(data), 3)
#
# centroids_result = parse_output(out)
# print(centroids_result)

