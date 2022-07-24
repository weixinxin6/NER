#导入需要的包
import pandas as pd
import csv
import jieba
from pprint import pprint
import gensim


sentence = pd.read_csv("love.txt",header=None,quoting = csv.QUOTE_NONE,delimiter="\n") #读取文件，记住取名不要用中文
print(sentence)

sentence.columns = ["内容"]
sentence["内容"] = sentence["内容"].str.replace("\（.*\）","")  #因为括号里有很多作者英文名和年份，去掉这部分的杂树据
sentence = sentence["内容"].tolist() #转换为列表格式

stopwords = pd.read_csv("stop_words_ch.txt",header=None,quoting = csv.QUOTE_NONE,delimiter="\t")
stopwords = stopwords[0].tolist()
stopwords.append("时")  #后面发现还有这几个漏网之鱼，继续加到停用词里去
stopwords.append("一种")
stopwords.append("请")
stopwords.append("●")

sentence_cut = [ " ".join(jieba.lcut(line)) for line in sentence] 
sentence_no_stopwords = [[word for word in line.split() if word not in stopwords] for line in sentence_cut]
from collections import defaultdict
frequency =defaultdict(int)
for line in sentence_no_stopwords:
    for token in line:
        frequency[token] +=1
sentence_morethan1time= [[token for token in line if frequency[token]>3]for line in sentence_no_stopwords]
pprint(sentence_morethan3times) 
