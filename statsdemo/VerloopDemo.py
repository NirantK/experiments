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


"## Generate Sentences Similar to Input"

from transformers import MarianMTModel, MarianTokenizer


def translate(texts, model, tokenizer, language="fr"):
    """"""
    # Prepare the text data into appropriate format for the model
    template = lambda text: f"{text}" if language == "en" else f">>{language}<< {text}"
    src_texts = [template(text) for text in texts]
    # Tokenize the texts
    encoded = tokenizer.prepare_seq2seq_batch(src_texts)

    # Generate translation using model
    translated = model.generate(**encoded)

    # Convert the generated tokens indices back into text
    translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)

    return translated_texts


@st.cache
def download_model_tokenizer_files(romance_lang: str = "ROMANCE"):
    ROMANCE = romance_lang

    target_model_name = f"Helsinki-NLP/opus-mt-en-{ROMANCE}"
    target_tokenizer = MarianTokenizer.from_pretrained(target_model_name)
    target_model = MarianMTModel.from_pretrained(target_model_name)

    en_model_name = f"Helsinki-NLP/opus-mt-{ROMANCE}-en"
    en_tokenizer = MarianTokenizer.from_pretrained(en_model_name)
    en_model = MarianMTModel.from_pretrained(en_model_name)
    return en_model, en_tokenizer, target_model, target_tokenizer


def back_translate(texts, source_lang="en", target_lang="fr"):
    """
    Paraphrasing via Back Translation
    """
    (
        en_model,
        en_tokenizer,
        target_model,
        target_tokenizer,
    ) = download_model_tokenizer_files(romance_lang=target_lang)

    # Translate from source to target language
    fr_texts = translate(texts, target_model, target_tokenizer, language=target_lang)

    # Translate from target language back to source language
    back_translated_texts = translate(
        fr_texts, en_model, en_tokenizer, language=source_lang
    )

    return back_translated_texts


from random import choice
from typing import List

download_model_tokenizer_files("ROMANCE")
download_model_tokenizer_files("zh")
download_model_tokenizer_files("hi")


@st.cache
def augment(en_texts: List[str]):
    random_romance_lang = choice(["fr", "es", "la", "it", "pt", "ro"])
    random_asian_lang = choice(["zh", "hi"])
    return back_translate(
        back_translate(en_texts, source_lang="en", target_lang="zh"),
        source_lang="en",
        target_lang="es",
    )


input_sentences = st.text_input(
    "Enter as many sentences as you want, separated by ||"
).split("||")
min_freq_count = st.slider(
    "How many tries do you want to make?",
    value=1,
    min_value=1,
    max_value=5,
)

while min_freq_count > 0:
    st.markdown(back_translate(input_sentences))
    min_freq_count -= 1

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
