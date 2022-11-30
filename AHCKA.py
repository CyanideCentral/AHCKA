import config
import numpy as np
import scipy.sparse as sp
from sklearn.preprocessing import normalize
from data import data
import argparse
from sklearn.preprocessing import normalize
import random
from cluster import cluster


p = argparse.ArgumentParser(description='Set parameter')
p.add_argument('--data', type=str, default='coauthorship', help='data type (coauthorship/cocitation)')
p.add_argument('--dataset', type=str, default='cora', help='dataset name (e.g.: cora/dblp for coauthorship, cora/citeseer for cocitation)')
p.add_argument('--tmax', type=int, default=200, help='t_max parameter')
p.add_argument('--seeds', type=int, default=0, help='seed for randomness')
p.add_argument('--alpha', type=float, default=0.2, help='mhc parameter')
p.add_argument('--beta', type=float, default=0.5, help='weight of knn random walk')
p.add_argument('--metric', type=bool, default=False, help='calculate additional metrics: modularity')
p.add_argument('--weighted_p', type=int, default=0, help='use transition matrix p weighted by attribute similarity')
p.add_argument('--verbose', action='store_true', help='print verbose logs')
p.add_argument('--scale', action='store_true', help='use configurations for large-scale data')
p.add_argument('--interval', type=int, default=5, help='interval between cluster predictions during orthogonal iterations')

args = p.parse_args()

def run_ahcka():
    dataset = data.load(config.data, config.dataset)
    features = dataset['features_sp']
    labels = dataset['labels']

    labels = np.asarray(np.argmax(labels, axis=1)) if labels.ndim == 2 else labels
    config.labels = labels
    k  = len(np.unique(labels))


    seed = config.seeds
    np.random.seed(seed)
    random.seed(seed)

    hg_adj = dataset['adj_sp']
    config.hg_adj = hg_adj
    config.features = features.copy()
    d_vec = np.asarray(config.hg_adj.sum(0)).flatten()
    deg_dict = {i: d_vec[i] for i in range(len(d_vec))}
    p_mat = (normalize(hg_adj.T, norm='l1', axis=1),  normalize(hg_adj, norm='l1', axis=1))

    results = None
    results = cluster(hg_adj, features, k, deg_dict, alpha=config.alpha, beta=config.beta, tmax=config.tmax, ri=False, weighted_p=config.weighted_p)

    return results

if __name__ == '__main__':
    config.data = args.data
    config.dataset = args.dataset
    config.metric = args.metric
    config.tmax = args.tmax
    config.beta = args.beta
    config.alpha = args.alpha
    config.seeds = args.seeds
    config.verbose = args.verbose
    config.cluster_interval = args.interval
    if args.scale:
        config.approx_knn = True
        config.init_iter = 1

    run_ahcka()
