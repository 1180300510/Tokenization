## 文件格式说明

首先需要说明的是分词结果中的格式

19980101-01-001-001/ 迈向/ 充满/ 希望/ 的/ 新/ 世纪/ ——/ 一/ 九九/ 八年/ 新年/ 讲话/ （/ 附/ 图片/ １张/ ）/ 

也就是每个词之后有一个/加一个空格，最后一个词也有

### 主文件夹为Lab1

包含两个文件和五个文件夹

其中两个文件为**199801_seg&pos.txt和199801_sent.txt**，这两个文件为实验的训练语料库和未分词的测试数据

#### dict-divide

该文件夹包含了3.1-3.4的内容

creat-dict.py：3.1创建词典的代码

match.py：3.2正反向最大匹配的代码，如果运行过满，可以使用match_length.py进行测试

match_length.py：第一个速度优化代码

match_trie.py：trie树实现的速度优化代码

trie.py：trie树的类

Effect_analy.py：性能分析

dic.txt：3.1生成的词典

seg_FMM.txt：正向最大匹配的结果

seg_BMM.txt：逆向最大匹配的结果

score.txt：精确率，召回率，F1值的输出结果文件

TimeCost.txt：优化前和优化后的时间文件

#### dic-test

该文件夹包含两个文件夹：8-2,9-1，表示使用正反向最大匹配进行开放测试，分别以8:2和9:1划分训练集和测试集

这两个文件中的代码文件和文本文件大致和dict-divide中相同

#### Ui-gram

该文件夹是一元语言模型的实现

uigram-train.py：根据输入训练语料库获取词频的代码

uigram.py：一元模型，viterbi算法实现代码

Effect.py：分词性能分析代码

test.txt：测试集，在这里就是199801_sent.txt的拷贝，老师测试的时候可以替代

singer.txt：存储了词频对应的对数概率值

seg_LM.txt：一元模型的分词结果

score.txt：一元模型分词结果的评价指标输出文件

#### Uigram-test

按照9:1划分训练测试集使用一元语言模型进行开放测试的文件，文件与Ui-gram相仿

#### HMM

HMM-train.py:HMM模型参数训练

bi-gram-HMM.py:HMM实现

Effect.py：评价指标代码

Initial.txt：初始矩阵

Lanuch.txt：发射概率矩阵

transfer.txt：状态转移矩阵

test.txt：测试文件

seg_LM.txt：HMM分词结果

score.txt：HMM分词结果评价指标输出文件


