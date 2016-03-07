# XtoVec 프로젝트
* 목표: 한국어 텍스트 데이터를 각종 XtoVec 모델들 (word2vec, paragraph2vec, skip-though 등)로 분석

### 전처리
1. http://dumps.wikimedia.org/kowiki/ 에서 kowiki 덤프
2. http://medialab.di.unipi.it/wiki/Wikipedia_Extractor 에서 wikiextractor를 받은 뒤 wiki 데이터 전처리
3. 이후 BeautifulSoup 등을 이용해 각 document의 text를 가져올 수 있음

### Word2Vec 결과
* Gensim의 내장 모델 이용. Learning rate 0.01 기준, 매 epoch마다 0.01씩 낮춤.
* t-SNE 이용해 2차원 공간으로 사상
* Mecab 형태소 분석기를 사용했으며, 동음 단어들을 구분하기 위해 POS 정보를 단어에 추가하였음.
* 장소, 이름, 숫자 등이 비슷한 공간으로 사상됨. 그 외의 텍스트 정보들은 기대보다 잘 사상되지 않은 것으로 보임.
![alt tag](https://github.com/jazzsaxmafia/XtoVec/blob/master/images/word2vec.1)
![alt tag](https://github.com/jazzsaxmafia/XtoVec/blob/master/images/word2vec.2)
![alt tag](https://github.com/jazzsaxmafia/XtoVec/blob/master/images/word2vec.3)
