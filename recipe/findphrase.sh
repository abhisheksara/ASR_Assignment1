#!/bin/sh

./steps/get_train_ctm.sh data/train_sp3/ data/lang exp/tri1

grep $1 ./exp/tri1/ctm > instances.txt

python3 findphrase.py
