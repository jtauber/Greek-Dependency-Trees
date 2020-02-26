#!/usr/bin/env python3

import glob
import re

from lxml import etree

for filename in sorted(glob.glob("xml versions/*.xml")):
    if "jan 15" in filename:
        continue
    with open(filename) as f:
        tree = etree.parse(f)

        for sentence in tree.xpath("/treebank/sentence"):
            sentence_id = sentence.attrib["id"]
            document_id = sentence.attrib["document_id"]
            subdoc = sentence.attrib["subdoc"]
            span = sentence.attrib.get("span")

            for word in sentence:
                word_id = word.attrib["id"]
                form = word.attrib["form"]
                relation = word.attrib["relation"]
                head = word.attrib["head"]
                lemma = word.attrib.get("lemma")
                postag = word.attrib.get("postag")
                cid = word.attrib.get("cid")
                insertion_id = word.attrib.get("insertion_id")
                artificial = word.attrib.get("artificial")
                form_original = word.attrib.get("form_original")
                ref = word.attrib.get("ref")

                if lemma and postag:
                    if document_id.startswith("http://perseids.org/cts5/nemo/citations/"):
                        document_id = document_id[len("http://perseids.org/cts5/nemo/citations/"):]
                    if document_id.startswith("http://perseids.org/annotsrc/"):
                        document_id = document_id[len("http://perseids.org/annotsrc/"):]
                    if document_id.startswith("http://data.perseus.org/texts/"):
                        document_id = document_id[len("http://data.perseus.org/texts/"):]
                    m = re.match("(urn:cts:greekLit:tlg\d{4}.tlg\d{3}.perseus-grc\d):", document_id)
                    if m:
                        document_id = m.group(1)
                    if document_id == "0014-059":
                        document_id = "urn:cts:greekLit:tlg0014.tlg059.perseus-grc1"
                    if document_id == "0014-046":
                        document_id = "urn:cts:greekLit:tlg0014.tlg046.perseus-grc1"
                    if document_id == "0014-049":
                        document_id = "urn:cts:greekLit:tlg0014.tlg049.perseus-grc1"
                    if document_id == "0014-001":
                        document_id = "urn:cts:greekLit:tlg0014.tlg001.perseus-grc1"
                    if re.match("urn:cts:greekLit:tlg\d{4}.tlg\d{3}.perseus-grc\d$", document_id):
                        if not re.match("\d+([A-Za-z]|(\.\d+[a-z]?)*)(-\d+(\.\d+[a-z]?)*)?$", subdoc):
                            if subdoc:
                                print(filename, document_id, sentence_id)
                                print(subdoc)
                                print("@@@")
                                quit()
                    else:
                        print(filename, sentence_id, document_id, subdoc)
                        print("###")
                        quit()

                    if postag[0] != "u":
                        print(
                            document_id[20:24],
                            document_id[28:31],
                            subdoc,
                            sentence_id,
                            word_id,
                            form,
                            postag,
                            lemma,
                            sep="\t",
                        )
