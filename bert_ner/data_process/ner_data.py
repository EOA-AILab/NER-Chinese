# encoding: utf-8
'''
@author: joven chu
@contact: jovenchu03@gmail.com
@time: 2017/11/30 21:11

3.处理评论命名实体识别的样式为ner样式
'''

# 1.评论命名实体识别.txt:把tab键转换成空格
import re
f = open('data_IB/trains.txt','r',encoding='utf-8')
f2 = open ('ner_data/total_ner_corpus.txt','w',encoding='utf-8')
lines = f.readlines()
for line in lines:
    new_spaces = re.sub(r'\t',' ',line)
    new_spacess = re.sub(r'ul', '', new_spaces)
    new_space = re.sub(r'  ', ' ', new_spacess)
    f2.write(new_space)
f2.close()
print('成功将数据集txt:把tab键转换成空格！')

# 2.添加分隔符(每个30行加一次)
f = open('ner_data/total_ner_corpus.txt','r',encoding='utf-8')
f2 = open('ner_data/total_ner2.txt','w',encoding='utf-8')
tag_list = ['。','！','？','；']
for line in f:
    f2.write(line)
    line_sps = line.strip().split(' ')
    if line_sps[0] in tag_list:
        line_sp = line.strip().split(' ')
        if len(line_sp) == 2:
            if line_sp[1] == 'O':
                f2.write('\n')
                line_num = 0
        else:
                f2.write('\n')
                line_num = 0
print('成功添加分隔符！')

# # 3.去掉多余的空行（如果最后一行是空行，并且上一行的标签是以I-结束的，就要去掉这个空行）
#
# f_r = open('ner_data/total_ner2.txt','r',encoding='utf-8')
# f_w = open('ner_data/total_ner3.txt','w',encoding='utf-8')
# previous_token_label = 'O'
# count = 0
# for line in f_r:
#     count += 1
#     #if count > 500:
#         #break
#     if line.find('-DOCSTART-' ) != -1:
#         f_w.write(line)
#         continue
#
#     line_sp = line.strip().split(' ')
#     if len(line_sp) <= 2 and previous_token_label == "O":
#         f_w.write(line)
#     elif len(line_sp) == 3:
#         f_w.write(line)
#         if line_sp[2] != "O":
#             previous_token_label = line_sp[2][:2]
#             #print("label %s" % previous_token_label)
#         else:
#             previous_token_label = "O"
#     else:
#         print(len(line_sp))
#         print("%d error %s" % (count, line))
#
# f_r.close()
# f_w.close()
# print("完成去掉多余的空行操作！")
#
# print("处理完成！")
