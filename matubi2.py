 #coding: utf-8
import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import urllib3
import pandas as pd
import xlsxwriter
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from func import *

#このコードは普通の、全議員文のめかぶtxtファイルを読み込んだ上、
# 読点以下の文字だけをファイルにめかぶ形式でなく普通の形式にかきこむコードである
# このあと、読点以下のtxtファイルを形態素解析し、前４単語をあれする
#matubi_copusとともに使う

size = 100000


# 形態素解析
# to_mecab('./old_speech.txt','./old_speech.mecab')
# to_mecab('./new_speech.txt','./new_speech.mecab')
#to_mecab('/home/share/Lab/yoto2011.txt','/home/share/Lab/yoto2011.txt.mecab')
#txtファイルからリストを作成
def make_lines2(fname_parsed):#ジェネレーター

    with open(fname_parsed,encoding='utf-8_sig') as file_parsed:

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
                print(morphemes)
                yield morphemes
                morphemes = []

def matubi_morpheme(write_file,mecab_file):
    #語数カウンター
    word=""
    for morphemes in make_lines2(mecab_file):
        # print(morphemes
        # print('A')
        morphemes=''.join(morphemes)
        morphemes=morphemes.split("、")
        # print(morphemes)
        # print('B')
        morphemes=morphemes[-1]
        # print(morphemes)
        # print('C')
        word+=morphemes
    with open(write_file, mode='w',errors='ignore') as out_file:
        out_file.write(word)

matubi_morpheme('./new_speech_matsubi.mecab','./new_speech.mecab')
matubi_morpheme('./old_speech_matsubi.mecab','./old_speech.mecab')
