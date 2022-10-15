import os, pickle
import numpy as np, scipy.sparse as sp
import pickle

import config


def load(data, dataset):

    if data == 'npz':
        data_dict = load_npz(dataset)
    else:
        ps = parser(data, dataset)

        with open(os.path.join(ps.d, 'hypergraph.pickle'), 'rb') as handle:
            hypergraph = pickle.load(handle)

        with open(os.path.join(ps.d, 'features.pickle'), 'rb') as handle:
            features = pickle.load(handle)

        with open(os.path.join(ps.d, 'labels.pickle'), 'rb') as handle:
            labels = ps._1hot(pickle.load(handle))

        adj = np.zeros((len(hypergraph), features.shape[0]))
        for index, edge in enumerate(hypergraph):
            hypergraph[edge] = list(hypergraph[edge])
            adj[index, hypergraph[edge]] = 1
        if config.remove_unconnected:
            nonzeros = adj.sum(0).nonzero()[0]
            adj = adj[:, nonzeros]
            features = features[nonzeros, :]
            labels = labels[nonzeros, :]
            pairs = adj.nonzero()
            hypergraph = {}
            for index, edge in enumerate(pairs[0]):
                if edge not in hypergraph:
                    hypergraph[edge]=[]
                hypergraph[edge].append(pairs[1][index])
        adj_sp = sp.csr_matrix(adj)
        data_dict = {'features': features.todense(), 'features_sp':features, 'labels': labels, 'n': features.shape[0], 'e': len(hypergraph), 'name': dataset, 'adj': adj, 'adj_sp': adj_sp}
    return data_dict

def load_npz(dataset):
    hg_adj = sp.load_npz(f'data/npz/{dataset}/hypergraph.npz')
    np.clip(hg_adj.data, 0, 1, out=hg_adj.data)
    features = sp.load_npz(f'data/npz/{dataset}/features.npz')
    labels = np.load(f'data/npz/{dataset}/labels.npy')
    return {'features_sp': features, 'labels': labels, 'n': features.shape[0], 'e': hg_adj.shape[0], 'name': dataset, 'adj': hg_adj, 'adj_sp': hg_adj}

class parser(object):

    def __init__(self, data, dataset):

        import inspect
        current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.d = os.path.join(current, data, dataset)
        self.data, self.dataset = data, dataset

    

    def parse(self):
        name = "_load_data"
        function = getattr(self, name, lambda: {})
        return function()



    def _load_data(self):

        with open(os.path.join(self.d, 'hypergraph.pickle'), 'rb') as handle:
            hypergraph = pickle.load(handle)

        with open(os.path.join(self.d, 'features.pickle'), 'rb') as handle:
            features = pickle.load(handle).todense()

        with open(os.path.join(self.d, 'labels.pickle'), 'rb') as handle:
            labels = self._1hot(pickle.load(handle))

        return {'hypergraph': hypergraph, 'features': features, 'labels': labels, 'n': features.shape[0]}



    def _1hot(self, labels):
        classes = set(labels)
        onehot = {c: np.identity(len(classes))[i, :] for i, c in enumerate(classes)}
        return np.array(list(map(onehot.get, labels)), dtype=np.int32)