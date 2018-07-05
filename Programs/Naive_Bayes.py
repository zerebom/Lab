import glob
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier



def load_file(yato):
    # yato=Old_yato or new hoge
    category={
    'old_fixed_matubi':1,
    'new_fixed_matubi':2,
    }

    docs=[]
    labels=[]


    
    for c_name,c_id in category.items():
        i=0
        files=glob.glob('../Docments/{}/old_fixed_matubi/*.txt'.format(yato))
        print(files)
        text = ''
        for file in files:
            with open(file, 'r',encoding="utf-8_sig") as f:
                text=f.read()
                print(text)
        docs.append(text)
        print(docs)
        labels.append(c_id)
        i+=1

    return docs, labels


    random.seed()

docs, labels = load_file('Old_yato')  

indices = list(range(len(docs)))
random.shuffle(indices)

train_data   = [docs[i] for i in indices[0:30]]
train_labels = [labels[i] for i in indices[0:30]]
test_data    = [docs[i] for i in indices[30:]]
test_labels  = [labels[i] for i in indices[30:]]

print(train_data)


#ベクトル化する
vectorizer = TfidfVectorizer()
train_matrix = vectorizer.fit_transform(train_data)
test_matrix = vectorizer.transform(test_data)
#ナイブベイズ
clf = MultinomialNB()
clf.fit(train_matrix, train_labels)

print(clf.score(train_matrix, train_labels))
print(clf.score(test_matrix, test_labels))