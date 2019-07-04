# NER-Chinese
Comparison of Chinese Named Entity Recognition Models between NeuroNER and BertNER



1. Word Embedding-BiLSTM-CRF：众多实验表明，该结构属于命名实体识别中最主流的模型，代表的工具有：[**NeuroNER**](https://github.com/Franck-Dernoncourt/NeuroNER)。它主要由Embedding层（主要有词向量，字向量以及一些额外特征）、双向LSTM层、以及最后的CRF层构成。
2. Bert-BiLSTM-CRF：随着Bert语言模型在NLP领域横扫了11项任务的最优结果，将其在中文命名实体识别中Fine-tune必然成为趋势。它主要是使用bert模型替换了原来网络的word2vec部分，从而构成Embedding层，同样使用双向LSTM层以及最后的CRF层来完成序列预测。

