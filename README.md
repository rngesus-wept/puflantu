
# Table of Contents

1.  [Installing and Contributing](#org33b9d89)
    1.  [Dependencies](#org2a66e1d)
2.  [How to *Puflantu*](#org515604b)
    1.  [General Language Elements](#org84b8a7b)
    2.  [Sounds](#org1784cb6)



<a id="org33b9d89"></a>

# Installing and Contributing


<a id="org2a66e1d"></a>

## Dependencies

-   **[Python 3.7+](https://www.python.org/downloads/):** Python 3 would technically be good enough but 3.7 is the
    version the virtual environment happens to be installed to.
-   **[pip](https://pip.pypa.io/en/stable/installing/):** Be sure that you install a version compatible with Python 3.7;
    depending on your system package manager, this may be under the \`pip3\`
    name (with \`pip\` defaulting to Python 2).
-   **[pipenv](https://pipenv.readthedocs.io/en/latest/install/):** This allows you to isolate this project's dependencies in its own
    virtual environment, without affecting your main Python installation.


<a id="org515604b"></a>

# How to *Puflantu*


<a id="org84b8a7b"></a>

## General Language Elements

Spelling is directly mapped onto pronunciation, which generally follows the
rules you'd expect for some kind of Romanized hybrid of Mandarin and Japanese.

Word order in Perflontus (Perflontus "*Puflantu*") is Subject-Object-Verb. Nouns
and adjectives always end in vowels. Verbs and adverbs always end in consonants.

    Alisu  Puflantu    catub.
    Alice  Perflontus  speak-she.

Descriptors are generally prepositive, i.e. they come before the things they
describe. In general Perflontus is head-final, meaning that the word that
defines the type of phrase it's in comes at the end of the phrase.


<a id="org1784cb6"></a>

## Sounds

Perflontus consists of 27 phonemes, which are mapped onto the English alphabet
plus apostrophe `'`. It has six vowels: `a`, `e`, `i`, `o`, `u`, and `w`. The first four are
pronounced as they are in Spanish or Japanese; in English these vowels appear in
"car", "bait", "feat", and "goat" respectively.

`u` is pronounced as a schwa <ə>, which appears with some frequency in English
depending on how slack the speaker is in their unstressed syllables. Examples
are the "i" in "pencil", the "e" in "camera", or the second "o" in "chocolate".
\\/ʌ\\/, as in "butt", is a reasonable allophone.

`w` is pronounced as <u>, the "oo" sound you'd expect `u` to make but it doesn't.
"Goon" and "pool" are good English examples.

Of the consonants, `b`, `d`, `j`, `k`, `l`, `m`, `n`, `p`, `r`, `s`, `t`, and `z` behave the way a
native English speaker would expect.

`f` and `v` are close to normal for English but are actually mapped to <ɸ> and
<β> respectively, which are pronounced without using one's teeth. The "f" and
"v" in Japanese and Spanish are supposed to actually use these if you're not a
gaijin/gringo. English speakers will perceive that they are blowing more air
than usual when pronouncing these.

`y` and `g` are <ɲ> and <ŋ> respectively; a reasonable shortcut for an English
speaker is to imagine a preceding "n" whenever these letters are encountered.
Italian and Spanish use "gn" and "ñ" respectively for <ɲ>. English "ng" is a
correct interpretation of <ŋ> but the phoneme will show up a lot more often
and in "unusual" places. For physiological reasons whenever two of `g`, `n`, and `y`
appear adjacent to one another the first is pronounced as <n> regardless of
the actual spelling used.

`q` and `x` are <tʃ> "ch" and <ʃ> "sh" respectively, corresponding to their use
in romanized Chinese.

`c` is <ʒ>, the second half of the "j" phoneme. In English it appears as the "s"
in "leisure", the "g" in "concierge", or the second half of the "x" in "luxury".

`h` is <x>, which is like English "h" but uses the back of the throat more. It's
all over the place in Hebrew/Yiddish, and its English usage is predominantly
in loan words from those language like the "ch" in "chutzpah". It is not quite
as rough as Klingon "H", because we aren't quite that deep into sci-fi tropes.

Finally, `'` is the sound of a bell. When pronouncing this as a human it is
sufficient to use a glottal stop instead &#x2013; that's the slight pause and buildup
of air that comes just before a lot of word-initial vowels in English. In
particular it happens just before both vowels in "uh-oh". For our audio work we
will overlay a bell sound on top of these pauses, so maybe draw them out a
little?

Syllables in Perflontus always contain exactly one vowel, which may be preceded
by at most one consonant, and followed by at most one consonant. This means that
an English speaker must take care to pronounce vowel and consonant clusters as
though they contain a syllable break, even if the cluster would represent a
valid English diphthong. For example `wfro` should be pronounced as `OOF-roh` and
not `OO-froh`; and `riqwa` as `REE-choo-ah` and not `REACH-wah` or `REE-chwa`. When in
doubt a consonant belongs to the same syllable as the vowel following it, e.g.
`i-qa` not `iq-a`.

Stress occurs on the syllable preceding a word's final consonant, not counting
any particles. Thus for verbs the stress will fall on the final syllable; for
nouns, on the penultimate or antepenultimate.

    A- li- su   Puf- lan- tu   ca-  tub.
    ah-LEE-suh  puff-LAHN-tuh  zhah-TUB.
