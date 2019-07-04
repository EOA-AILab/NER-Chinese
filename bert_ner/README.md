## 基于BERT的中文命名实体识别框架

1. 项目目录
    ```xml
     bert_ner
      |——bert_ner # 模型与数据文件
	  |   |——bert_base  # bert的训练代码
	  |   |——train  # 主要训练代码
	  |   |——bert_lstm_ner.py  # 训练的主函数代码
	  |   |——train_helper.py  # 参数预设代码
	  |   |——chinese_L-12_H-768_A-12 # bert-base的中文预训练模型
	  |   |——ltp_data_v3.4.0 # pyltp的词性分析、句法分析的模型
	  |   |——NERdata  # 切分后的数据集
	  |   |    |——dev.txt  # 验证集
	  |   |    |——test.txt  # 测试集
	  |   |    |——train.txt  # 训练集
	  |   |——output  # 模型输出
	  |——data_process # 处理训练数据格式
	  |   |——data_IB  # 原始数据集
	  |   |——ner_data  # 处理后的ner格式数据集，在“。"、"？"、"！"后面加入空行
	  |   |——split_data  # 将处理后的数据按7:1:2切分成训练集、验证集、测试集，放入NERdata目录中
	  |   IB_tag.py  # 第一步
	  |   ner_data.py  # 第二步
	  |   split_data.py  # 第三步
	  |——src # 运行调用的脚本
	  |   |——bert_ner_predict.py  # bert-ner预测脚本
	  bert_ner_api.py  # 控制bert-ner训练和测试的主函数脚本
	  README.md # 说明文件
	```
	
2. 框架及模型使用
	* NER模型训练与预测：
      * 模型训练和预测：
          * 修改`bert_ner/bert_ner/bert_base/train/train_helper.py`中的参数和路径
              ```python
            # windows系统下路径
              if os.name == 'nt':
	            		bert_path = r'D:\Workproject\5.15\watson_IE_RE_all\bert_ner\chinese_L-12_H-768_A-12'
	        		root_path = r'D:\Workproject\5.15\watson_IE_RE_all\bert_ner'
	            # mac和Linux系统下路径
	            else:
	        		bert_path = '/home/macan/ml/data/chinese_L-12_H-768_A-12/'
	                root_path = '/home/macan/ml/workspace/BERT-BiLSTM-CRF-NER'
	        ```
          
          
          
          * 在`watson_IE_RE_all/src/bert_ner_api.py`文件中启动训练或预测（关闭训练）
              ```python 
                 if __name__ == '__main__':
                      use_train = False
                      # use_train = True
	                    # 开启训练：
	                    if use_train:
	                      train_api()
	                    # 开启预测：
                      else:
	                      predict_cmd()
	        ```
	
3. 训练数据和模型下载：链接:https://pan.baidu.com/s/1PXhQE5iEecLf0IiRHN52Lw  密码:sx2z


