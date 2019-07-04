#!/usr/bin/env output
# encoding: utf-8
'''
@Author: Joven Chu
@Email: jovenchu03@gmail.com
@File: bert_ner_api.py
@Time: 2019/5/15 15:43
@Project: bert-ner
@About: 使用bert-ner的训练、预测功能。
'''

from bert_ner.bert_base.train.train_helper import get_args_parser
from bert_ner.bert_base.train.bert_lstm_ner import train

def train_api():
    """
    开启训练服务
    :return:
    """
    args = get_args_parser()
    train(args)

def predict_cmd():
    """
    基于命令行的多次预测展示
    :return:
    """
    from src.bert_ner_predict import ner_predict
    while True:
        print('input the test sentence:')
        sentence = str(input())
        if len(sentence) < 2:
            print('句子长度过短！')
            continue
        # 命名实体识别
        # all_list：所有实体列表，ner_list：处理后的实体映射列表，ner_dic：实体字典
        all_list, ner_list, ner_dic = ner_predict(sentence)
        print('entities_list:', all_list)
        print('实体ner_list:', ner_list)


if __name__ == '__main__':
    use_train = False
    # use_train = True
    # 开启训练：
    if use_train:
        train_api()
    # 开启预测：
    else:
        predict_cmd()
