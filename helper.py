import PyPDF2
import nltk
from os import walk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


def get_all_files(folder_name):
    f =[]
    for (dirpath, dirnames, filenames) in walk(folder_name):
        f.extend(filenames)
    return f

def save_text_file(file_name, file_text):
    f = open(file_name,'w')
    f.write(file_text)
    f.close()

def read_text_file(file_name):
    f = open(file_name,'r')
    file_text = f.read()
    f.close()
    return file_text

# get the text corpus from the files
def get_pdf_corpus(file_name):
    # creating a pdf file object
    pdfFileObj = open(file_name, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    corpus_=''
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        corpus_ +=pageObj.extractText()
    pdfFileObj.close()
    return corpus_


# returnsthe bag of words with counts, list of cleaned sentences
def get_dict_words(corpus_):
    stopword=set(stopwords.words('english'))
    updated_sentences=[]   # array of words per sentence
    updated_corpus_all={}  # all bag of words with counts
    for i in sent_tokenize(corpus_):
        #print(word_tokenize(i))
        updated_corpus={}  # bag of words per sentence
        for j in word_tokenize(i):
            if j not in stopword:
                if j in updated_corpus:
                    updated_corpus[j] += 1
                else:
                    updated_corpus[j] = 1
        updated_sentences.append(updated_corpus.keys()) # append new list of words
        updated_corpus_all.update(updated_corpus) # append current sentence bag of words to our final dict

    return updated_corpus_all, updated_sentences # return both dict of words, count and new updated sentences


# print sorted list of key words based on the count of words
def print_sorted_dict_byval(dict_):
    for key, value in sorted(dict_.iteritems(), key=lambda (k,v): (-v,k)):
        print(key, value)
