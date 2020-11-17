import collections
import json
import time
from typing import Dict, List, Tuple

import streamlit as st
import textacy
from fastcore.utils import Path
from textacy.spacier.doc_extensions import get_preview, get_tokens
from collections import Counter
import spacy
st.title("s1explorer.com")
st.subheader("Exploring S1 documents with NLP tools")

import io
st.set_option("deprecation.showfileUploaderEncoding", False)

with st.sidebar.beta_expander("Credits"):
    st.markdown("Created by [Nirant](https://nirantk.com) | Twitter: [@NirantK](https://twitter.com/NirantK).\n Contact for Enterprise and Custom Versions of this for your documents"
    )

with st.sidebar.beta_expander("Coming up Next"):
    st.markdown("Tweet to [NirantK](https://twitter.com/NirantK) for which S1 you want to see here next")

## Frequency Calculation

@st.cache
def get_text(filepath:str):
    with Path(filepath).open("r") as f:
        plaintext = f.read()
    return plaintext

def get_spacy_doc(filepath: str):
    plaintext = get_text(filepath)    
    nlp = spacy.load("en_core_web_sm")    
    nlp.max_length = 1.1*1341865 # allow greater memory consumption
    print("Loaded NLP object")
    doc = nlp(plaintext)
    return doc

doc = get_spacy_doc("airbnb.txt")

# all tokens that arent stop words or punctuations
words = [token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_digit]

# noun tokens that arent stop words or punctuations
nouns = [
    token.text
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_digit and token.pos_ == "NOUN"
]
k = st.number_input("Number of Common Words, Phrases, Nouns you want to see. Smaller is faster.", min_value=2, step=1, value=6)
# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(k)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(k)

noun_counter = [{"word": k, "count": v} for (k, v) in common_nouns]
word_counter = [{"word": k, "count": v} for (k, v) in common_words]
st.bar_chart(noun_counter)
st.bar_chart(word_counter)
# ngrams = list(textacy.extract.ngrams(doc, 2, min_freq=2))

# custom_stop_words = ["$", "\n", "common", "Class", "2020", "2019", "million", "shares", "Company", "business"]
# for word in custom_stop_words:
#     nlp.Defaults.stop_words.add(word)


# if st.sidebar.checkbox("Ignore Case (Recommended)", value=True):
#     freq_dict: Dict = corpus.word_counts(
#         as_strings=True, normalize="lower", filter_nums=True, filter_punct=True
#     )
# else:
#     freq_dict: Dict = corpus.word_counts(
#         as_strings=True, filter_nums=True, filter_punct=True
#     )

# freq_dict = {
#     k: v
#     for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
#     if v >= 2
# }

# min_freq_count = st.sidebar.slider(
#     "What is the minimum frequency of words you want to see?",
#     value=int(freq_df[index_key].quantile(0.81)),
#     min_value=2,
#     max_value=int(freq_df[index_key].quantile(0.999)),
# )
# freq_df = freq_df[freq_df[index_key] > min_freq_count]
# left, right = st.beta_columns([2, 1])
# left.bar_chart(freq_df)
# word_display_count = min(20, len(freq_df))
# right.markdown(f"Top {word_display_count} words by frequency")
# right.table(freq_df[:word_display_count])