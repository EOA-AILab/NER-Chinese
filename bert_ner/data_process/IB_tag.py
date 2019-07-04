# encoding: utf-8
'''
@author: jovenchu
@contact: jovenchu03@gmail.com
@time: 2017/11/30 10:10
2.负责将十万的文本段语料，用IOB标注法标注出与商品相关无关的文本边界
'''
import csv
import jieba
import jieba.posseg as pseg

with open('data_IB/all2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    column1 = [row for row in reader]
content = [i[0] for i in column1]  # 第一列为文本内容
label = [i[1] for i in column1]  # 第二列为标签
len = len(column1)
result = ''
# print(content[0])
# print(label[0])
# print(len-1)
for k in range(0,len):
    count = 0
    string = content[k].replace('\ufeff','')
    # location = jieba.tokenize(content[k])
    words = pseg.cut(string)  # 结巴分词
    if label[k] == str(1):  # 判断评论与商品相关（标rel）和无关（标irr）
        mark = 'rel'
    else:
        mark = 'irr'
    # print(k)
    # print(mark)
    for w in words:  # 按照词在句子中的位置进行标注
        count += 1
        if count ==1:
            marks = 'B-' + mark
            result += str(w.word) + "\t" + str(w.flag) + "\t" + marks +"\n"
        else:
            marks = 'I-' + mark
            result += str(w.word) + "\t" + str(w.flag) + "\t" + marks + "\n"
    result +="，" + "\t" + "wd" + "\t" + "O" + "\n"
    result +="\n"
f = open('data_IB/评论命名实体识别.txt', 'w', encoding='utf-8')  # 将结果保存到另一个文档中
f.write(result)
f.close()
print('标注完成！')