#!/usr/bin/env bash

# Explains the provenance of all duplicates. test_lexicon.py uses a bloom filter
# for efficient duplicate detection and therefore only lists *probable*
# duplicates. This script lists the derivation of all duplicates explicitly. As
# long as each putative duplicate only have one derivation, everything is okay
# and those false positives can be added to collisions.tsv.

mv collisions.tsv collisions.tsv.tmp;

for DUPLICATE in `python test_lexicon.py 2>&1 | head -n-1 | cut -d' ' -f1`; do
    WORD=${DUPLICATE[2,${#DUPLICATE}-1]};
    echo "-- $WORD --";
    python test_lexicon.py $WORD;
done;

mv collisions.tsv.tmp collisions.tsv;
