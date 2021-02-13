#!/bin/sh

[ ! -L "utils" ] && ln -s ../../wsj/s5/utils

python3 data-prep.py

touch ./corpus/data/train/spk2utt
touch ./corpus/data/test/spk2utt
touch ./corpus/data/truetest/spk2utt

#generates spk2utt files from utt2spk
./utils/utt2spk_to_spk2utt.pl ./corpus/data/train/utt2spk > ./corpus/data/train/spk2utt
./utils/utt2spk_to_spk2utt.pl ./corpus/data/test/utt2spk > ./corpus/data/test/spk2utt
./utils/utt2spk_to_spk2utt.pl ./corpus/data/truetest/utt2spk > ./corpus/data/truetest/spk2utt


#sorting all files

LC_ALL=C sort -o corpus/data/train/text corpus/data/train/text
LC_ALL=C sort -o corpus/data/train/wav.scp corpus/data/train/wav.scp
LC_ALL=C sort -o corpus/data/train/spk2utt corpus/data/train/spk2utt
LC_ALL=C sort -o corpus/data/train/utt2spk corpus/data/train/utt2spk

LC_ALL=C sort -o corpus/data/test/text corpus/data/test/text
LC_ALL=C sort -o corpus/data/test/wav.scp corpus/data/test/wav.scp
LC_ALL=C sort -o corpus/data/test/spk2utt corpus/data/test/spk2utt
LC_ALL=C sort -o corpus/data/test/utt2spk corpus/data/test/utt2spk

LC_ALL=C sort -o corpus/data/truetest/text corpus/data/truetest/text 
LC_ALL=C sort -o corpus/data/truetest/wav.scp corpus/data/truetest/wav.scp
LC_ALL=C sort -o corpus/data/truetest/spk2utt corpus/data/truetest/spk2utt
LC_ALL=C sort -o corpus/data/truetest/utt2spk corpus/data/truetest/utt2spk


./utils/fix_data_dir.sh corpus/data/train
./utils/fix_data_dir.sh corpus/data/test
./utils/fix_data_dir.sh corpus/data/truetest
