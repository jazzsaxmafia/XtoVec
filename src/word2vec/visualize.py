import os
import sys
sys.path.insert(0, '/home/taeksoo/Package/tsne_python')

from tsne import tsne

import pandas as pd
import numpy as np
word2vec_vectors = pd.read_pickle('../../data/word2vec_vectors.pickle')

sampled_word2vec_vectors = word2vec_vectors.ix[ np.random.permutation(len(word2vec_vectors))[:10000]]
tsne_vecs = tsne( X=np.stack( sampled_word2vec_vectors['vector'].values ), initial_dims=200 )
word2vec_vectors['tsne'] = tsne_vecs.tolist()
