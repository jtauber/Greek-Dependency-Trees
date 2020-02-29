import re

PERSON = r"(?P<person>[123_])"
PERSON_ = r"(?P<person>[-123_])"
NUMBER = r"(?P<number>[sdp_])"
NUMBER_ = r"(?P<number>[-sdp_])"
VOICE = r"(?P<voice>[aemp_])"
VOICE_ = r"(?P<voice>[-aemp_])"
GENDER = r"(?P<gender>[fmn_])"
GENDER_ = r"(?P<gender>[-fmn_])"
CASE = r"(?P<case>[navgd_])"
CASE_ = r"(?P<case>[-navgd_])"
DEGREE_ = r"(?P<degree>[-pcs_])"
TENSE_ = r"(?P<tense>[-pifarlt_])"
TENSE_P_ = r"(?P<tense>[-pfart_])"
MOOD_F = r"(?P<mood>[miso_])"
MOOD_N = r"(?P<mood>n)"
MOOD_P = r"(?P<mood>p)"

POS_A = r"(?P<pos>a)"  # adjective
POS_L = r"(?P<pos>l)"  # article
POS_M = r"(?P<pos>m)"  # numeral
POS_N = r"(?P<pos>n)"  # noun
POS_P = r"(?P<pos>p)"  # pronoun
POS_V = r"(?P<pos>v)"  # verb
POS_X = r"(?P<pos>x)"  # ???

# c: conjunction
# d: adverb
# g: particle
# i: interjection
# r: preposition
# u: punctuation
POS_INDECL = r"(?P<pos>[cdgiru])"

REGEXES1 = [
    f"d-------{DEGREE_}",
    f"{POS_INDECL}--------",

    f"{POS_X}-{NUMBER_}---{GENDER_}{CASE_}-",  # ???
    f"{POS_M}-{NUMBER_}---{GENDER_}{CASE_}-",  # numeral
    f"{POS_N}-{NUMBER_}---{GENDER_}{CASE_}-",  # noun

    f"{POS_L}-{NUMBER}---{GENDER}{CASE}-",  # article

    f"{POS_A}-{NUMBER}---{GENDER_}{CASE_}{DEGREE_}",  # adjective

    f"{POS_P}{PERSON_}{NUMBER_}---{GENDER_}{CASE_}-",  # pronoun

    f"{POS_V}{PERSON}{NUMBER}{TENSE_}{MOOD_F}{VOICE}---",  # finite verb
    f"{POS_V}--{TENSE_P_}{MOOD_N}{VOICE}---",  # infinitive
    f"{POS_V}-{NUMBER}{TENSE_P_}{MOOD_P}{VOICE}{GENDER}{CASE}-",  # participle

    f"{POS_A}-------[-cs]",
    f"{POS_A}-----{GENDER_}{CASE_}{DEGREE_}",
    "c-------_",
    "r-------_",
    "c2sfim---",
    "d-p---ma-",
    f"{POS_N}-{NUMBER_}---{GENDER_}l-",
    f"{POS_N}-{NUMBER_}---{GENDER_}{CASE_}_",
    "r-s---fv-",
    "l-p----g-",

    # g mood? should these be participles?
    f"{POS_V}-{NUMBER}{TENSE_}g{VOICE}{GENDER}{CASE}-",
    f"{POS_V}-{NUMBER}{TENSE_}g{VOICE}{GENDER}{CASE}-",
    f"{POS_V}-{NUMBER}{TENSE_}g{VOICE}{GENDER}{CASE}-",
    f"{POS_V}-{NUMBER}{TENSE_}g{VOICE}{GENDER}{CASE}-",

    # infinitives
    f"{POS_V}--i{MOOD_N}{VOICE}---",  # can't have imperfect infinitive
    f"{POS_V}--{TENSE_}{MOOD_N}{VOICE}--c",  # bad degree
    f"{POS_V}--{TENSE_}{MOOD_N}d---",  # VOICE=d

    f"{POS_V}-{NUMBER}{TENSE_}{MOOD_N}{VOICE}---",  # infinitives with NUMBER
    f"{POS_V}{PERSON}{NUMBER}{TENSE_}{MOOD_N}{VOICE}---",  # infinitives with NUMBER and PERSON

    # participles
    f"{POS_V}-{NUMBER}{TENSE_}{MOOD_P}{VOICE}{GENDER}{CASE}[p_]",  # bad DEGREE

    f"{POS_V}3{NUMBER}{TENSE_}{MOOD_P}{VOICE}{GENDER}{CASE}_",  # participle with PERSON and DEGREE
    f"{POS_V}--{TENSE_}{MOOD_P}{VOICE}{GENDER}{CASE}-",  # participle without NUMBER
    f"{POS_V}{PERSON}{NUMBER}{MOOD_P}-a---",  # GENDER=a

    # finites
    f"{POS_V}{PERSON}{NUMBER}{TENSE_}{MOOD_F}{VOICE}{GENDER}--",  # shouldn't have GENDER
    f"{POS_V}{PERSON}{NUMBER}{TENSE_}{MOOD_F}d---",  # VOICE=d
    f"{POS_V}{PERSON}{NUMBER}{TENSE_}{MOOD_F}{VOICE}--c",  # shouldn't have DEGREE
    f"{POS_V}{PERSON}{NUMBER}{TENSE_}{MOOD_F}----",  # missing VOICE

    f"{POS_V}-{NUMBER}{TENSE_}{MOOD_F}{VOICE}{GENDER}{CASE}-",  # finite without PERSON but with CASE; is this a participle?

    f"{POS_V}--{TENSE_}{MOOD_F}{VOICE}---",  # finite without PERSON or NUMBER

    f"{POS_V}{PERSON}{NUMBER}------",  # no mood


    f"{POS_V}__{TENSE_P_}{MOOD_N}{VOICE}---",
    f"{POS_V}-{NUMBER}{TENSE_P_}{MOOD_P}-{GENDER}{CASE}-",
    f"{POS_V}-{NUMBER}{TENSE_P_}{MOOD_P}{VOICE}{GENDER}{CASE}_",
    "_--------",
]


def test_postag(postag):
    for regex in REGEXES1:
        if m := re.match(regex + "$", postag):
            break
    else:
        return False
    return True
