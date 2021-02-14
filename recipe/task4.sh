# ./cmd.sh
# set -e
# ./path.sh
# stage=0
# nsegs=1000000;  # limit the number of training segments

# ./utils/parse_options.sh
# if ! command ngram-count >/dev/null; then
#     sdir=$KALDI_ROOT/tools/srilm/bin/i686-m64
#   if [ -f $sdir/ngram-count ]; then
#     echo Using SRILM tools from $sdir
#     export PATH=$PATH:$sdir
#   else
#     echo You appear to not have SRILM tools installed, either on your path,
#     echo or installed in $sdir.  See tools/install_srilm.sh for installation
#     echo instructions.
#     exit 1
#   fi
# fi
# ngram-count -order 1 -text ../corpus/LM/train.txt -write countsfile
# sort -n -r -k 2 countsfile | head -n 20000 | cut -f 1 > 20000.words
# ngram-count -vocab 20000.words -text ../corpus/LM/train.txt -order 3 -kndiscount1 -kndiscount2 -kndiscount3 -interpolate -lm local/corp_kn.lm.arpa
./ngram-count -limit-vocab -text corpus/LM/train.txt -order 3 -interpolate -addsmooth 0.001 -lm local/my_lm0.lm.arpa