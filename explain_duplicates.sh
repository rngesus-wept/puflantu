#!/usr/bin/env bash

# Explains the provenance of all duplicates. test_lexicon.py uses a bloom filter
# for efficient duplicate detection and therefore only lists *probable*
# duplicates. This script lists the derivation of all duplicates explicitly. As
# long as each putative duplicate only have one derivation, everything is okay
# and those false positives can be added to collisions.tsv.

LEX_FILE=/tmp/perflontus_lexicon;
ERR_FILE=/tmp/perflontus_stderr;

python test_lexicon.py 2>$ERR_FILE > $LEX_FILE;
sort $LEX_FILE | uniq -w 32 -D;
