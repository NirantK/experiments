"""
Easy Data Augmentation

Based on the work by Jason Wei and Kai Zou
https://github.com/jasonwei20/eda_nlp

@author: Nirant Kasliwal nirant@verloop.io
"""
from preprocessing import *
import random
import re
from pathlib import Path
from random import shuffle
from typing import List, Tuple, Union

# for the first time you use wordnet
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet

strOrNone = Union[str, None]

with Path("artifacts/stopwords.txt").open("r") as f:
    stop_words = f.readlines()

def is_alpha(char:str)->bool:
    """
    Check whether a character is an English alphabet or not
    
    Args:
        word (str): [description]
    
    Returns:
        Boolean: [description]
    """
    try:
        return char.encode('ascii').isalpha()
    except:
        return False


def get_only_chars(line: str):
    """
    Removes vowels from a line, I guess?
    
    Args:
        line (str): [description]
    
    Returns:
        clean_line (str): [description]
    """
    line = fix_html(line)
    line = deal_caps(line)

    clean_line = [char if is_alpha(char) else " " for char in line]
    clean_line = rm_useless_spaces(clean_line)  # delete extra spaces
    return clean_line


def synonym_replacement(words: str, n: int):
    """
    Replace n words in the sentence with synonyms from wordnet
    
    Args:
        words (str): [description]
        n (int): [description]
    
    Returns:
        new_words (List[str]): [description]
    """

    new_words = words.copy()
    random_word_list = list(set([word for word in words if word not in stop_words]))
    random.shuffle(random_word_list)
    num_replaced = 0
    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        if len(synonyms) >= 1:
            synonym = random.choice(list(synonyms))
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        if num_replaced >= n:  # only replace up to n words
            break

    return new_words


def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonym = l.name().replace("_", " ").replace("-", " ").lower()
            synonym = "".join(
                [char for char in synonym if char in " qwertyuiopasdfghjklzxcvbnm"]
            )
            synonyms.add(synonym)
    if word in synonyms:
        synonyms.remove(word)
    return list(synonyms)


def random_deletion(words, p):
    """
    Randomly delete words from the sentence with probability p    
    
    Args:
        words ([type]): [description]
        p ([type]): [description]
    
    Returns:
        [type]: [description]
    """
    # obviously, if there's only one word, don't delete it
    if len(words) == 1:
        return words

    # randomly delete words with probability p
    new_words = []
    for word in words:
        r = random.uniform(0, 1)
        if r > p:
            new_words.append(word)

    # if you end up deleting all words, just return a random word
    if len(new_words) == 0:
        rand_int = random.randint(0, len(words) - 1)
        return [words[rand_int]]

    return new_words


def random_swap(words, n):
    """
    Randomly swap two words in the sentence n times

    
    Args:
        words ([type]): [description]
        n ([type]): [description]
    
    Returns:
        [type]: [description]
    """

    def swap_word(new_words):
        random_idx_1 = random.randint(0, len(new_words) - 1)
        random_idx_2 = random_idx_1
        counter = 0
        while random_idx_2 == random_idx_1:
            random_idx_2 = random.randint(0, len(new_words) - 1)
            counter += 1
            if counter > 3:
                return new_words
        new_words[random_idx_1], new_words[random_idx_2] = (
            new_words[random_idx_2],
            new_words[random_idx_1],
        )
        return new_words

    new_words = words.copy()
    for _ in range(n):
        new_words = swap_word(new_words)
    return new_words


def random_insertion(words, n):
    """
    Randomly insert n words into the sentence
    
    Args:
        words ([type]): [description]
        n ([type]): [description]
    
    Returns:
        [type]: [description]
    """

    def add_word(new_words):
        synonyms = []
        counter = 0
        while len(synonyms) < 1:
            random_word = new_words[random.randint(0, len(new_words) - 1)]
            synonyms = get_synonyms(random_word)
            counter += 1
            if counter >= 10:
                return
        random_synonym = synonyms[0]
        random_idx = random.randint(0, len(new_words) - 1)
        new_words.insert(random_idx, random_synonym)

    new_words = words.copy()
    for _ in range(n):
        add_word(new_words)
    return new_words


def augment(
    sentence: str,
    alpha_sr: float = 0.1,
    alpha_ri: float = 0.1,
    alpha_rs: float = 0.1,
    p_rd: float = 0.1,
    num_aug: float = 9,
):
    """
    Main driver function which takes in one sentences and returns a list of num_aug sentences
    
    Args:
        sentence (str): input sentence for augmentation
        alpha_sr (float, optional): Synonym Replacement Probability. Defaults to 0.1.
        alpha_ri (float, optional): Random Insertion Probability. Defaults to 0.1.
        alpha_rs (float, optional): Random Swap Probability. Defaults to 0.1.
        p_rd (float, optional): Percentaged of words to delete randomly. Defaults to 0.1.
        num_aug (int, optional): Number of augmented sentences to return. Defaults to 9.
    
    Returns:
        List[str]: [description]
    """
    sentence = get_only_chars(sentence)
    words = sentence.split(" ")
    words = [word for word in words if word is not ""]
    num_words = len(words)

    augmented_sentences = []
    num_new_per_technique = int(num_aug / 4) + 1
    n_sr = max(1, int(alpha_sr * num_words))
    n_ri = max(1, int(alpha_ri * num_words))
    n_rs = max(1, int(alpha_rs * num_words))

    # synonym replacement
    for _ in range(num_new_per_technique):
        a_words = synonym_replacement(words, n_sr)
        augmented_sentences.append(" ".join(a_words))

    # random insertion
    for _ in range(num_new_per_technique):
        a_words = random_insertion(words, n_ri)
        augmented_sentences.append(" ".join(a_words))

    # random swap
    for _ in range(num_new_per_technique):
        a_words = random_swap(words, n_rs)
        augmented_sentences.append(" ".join(a_words))

    # random delete
    for _ in range(num_new_per_technique):
        a_words = random_deletion(words, p_rd)
        augmented_sentences.append(" ".join(a_words))

    augmented_sentences = [get_only_chars(sentence) for sentence in augmented_sentences]
    shuffle(augmented_sentences)

    # trim so that we have the desired number of augmented sentences
    if num_aug >= 1:
        augmented_sentences = augmented_sentences[:num_aug]
    else:
        keep_prob = num_aug / len(augmented_sentences)
        augmented_sentences = [
            s for s in augmented_sentences if random.uniform(0, 1) < keep_prob
        ]

    # append the original sentence
    augmented_sentences.append(sentence)

    return augmented_sentences
