import streamlit as st
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
def get_model_tokenizer_files(romance_lang: str = "ROMANCE"):
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

    def get_model_tokenizer_files(romance_lang: str = "ROMANCE"):
        """
        Adding a nested function, because this shit was unreadable enough already

        Args:
            romance_lang (str, optional): [description]. Defaults to "ROMANCE".

        Returns:
            [type]: [description]
        """
        ROMANCE = romance_lang

        target_model_name = f"Helsinki-NLP/opus-mt-en-{ROMANCE}"
        target_tokenizer = MarianTokenizer.from_pretrained(target_model_name)
        target_model = MarianMTModel.from_pretrained(target_model_name)

        en_model_name = f"Helsinki-NLP/opus-mt-{ROMANCE}-en"
        en_tokenizer = MarianTokenizer.from_pretrained(en_model_name)
        en_model = MarianMTModel.from_pretrained(en_model_name)
        return en_model, en_tokenizer, target_model, target_tokenizer

    (
        en_model,
        en_tokenizer,
        target_model,
        target_tokenizer,
    ) = get_model_tokenizer_files(romance_lang=target_lang)

    # Translate from source to target language
    fr_texts = translate(texts, target_model, target_tokenizer, language=target_lang)

    # Translate from target language back to source language
    back_translated_texts = translate(
        fr_texts, en_model, en_tokenizer, language=source_lang
    )

    return back_translated_texts


from random import choice
from typing import List


def augment(en_texts: List[str]):
    return back_translate(
        back_translate(en_texts, source_lang="en", target_lang="zh"),
        source_lang="en",
        target_lang="es",
    )
