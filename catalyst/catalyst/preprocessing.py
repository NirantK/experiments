import re, html
from typing import Any, AnyStr, Callable, Collection, Dict, Hashable, Iterator, List, Mapping, NewType, Optional
BOS,EOS,FLD,UNK,PAD = 'xxbos','xxeos','xxfld','xxunk','xxpad'
TK_MAJ,TK_UP,TK_REP,TK_WREP = 'xxmaj','xxup','xxrep','xxwrep'

def spec_add_spaces(t: str) -> str:
    "Add spaces around / and # in `t`. \n"
    return re.sub(r"([/#\n])", r" \1 ", t)


def rm_useless_spaces(t: str) -> str:
    "Remove multiple spaces in `t`."
    return re.sub(" {2,}", " ", t)


def replace_rep(t: str) -> str:
    "Replace repetitions at the character level in `t`."

    def _replace_rep(m: Collection[str]) -> str:
        c, cc = m.groups()
        return f" {TK_REP} {len(cc)+1} {c} "

    re_rep = re.compile(r"(\S)(\1{3,})")
    return re_rep.sub(_replace_rep, t)


def replace_wrep(t: str) -> str:
    "Replace word repetitions in `t`."

    def _replace_wrep(m: Collection[str]) -> str:
        c, cc = m.groups()
        return f" {TK_WREP} {len(cc.split())+1} {c} "

    re_wrep = re.compile(r"(\b\w+\W+)(\1{3,})")
    return re_wrep.sub(_replace_wrep, t)


def fix_html(x: str) -> str:
    "List of replacements from html strings in `x`."
    re1 = re.compile(r"  +")
    x = (
        x.replace("#39;", "'")
        .replace("amp;", "&")
        .replace("#146;", "'")
        .replace("nbsp;", " ")
        .replace("#36;", "$")
        .replace("\\n", "\n")
        .replace("quot;", "'")
        .replace("<br />", "\n")
        .replace('\\"', '"')
        .replace("<unk>", UNK)
        .replace(" @.@ ", ".")
        .replace(" @-@ ", "-")
        .replace(" @,@ ", ",")
        .replace("\\", " \\ ")
    )
    return re1.sub(" ", html.unescape(x))


def replace_all_caps(x: Collection[str]) -> Collection[str]:
    "Replace tokens in ALL CAPS in `x` by their lower version and add `TK_UP` before."
    res = []
    for t in x:
        if t.isupper() and len(t) > 1:
            res.append(TK_UP)
            res.append(t.lower())
        else:
            res.append(t)
    return res

def deal_caps(x:Collection[str]) -> Collection[str]:
    "Replace all Capitalized tokens in `x` by their lower version and add `TK_MAJ` before."
    res = []
    for t in x:
        if t == '': continue
        if t[0].isupper() and len(t) > 1 and t[1:].islower(): res.append(TK_MAJ)
        res.append(t.lower())
    return res