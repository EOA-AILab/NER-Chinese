# encoding: utf-8
'''
@author: joven chu
@contact: jovenchu03@gmail.com
@time: 2017/11/30 22:10

4.自动化切割ner的total_ner2.txt数据为train，test，valid数据集，按行切割
'''

print('\n')
print('开始切割ner的total_ner2.txt数据：')
# f_path = 'ner_data/2/test' + str(k) + '.txt'
f_path = 'ner_data/total_ner2.txt'
train_path = 'split_data/train.txt'
valid_path = 'split_data/dev.txt'
test_path = 'split_data/test.txt'
f = open(f_path,'r',encoding='utf-8')
f1 = open(f_path, 'r', encoding='utf-8')
f_train = open(train_path,'w',encoding='utf-8')
f_valid = open(valid_path, 'w', encoding='utf-8')
f_test = open(test_path, 'w', encoding='utf-8')
line_num = 0
for line in f:
    line_num += 1
print(line_num)
train_num = int(line_num * 0.7)
# train_num = int(line_num * 0.8)  # 训练集为8：1：1时使用该句
print(train_num)
valid_num = int(line_num * 0.1)
print(valid_num)
# test_num =
count_num = 0
count_1 = 0
for line_train in f1:
    count_num += 1
    if count_num <= train_num :
        # count_1 +=1
        f_train.write(line_train)
    else:
        line_sp = line_train.strip().split(' ')
        if len(line_sp) == 3:
                f_train.write(line_train)
        else:
            break
for line_valid in f1:
    count_1 += 1
    if count_1 <= valid_num :
        # count_1 +=1
        f_valid.write(line_valid)
    else:
        line_sp = line_valid.strip().split(' ')
        if len(line_sp) == 3:
            f_valid.write(line_valid)
        else:
            break
for line_test in f1:
    f_test.write(line_test)
print('切割完成！')