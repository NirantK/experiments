import collections
import time
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import streamlit as st
import textacy
import textacy.similarity
import textacy.tm  
import textacy.vsm
from fastcore.dispatch import *
from textacy.spacier.doc_extensions import get_preview, get_tokens

st.title("Text Analysis")
st.markdown("Demo Client: **Abhibus**")
preview_count = 5
min_freq_count = 1

api_url = st.text_input(
    "Please share your Sheet **API** link here",
    value="https://api.steinhq.com/v1/storages/5f619d225d3cdc44fcd7d4b1",
)
sheet = st.text_input("Please input your sheet name here:", value="Queries150")
col_name = st.text_input(
    "What is the name of the column which has user queries?", value="QueryText"
)
data_url = f"{api_url}/{sheet}"


@st.cache
def read_data_to_df(url: str):
    df = pd.read_json(url)
    return df


df = read_data_to_df(data_url)

st.markdown("## Text Preview")

st.markdown(f"Here are {preview_count} random samples from the input")
preview_df = df.sample(preview_count, random_state=37)
preview_df

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

"### Preparing for Analysis"
st.write(
    "Use a larger number for quick analysis in the beginning and reduce when you are going for depth"
)
min_token_count = st.number_input(
    "Analyze sentences which have atleast how many tokens?",
    value=2,
    min_value=2,
    max_value=10,
)


def make_corpus(
    df: pd.DataFrame, col_name: str, min_token_count: int
) -> textacy.Corpus:
    spacy_records = df[col_name].apply(lambda x: textacy.make_spacy_doc(x, lang="en"))
    long_records = [
        record for record in spacy_records if len(record) >= min_token_count
    ]
    corpus = textacy.Corpus("en", data=list(long_records))
    return corpus


corpus = make_corpus(df, col_name="QueryText", min_token_count=min_token_count)
corpus
"Docs:", corpus.n_docs, "Sentences:", corpus.n_sents, "Tokens:", corpus.n_tokens


if st.checkbox("Explore Word Frequencies"):
    st.markdown("## Word Frequencies Exploration")
    min_freq_count = st.slider(
        "What is the minimum frequency of words you want to see?",
        value=3,
        min_value=2,
        max_value=10,
    )
    freq_dict: Dict = corpus.word_counts(as_strings=True)

    freq_dict = {
        k: v
        for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
        if v >= min_freq_count
    }

    freq_df = pd.DataFrame(freq_dict, index=["Frequency"]).transpose()
    st.write(freq_df)
    st.bar_chart(data=freq_df)

if st.checkbox("Explore Word Sets"):
    st.markdown("## Word Set Exploration")

    def make_doc_term_matrix(
        corpus: textacy.Corpus,
        min_freq_count: int,
        ngrams: int = 1,
        entities: bool = True,
    ):
        vectorizer = textacy.vsm.Vectorizer(
            tf_type="linear",
            apply_idf=True,
            idf_type="smooth",
            norm="l2",
            min_df=min_freq_count,
            max_df=0.95,
        )
        doc_term_matrix = vectorizer.fit_transform(
            (
                doc._.to_terms_list(ngrams=ngrams, entities=entities, as_strings=True)
                for doc in corpus
            )
        )
        return vectorizer, doc_term_matrix

    ngrams = st.number_input("ngrams:", value=2, min_value=1, max_value=3)
    vectorizer, doc_term_matrix = make_doc_term_matrix(
        corpus, min_freq_count=min_freq_count, ngrams=ngrams
    )
    repr(doc_term_matrix)

    n_topics = st.number_input(
        "How many topics do you want to explore?", value=3, min_value=2, max_value=10
    )
    model = textacy.tm.TopicModel("nmf", n_topics=n_topics)
    model.fit(doc_term_matrix)
    doc_topic_matrix = model.transform(doc_term_matrix)
    doc_topic_matrix.shape
    for topic_idx, top_terms in model.top_topic_terms(vectorizer.id_to_term, top_n=5):
        st.markdown(f"Word Set {topic_idx+1} : {'; '.join(top_terms)}")

if st.checkbox("Find Similar Sentences"):
    "## Similar Sentences"

    input_sentence = st.text_input(
        "Enter your sentence to which you want to find similar examples",
        value="train ticket cancel",
        max_chars=300,
    )
    input_doc = textacy.make_spacy_doc(input_sentence, lang="en")

    sent_count = st.slider(
        "Maximum number of Similar sentences that you want",
        min_value=1,
        max_value=10,
        value=3,
    )
    similarity_cutoff = (
        st.slider("Similarity Cutoff", min_value=1, max_value=100, value=70) / 100.0
    )
    for i, doc in enumerate(corpus):
        score = textacy.similarity.word2vec(input_doc, doc)
        if score >= similarity_cutoff and sent_count > 0:
            st.write(doc, f"{score:.2f}")
            sent_count -= 1
        elif sent_count <= 0:
            st.write("---*Finished*---")
            break

if st.checkbox("Words in Sentences Explorer"):
    "## Find Sentences with Specific Words"
    input_sentence = st.text_input(
        "Enter the words (separated by space)", value="ticket", max_chars=300
    )
    input_doc = textacy.make_spacy_doc(input_sentence, lang="en")
    input_tokens: set = set([str(x) for x in get_tokens(input_doc)])
    sent_count = st.slider(
        "Maximum number of sentences that you want", min_value=1, max_value=10, value=3
    )
    for i, doc in enumerate(corpus):
        doc_tokens = set([str(x) for x in get_tokens(doc)])
        if len(input_tokens.intersection(doc_tokens)) >= len(input_tokens):
            st.write(doc)
            sent_count -= 1
        if sent_count == 0:
            break

# option = st.sidebar.selectbox("Which sample do you like best?", df["QueryText"])

# "You selected:", option

# Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     # Update the progress bar with each iteration.
#     latest_iteration.text(f"Iteration {i+1}")
#     bar.progress(i + 1)
#     # time.sleep(0.1)
