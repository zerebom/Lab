import glob
import random

category={
    'old_fixed_matubi':1,
    'new_fixed_matubi':2,
}

docs=[]
labels=[]

def load_file():
    for c_name,c_id in category.items():
        i=0
        files=glob.glob('./{}/{}_{}.txt'.format(c_name,i,c_name))
        text = ''
        for file in files:
            with open(file, 'r',encoding="utf-8_sig") as f:
                text=f.read()
        docs.append(text)
        print(docs)
        labels.append(c_id)
        i+=1

    return docs, labels


    random.seed()

docs, labels = load_file()  

indices = list(range(len(docs)))
random.shuffle(indices)

train_data   = [docs[i] for i in indices[0:30]]
train_labels = [labels[i] for i in indices[0:30]]
test_data    = [docs[i] for i in indices[30:]]
test_labels  = [labels[i] for i in indices[30:]]

print(train_data)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

#ベクトル化する
vectorizer = TfidfVectorizer()
train_matrix = vectorizer.fit_transform(train_data)
#ナイブベイズ
clf = MultinomialNB()
clf.fit(train_matrix, train_labels)

print(clf.score(train_matrix, train_labels))
print(clf.score(test_matrix, test_labels))