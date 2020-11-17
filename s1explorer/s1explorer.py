import collections
import json
import time
from typing import Dict, List, Tuple

import streamlit as st
import textacy
from fastcore.utils import Path
from textacy.spacier.doc_extensions import get_preview, get_tokens

st.title("s1explorer.com")
st.subheader("Exploring S1 documents with NLP tools")

import io
st.set_option("deprecation.showfileUploaderEncoding", False)

with st.beta_expander("Credits"):
    st.markdown("Created by [Nirant](https://nirantk.com) || Twitter: [@NirantK](https://twitter.com/NirantK)"
    )

## Frequency Calculation

if st.sidebar.checkbox("Ignore Case (Recommended)", value=True):
    freq_dict: Dict = corpus.word_counts(
        as_strings=True, normalize="lower", filter_nums=True, filter_punct=True
    )
else:
    freq_dict: Dict = corpus.word_counts(
        as_strings=True, filter_nums=True, filter_punct=True
    )

freq_dict = {
    k: v
    for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    if v >= 2
}

min_freq_count = st.sidebar.slider(
    "What is the minimum frequency of words you want to see?",
    value=int(freq_df[index_key].quantile(0.81)),
    min_value=2,
    max_value=int(freq_df[index_key].quantile(0.999)),
)
freq_df = freq_df[freq_df[index_key] > min_freq_count]
left, right = st.beta_columns([2, 1])
left.bar_chart(freq_df)
word_display_count = min(20, len(freq_df))
right.markdown(f"Top {word_display_count} words by frequency")
right.table(freq_df[:word_display_count])