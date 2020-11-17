import collections
import json
import time
from typing import Dict, List, Tuple

import streamlit as st
import textacy
import pandas as pd
from fastcore.utils import Path
from textacy.spacier.doc_extensions import get_preview, get_tokens
from collections import Counter
import spacy

st.set_page_config(
    page_title="S1 Explorer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.title("s1explorer.com")
st.subheader("Exploring S1 documents with NLP tools")

import io

st.set_option("deprecation.showfileUploaderEncoding", False)

with st.sidebar:
    st.markdown(
        "Created by [Nirant](https://nirantk.com) | Twitter: [@NirantK](https://twitter.com/NirantK).\n Contact for Enterprise and Custom Versions of this for your documents"
    )
    st.markdown("Tweet to [NirantK](https://twitter.com/NirantK) for which S1 you want to see here next")

@st.cache
def get_text(filepath: str):
    with Path(filepath).open("r") as f:
        plaintext = f.read()
    return plaintext


def get_nlp_object():
    nlp = spacy.load("en_core_web_sm")
    custom_stop_words = ["$", " ", "\n", "common"]
    custom_stop_words += [
        "Class",
        "2020",
        "2019",
        "million",
        "shares",
        "Company",
        "business",
    ]
    for word in custom_stop_words:
        nlp.Defaults.stop_words.add(word)

    nlp.max_length = 1.1 * 1341865  # allow greater memory consumption
    return nlp


def my_hash_func(spacy_obj: spacy.tokens.doc.Doc):
    return str(spacy_obj)


@st.cache(hash_funcs={spacy.tokens.doc.Doc: my_hash_func})
def get_spacy_doc(filepath: str):
    plaintext = get_text(filepath)
    nlp = get_nlp_object()
    print("Loaded NLP object")
    doc = nlp(plaintext)
    return doc


doc = get_spacy_doc("airbnb.txt")

# all tokens that arent stop words or punctuations
words = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_digit]

# noun tokens that arent stop words or punctuations
nouns = [
    token.text.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_digit and token.pos_ == "NOUN"
]

most_common_count = st.number_input(
    "Number of Common Words, Phrases, Nouns you want to see. Smaller is faster.",
    min_value=2,
    step=1,
    value=5,
)
word_freq = Counter(words)
common_words = word_freq.most_common(most_common_count)

noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(most_common_count)

left, left_center, right_center, right = st.beta_columns([1, 2, 2, 1])

noun_counter = [{"noun": k, "count": v} for (k, v) in common_nouns]
left.dataframe(noun_counter)

word_counter = [{"word": k, "count": v} for (k, v) in common_words]
right.dataframe(word_counter)

ngrams_list = list(textacy.extract.ngrams(doc, 2, min_freq=2))
ngrams_list = [t.text for t in ngrams_list]
ngrams = Counter(ngrams_list).most_common(most_common_count)
left_center.dataframe([{"phrase": k, "count": v} for (k, v) in ngrams])

ngrams_list = list(textacy.extract.ngrams(doc, 3, min_freq=2))
ngrams_list = [t.text for t in ngrams_list]
ngrams = Counter(ngrams_list).most_common(most_common_count)
right_center.dataframe([{"phrase": k, "count": v} for (k, v) in ngrams])
