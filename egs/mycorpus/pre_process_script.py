#!/usr/bin/env python
# coding: utf-8

import pandas as pd
sep = " "

# Reading df with audio end time
df = pd.read_csv("val_with_end_audio.csv")

# Create segments file
segments_df = df[["wav_filename", "wav_filename", "start_time", "end_time"]]
segments_df.to_csv("data/train/segments", sep=sep, index=False, header=False)

# Create wav.scp
wav_scp = df[["wav_filename", "wav_filename"]]
wav_scp.to_csv("data/train/wav.scp", sep=sep, index=False, header=False)

# Create utt2spk
speaker_df = df.copy()
df["speaker"] = df["wav_filename"].apply(lambda x : x.split("/")[0])
utt2spk_df = df[["wav_filename", "speaker"]]
utt2spk_df.to_csv("data/train/utt2spk", sep=sep, index=False, header=False)


# In[ ]:




