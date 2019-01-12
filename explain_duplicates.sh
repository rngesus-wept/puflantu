#!/usr/bin/env bash

mv collisions.tsv collisions.tsv.tmp;

for DUPLICATE in `python test_lexicon.py 2>&1 | head -n-1 | cut -d' ' -f1`; do
    WORD=${DUPLICATE[2,${#DUPLICATE}-1]};
    echo "-- $WORD --";
    python test_lexicon.py $WORD;
done;

mv collisions.tsv.tmp collisions.tsv;
