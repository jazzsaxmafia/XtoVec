import pandas as pd
import numpy as np
import tensorflow as tf
from bs4 import BeautifulSoup
import ipdb

from konlpy.tag import Mecab

from gensim.models import Word2Vec

mecab = Mecab()

learning_rate = 0.001
dim_embed = 200
n_epochs = 20
window_size = 5
min_count = 3

wiki_file = '../text/wiki_all'
with open( wiki_file ) as f:
    wiki_contents = f.read()
    wiki_docs = map(lambda x: filter(lambda y: y != '', x.text.split('\n')), BeautifulSoup( wiki_contents ).find_all('doc'))
    wiki_paragraphs = [item for sublist in wiki_docs for item in sublist]

paragraph_list = []
for wiki_paragraph in wiki_paragraphs:
    wiki_paragraph_pos = map(lambda x: x[0] + '^/'+ x[1], mecab.pos( wiki_paragraph ))
    if len(wiki_paragraph_pos) > 2:
        paragraph_list.append( wiki_paragraph_pos )

del wiki_paragraphs
word2vec_model = Word2Vec( size=dim_embed, alpha=learning_rate, min_count=min_count, workers=-1 )
word2vec_model.build_vocab( paragraph_list )

for epoch in range( n_epochs ):
    print "Training Epoch:", epoch
    word2vec_model.train( paragraph_list )
    word2vec_model.alpha *= 0.99

word2vec_model.save('../../models/word2vec')

