# coding: utf-8
import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import slothLib
import urllib3
import pandas as pd
import xlsxwriter
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def to_mecab(fname,fname_parsed):
    with open(fname,errors='ignore') as data_file, \
            open(fname_parsed, mode='w',errors='ignore') as out_file:

        mecab = MeCab.Tagger('-d /var/lib/mecab/dic/mecab-ipadic-neologd')
        out_file.write(mecab.parse(data_file.read()))


def make_lines(fname_parsed):#ジェネレーター

    with open(fname_parsed) as file_parsed:

        morphemes = []
        for line in file_parsed:

            # 表層形はtab区切り、それ以外は','区切りでバラす
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration     # 区切りがなければ終了
            res_cols = cols[1].split(',')

            # 辞書作成、リストに追加
            '''
            morpheme = {
                'surface': cols[0],
                #'base': res_cols[6],
                #'pos': res_cols[0],
                #'pos1': res_cols[1]
            }
            '''
            morphemes.append(cols[0])

            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':
                morphemes.append(cols[0])
                yield morphemes
                morphemes = []
size = 100000
stop_word=slothLib.sloth()


# 形態素解析
to_mecab('./new_speech_matsubi.txt','./new_speech_matsubi.mecab')
to_mecab('./old_speech_matsubi.txt','./old_speech_matsubi.mecab')
#to_mecab('/home/share/Lab/yoto2011.txt','/home/share/Lab/yoto2011.txt.mecab')
#txtファイルからリストを作成

def count_morpheme2(mecab_file):

    copus=[]
    #語数カウンター
    word_counter = Counter()
    for morphemes in make_lines(mecab_file):
        if len(morphemes)>=6:
            copus.append(morphemes[-6]+morphemes[-5]+morphemes[-4]+morphemes[-3])
        elif len(morphemes)>=5:
            copus.append(morphemes[-5]+morphemes[-4]+morphemes[-3])
            # print(copus)
            # print(3)
        elif len(morphemes)>=4:
            # print(morphemes)
            copus.append(morphemes[-4]+morphemes[-3])
            # print(copus)
            # print(2)
        elif len(morphemes)>=3:
            copus.append(morphemes[-3])
            # print(copus)
            # print(1)

    copus=''.join(str(copus))
    print(copus)
    return(copus)


a=count_morpheme2('./old_speech_matsubi.mecab')
b=count_morpheme2('./new_speech_matsubi.mecab')

count=CountVectorizer()

#べくトルになおしている
docs=np.array([a,b])
bag=count.fit_transform(docs)
features = count.get_feature_names()
print('aaaaaaaaaaaaaaaaaaaaaaaa')
bag_array=bag.toarray()
# bag_array[1]=np.round(bag_array[1]*(sum(bag_array[0])/sum(bag_array[1])))


#def to_excel(output_pass):

data={
"index":features,
"zimin_yato":bag_array[0],
"minsyu_yato":bag_array[1],
"sum":bag_array[0]+bag_array[1]}
df=pd.DataFrame(data)
df=df.sort_values(by='sum',ascending=False)
print(df)
#print(data)
df.to_excel('./true_matubi.xlsx')#←ハイパーパラメーッタ

sum2016=sum(bag_array[0])
sum2011=sum(bag_array[1])

print(sum2016)
print(sum2011)
