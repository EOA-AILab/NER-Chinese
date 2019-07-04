# -*- coding: utf-8 -*-

"""

 @Time    : 2019/1/30 14:01
 @File    : train_helper.py
"""

import argparse
import os

__all__ = ['get_args_parser']

def get_args_parser():
    __version__ = '0.1.0'
    parser = argparse.ArgumentParser()
    # windows下的路径表示
    if os.name == 'nt':
        bert_path = r'D:\Workproject\bert_ner\bert_ner\chinese_L-12_H-768_A-12'
        root_path = r'D:\Workproject\bert_ner\bert_ner'
    # linux/macos下的路径表示
    else:
        bert_path = '/home/jovenchu/joven/NER/bert_ner/bert_ner/chinese_L-12_H-768_A-12'
        root_path = '/home/jovenchu/joven/NER/bert_ner/bert_ner'

    group1 = parser.add_argument_group('File Paths',
                                       'config the path, checkpoint and filename of a pretrained/fine-tuned BERT model')
    group1.add_argument('-bert_path', type=str, default=bert_path,
                        help='directory of a pretrained BERT ')
    group1.add_argument('-model_path', type=str, default=os.path.join(root_path, 'output'),
                        help='trained BERT model')
    group1.add_argument('-data_dir', type=str, default=os.path.join(root_path, 'NERdata'),
                        help='train, dev and test data dir')
    group1.add_argument('-bert_config_file', type=str, default=os.path.join(bert_path, 'bert_config.json'))
    group1.add_argument('-output_dir', type=str, default=os.path.join(root_path, 'output2'),
                        help='directory of a pretrained BERT model')
    group1.add_argument('-init_checkpoint', type=str, default=os.path.join(bert_path, 'bert_model.ckpt'),
                        help='Initial checkpoint (usually from a pre-trained BERT model).')
    group1.add_argument('-vocab_file', type=str, default=os.path.join(bert_path, 'vocab.txt'),
                        help='')

    group2 = parser.add_argument_group('Model Config', 'config the model params')
    # 减少最大的长度，字向量：128——32
    group2.add_argument('-max_seq_length', type=int, default=128,
                        help='The maximum total input sequence length after WordPiece tokenization.')
    group2.add_argument('-do_train', type=bool, default=True,
                        help='Whether to run training.')
    group2.add_argument('-do_eval', type=bool, default=True,
                        help='Whether to run eval on the dev set.')
    group2.add_argument('-do_predict', type=bool, default=True,
                        help='Whether to run the model in inference mode on the test set.')
    # 减少batch_size：64——16
    group2.add_argument('-batch_size', type=int, default=32,
                        help='Total batch size for training, eval and predict.')
    group2.add_argument('-learning_rate', type=float, default=1e-5,
                        help='The initial learning rate for Adam.')
    group2.add_argument('-num_train_epochs', type=float, default=30,
                        help='Total number of training epochs to perform.')
    # 修改2：减少丢失：0.5——0.2
    group2.add_argument('-dropout_rate', type=float, default=0.5,
                        help='Dropout rate')
    group2.add_argument('-clip', type=float, default=0.5,
                        help='Gradient clip')
    group2.add_argument('-warmup_proportion', type=float, default=0.1,
                        help='Proportion of training to perform linear learning rate warmup for '
                             'E.g., 0.1 = 10% of training.')
    group2.add_argument('-lstm_size', type=int, default=128,
                        help='size of lstm units.')
    group2.add_argument('-num_layers', type=int, default=1,
                        help='number of rnn layers, default is 1.')
    group2.add_argument('-cell', type=str, default='lstm',
                        help='which rnn cell used.')
    group2.add_argument('-save_checkpoints_steps', type=int, default=200,
                        help='save_checkpoints_steps')
    group2.add_argument('-save_summary_steps', type=int, default=200,
                        help='save_summary_steps.')
    group2.add_argument('-filter_adam_var', type=bool, default=False,
                        help='after training do filter Adam params from model and save no Adam params model in file.')
    group2.add_argument('-do_lower_case', type=bool, default=True,
                        help='Whether to lower case the input text.')
    group2.add_argument('-clean', type=bool, default=True)
    group2.add_argument('-device_map', type=str, default='0',
                        help='witch device using to train')

    # add labels
    group2.add_argument('-label_list', type=str, default=None,
                        help='User define labels， can be a file with one label one line or a string using \',\' split')

    parser.add_argument('-verbose', action='store_true', default=False,
                        help='turn on tensorflow logging for debug')
    parser.add_argument('-ner', type=str, default='ner', help='which modle to train')
    parser.add_argument('-version', action='version', version='%(prog)s ' + __version__)
    return parser.parse_args()
