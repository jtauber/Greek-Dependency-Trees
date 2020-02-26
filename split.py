#!/usr/bin/env python3

import re
import unicodedata

with open("gorman.txt") as f:
    c = 0
    for line in f:
        c += 1
        (
            author, work, subdoc, sentence_id, word_id, form, postag, lemma
        ) = line.strip().split("\t")
        assert re.match(r"\d{4}$", author), author
        assert re.match(r"\d{3}$", work), work
        assert re.match(r"(\d+[A-Za-z]?(\.\d+[A-Za-z]?)*)?(-\d+[A-Za-z]?(\.\d+[A-Za-z]?)*)?$", subdoc), (author, work, "|" + subdoc + "|")
        assert re.match(r"\d+", sentence_id), sentence_id
        assert re.match(r"\d+", word_id), word_id
        form = unicodedata.normalize("NFC", form)
        form = form.replace("\u02BC", "\u2019")
        form = form.replace("\u1FBD", "\u2019")
        if re.match(r"[\u0370-\u03FF\u1F00-\u1FFF]+\u2019?", form):
            pass
        elif re.match(r"(\u2019ς|\u2019|\u2019κείνῳ|\u2019κείνου|'ν|\u2019στὶ|\u2019ξαπατηθῇς|\u2019στ\u2019|\u2019στί|\[\d\]|†|.\u2019|η'|'πεπόνθεσαν|κ'|Π̔ελασγοῦ|Ρ̓ῶμε|ὅτ'|’κείνην|’κείνων|’κεῖνοι|'κείνῳ|'κείνη|'κείνους|\[παράδειγμα\]|\[ὁ\]|\[τὴν|νῆσον\])$", form):
            pass
        elif re.match(r"(-ᾆτ\u2019|-δὲ|-δέ|χ-|-ἀναντί\u2019|-ἀλεύθερ\u2019|-ἂν|οὔ-|μη-|-δ\u2019|κ-|τ-|-τε|μ-|-τ\u2019|-θ\u2019|θ-|-γὼ|-ν|το-|θο-|-δε|-πώποτε|-ὢν|-ἀσθίειν|τουτ-|κἀ-|-πὶ|οὑ-|-ᾦμαι|-τ|οὐ-|ἐγ-|-ἄπειτα|-ουν|μή-|-ποτ\u2019)$", form):
            pass
        else:
            assert False, (c, author, work, subdoc, sentence_id, word_id, form, "<-- form problem")

        if re.match(r"[\u0370-\u03FF\u1F00-\u1FFF]+", lemma):
            pass
        elif re.match(r"\[\d\]", lemma):
            pass
        elif re.match(r"(-δέ|-τε|-πώποτε)", lemma):
            pass
        else:
            assert False, (c, author, work, subdoc, sentence_id, word_id, lemma, "<-- lemma problem")
