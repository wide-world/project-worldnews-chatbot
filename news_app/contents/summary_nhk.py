import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import pt_core_news_sm
import os
import sys
import urllib.request

def run():
    nlp = pt_core_news_sm.load()
    read_nhk = open('scrapping/nhkcontent.txt', 'r', encoding = 'utf-8')
    if os.path.exists('summary/nhksummary.txt'):
        os.remove('summary/nhksummary.txt')
    while True :
        text = read_nhk.readline()
        if not text :
            break
        doc = nlp(text)
        corpus = [sent.text.lower() for sent in doc.sents ]
        cv = CountVectorizer(stop_words=list(STOP_WORDS))
        cv_fit=cv.fit_transform(corpus)
        word_list = cv.get_feature_names_out();
        count_list = cv_fit.toarray().sum(axis=0)
        word_frequency = dict(zip(word_list,count_list))
        val=sorted(word_frequency.values())
        higher_word_frequencies = [word for word,freq in word_frequency.items() if freq in val[-3:]]
        higher_frequency = val[-1]
        for word in word_frequency.keys():
            word_frequency[word] = (word_frequency[word]/higher_frequency)
        sentence_rank={}
        for sent in doc.sents:
            for word in sent :
                if word.text.lower() in word_frequency.keys():
                    if sent in sentence_rank.keys():
                        sentence_rank[sent]+=word_frequency[word.text.lower()]
                    else:
                        sentence_rank[sent]=word_frequency[word.text.lower()]
        top_sentences=(sorted(sentence_rank.values())[::-1])
        top_sent=top_sentences[:3]
        summary=[]
        for sent, strength in sentence_rank.items():
            if strength in top_sent:
                summary.append(sent)
                summary.append(' ')
            else:
                continue

        write_nhk = open("summary/nhksummary.txt", "a+")
        for i in summary :
            write_nhk.write(str(i))
        write_nhk.write('\n')
        write_nhk.close()
    read_nhk.close()
