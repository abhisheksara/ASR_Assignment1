#!/bin/bash
# Copyright 2012  Johns Hopkins University (Author: Daniel Povey)
# Apache 2.0

[ -f ./path.sh ] && . ./path.sh

# begin configuration section.
cmd=run.pl
stage=0
decode_mbr=true
word_ins_penalty=0.0
min_lmwt=7
max_lmwt=17
#end configuration section.

[ -f ./path.sh ] && . ./path.sh
. parse_options.sh || exit 1;

data="data/test"
lang_or_graph="data/lang"
dir="exp/tri1/decode_test"

symtab=$lang_or_graph/words.txt

for f in $symtab $dir/lat.1.gz $data/text; do
  [ ! -f $f ] && echo "score.sh: no such file $f" && exit 1;
done

mkdir -p $dir/scoring/log

cat $data/text | sed 's:<NOISE>::g' | sed 's:<SPOKEN_NOISE>::g' > $dir/scoring/test_filt.txt

$cmd LMWT=$min_lmwt:$max_lmwt $dir/scoring/log/best_path.LMWT.log \
  lattice-scale --inv-acoustic-scale=LMWT "ark:gunzip -c $dir/lat.*.gz|" ark:- \| \
  lattice-add-penalty --word-ins-penalty=$word_ins_penalty ark:- ark:- \| \
  lattice-best-path --word-symbol-table=$symtab \
    ark:- ark,t:$dir/scoring/LMWT.tra || exit 1;

list_of_files=$(python3 split_speakers.py | tr -d "[],'")

# Note: the double level of quoting for the sed command
for f in ${list_of_files[@]};
  do
  $cmd LMWT=$min_lmwt:$max_lmwt $dir/scoring/log/score.LMWT.log \
    cat $dir/scoring/LMWT.tra \| \
      utils/int2sym.pl -f 2- $symtab \| sed 's:\<UNK\>::g' \| \
      compute-wer --text --mode=present \
      ark:$dir/scoring/$f  ark,p:- ">&" $dir/wer_LMWT || exit 1;

  for x in exp/tri1/decode*; do [ -d $x ] && grep WER $x/wer_* | utils/best_wer.sh | sed "s/%WER/$f/g" > out.txt; done

  python3 score_output.py
  rm $dir/scoring/$f
  rm out.txt
done;

exit 0;
