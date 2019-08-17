# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..'))
	print(os.getcwd())
except:
	pass

#%%
import spacy
import json


#%%
# !python -m spacy download en_core_web_lg


#%%
nlp = spacy.load("en_core_web_lg")


#%%
nlp.vocab[u'dog'].cluster


#%%
def most_similar(word):
    queries = [w for w in word.vocab if w.is_lower == word.is_lower and w.prob >= -15]
    by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
    c_val = word.cluster
    words = [(w.lower_, w.cluster, str(word.similarity(w))) for w in by_similarity if abs(w.cluster - c_val)<=180 and word.similarity(w) >= 0.45]
    return words[1:7]


#%%
interesting_words = ["order", "price", "cancel", "refund", "late"]


#%%
for w in interesting_words:
    most_sim_words = most_similar(nlp.vocab[w])
    print(f"Query: {w}", f"\nMost Similar words:{json.dumps(most_sim_words, indent=2)}")
    print("------")


#%%



