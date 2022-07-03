#!/bin/sh

#  filter_dict.py
#  
#
#  Created by Eleanor Chodroff on 2/22/15.
# This script filters out words which are not in our corpus.
# It requires a list of the words in the corpus: words.txt
#/home/deepu/Desktop/Assignment_IIITH/kaldi/egs/mycorpus/data/local/lang

import os

ref = dict()
phones = dict()

with open("//home/deepu/Desktop/Assignment_IIITH/kaldi/egs/mycorpus/data/local/lang//lexicon.txt","r") as f:
    for line in f:
        line = line.strip()
        columns = line.split(" ", 1)
        word = columns[0]
        pron = columns[1]
        try:
            ref[word].append(pron)
        except:
            ref[word] = list()
            ref[word].append(pron)

print(ref)

lex = open("/home/deepu/Desktop/Assignment_IIITH/kaldi/egs/mycorpus/data/local/lang/lexicon.txt", "wb")

with open("/home/deepu/Desktop/Assignment_IIITH/kaldi/egs/mycorpus/data/train/words.txt","r") as f:
    for line in f:
        line = line.strip()
        if line in ref.keys():
            for pron in ref[line]:
                lex.write(line + " " + pron+"\n")
        else:
            print("Word not in lexicon:" + line)


