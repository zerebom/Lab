def new_mecab(fname,fname_parsed):
    Matubi=[]
    with open(fname,errors='ignore',encoding='utf-8_sig') as data_file, \
            open(fname_parsed, mode='w',errors='ignore') as out_file:
                #空白文字を削除する
                text_data=data_file.read()
                text_data=re.sub('.+　','',text_data)
                #改行で区切る
                text_data=re.sub('\n','',text_data)
                #句点で区切り、最後の要素を抜き取る
                text_data=text_data.split('。')
                for i,text in enumerate(text_data):
                    #読点以前を削除する
                    text=text.split('、')
                    #なぜか先頭に空白文字が入るので取り除く↓。
                    text[0]=text[0].lstrip()
#                     print(text[0])
#                     print('======tex↑=======--')    
#                     print(i)
#                     print(text)
#                     print('======text↑=======--')
#                     print(text[-1])
#                     print('======text[-1]↑=======--')
#                     print()
                    #読点以降のみが集まる↓
                    Matubi.append(text[-1])
#                 print(morphemes)    
#                     mecab = MeCab.Tagger(r'-d C:\Users\icech\mecab-ipadic-neologd\build\mecab-ipadic-2.7.0-20070801-neologd-20180625')
#                     mecab_data=mecab.parse(text[-1])
#                     print(mecab_data)
                abc=[]
                for morpheme in Matubi:
                    mecab = MeCab.Tagger(r'-d C:\Users\icech\mecab-ipadic-neologd\build\mecab-ipadic-2.7.0-20070801-neologd-20180625')
                    mecab_data=mecab.parse(morpheme)
                    print('morpheme↓')
                    print(morpheme)
#                     print(mecab_data)
                    cols=mecab_data.split('\n')
#                     for col in cols:
#                         co=col.split('\t')
#                         print('co↓')
#                         if(len(co)<2):
#                             print('abc↓')    
#                             print(abc)
#                             yield abc
#                         print(co[0])
#                         abc.append(co[0])
#                     if(len(cols)<2):
#                         raise StopIteration
#                     print(cols)
#                 print(abc)
# #                 mecab_data= re.sub('　.+.','',mecab_data)
#                 print(len(mecab_data))
#                 print(mecab_data)
#                 mecab_data=mecab_data.split('\n')
            
#     ----------------------------------------
#     for line in mecab_data:
#         cols = line.split('\t')
#         print(cols[0])
#         if(len(cols) < 2):
#             raise StopIteration
#         morphemes.append(cols[0])
#         if cols[0]=='。':
#             print(morphemes)
#             yield morphemes
#             morphemes = []


# #         print(mecab_data)
                    
                
def make_lines2(fname_parsed):#ジェネレーター
    with open(fname_parsed) as file_parsed:       

        morphemes = []
   
        for line in file_parsed:          
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration     
            
            res_cols = cols[1].split(',')

    
            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':

                # morphemes.append(cols[0])
                # ↑これがあると。が二つになってしまう
                yield morphemes
                # print(morphemes)
                morphemes = []
                