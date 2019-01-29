
# Table of Contents

1.  [Installing and Contributing](#org2dff04a)
    1.  [Dependencies](#orga6bf19b)
2.  [Language TODOs](#orgc083247)
3.  [How to *Puflantu*](#org4f02423)
    1.  [General Language Elements](#org3b2afb3)
    2.  [Sounds](#orge1778f3)
        1.  [Vowels](#org070072a)
        2.  [Consonants](#org6065515)
        3.  [Syllables](#org047fdbc)
    3.  [Pronouns, Part 1 &#x2013; Personal Pronouns](#orga78cf44)
    4.  [Verbs, Part 1 &#x2013; Basic Infixes](#orge5d2bd6)
    5.  [Pronouns, Part 2 &#x2013; This, That, A, and The](#orge9707d1)
    6.  [Verbs, Part 2 &#x2013; Tense, Aspect, Degree, and Reversal](#org43bf3b7)
    7.  [Nouns and Adjectives, Part 1 &#x2013; Number](#org815145d)
    8.  [Verbs, Part 3 &#x2013; To Be](#orgcab24fd)
    9.  [Nouns and Adjectives, Part 2 &#x2013; Verb-Derivation](#org052d0dd)
        1.  [Gerund Case `-a`](#org2024836)
        2.  [Agent Case `-afe`](#org1678c83)
        3.  [Patient Case `-who`](#org6d02fc0)
        4.  [Instrumental Case `-aqo`](#orgdcb5b35)
        5.  [Locative Case `-ice`](#orgee1bfc2)
        6.  [Causative Case `-ede`](#orgd1e75da)



<a id="org2dff04a"></a>

# Installing and Contributing


<a id="orga6bf19b"></a>

## Dependencies

-   **[Python 3.7+](https://www.python.org/downloads/):** Python 3 would technically be good enough but 3.7 is the
    version the virtual environment happens to be installed to.
-   **[pip](https://pip.pypa.io/en/stable/installing/):** Be sure that you install a version compatible with Python 3.7;
    depending on your system package manager, this may be under the \`pip3\`
    name (with \`pip\` defaulting to Python 2).
-   **[pipenv](https://pipenv.readthedocs.io/en/latest/install/):** This allows you to isolate this project's dependencies in its own
    virtual environment, without affecting your main Python installation.


<a id="orgc083247"></a>

# Language TODOs

-   [ ] Fill out the lexicon
    -   [ ] Common verbs - to have (possess), to need, to want, to must (obligatory)
    -   [ ] Common "particles" - on, from, positions
    -   [ ] Mother, father, parent, child, other familial relations
    -   [ ] Same, different
    -   [ ] Elements of the periodic table
        -   There are some interesting etymological choices to be made here. For
            example, in human languages, many of the smaller atoms are named for
            their most common occurrences, whereas many of the larger ones are named
            for their discoverers (as people or as institutions).
-   [ ] Reflexive constructions &#x2013; easiest way is probably just to create
    another class of pronouns. In particular, because the pronoun infix always
    precedes a vowel, you can do something like add `-b` to the end of the
    existing pronoun and specify that the special reflexive pronoun never occurs
    as a word on its own. Thus `Dwmax.` "I teach" can be `Dwmbax.` "I teach myself."
    (But probably not exactly `-b`; "I teach myself" is getting a little
    phonetically close to "Dumbass" there.)
-   [ ] Passive voice &#x2013; revise section on infixing verbs to say that either a
    subject or an object infix is necessary; leaving out the subject creates the
    passive voice, e.g. `Torelwa wlodoc.` "The cookies were eaten."
-   [ ] Appositives
-   [ ] Addressing the listener
-   [ ] Imperatives
-   [ ] Adverbial suffix should be changed from `-q` (in the doc) to `-s`, which
    generalizes the change made to particles `-li`, `-ba`, `-fo` and `-vo` in a nice
    way.
-   [ ] Adpositions or equivalent &#x2013; Note that many human languages use these
    cases in ways that only overlap via locational metaphor, e.g. when
    describing *temporal* location like in "in five minutes"; and the mapping is
    not consistent across languages.
    -   Inessive (INE) &#x2013; "in" or "located at"
    -   Elative (ELA) &#x2013; "out of"
    -   Illative (ILL) &#x2013; "into" (contrast inessive, which does not have
        directional connotations)
    -   Adessive (ADE) &#x2013; "on"
    -   Ablative (ABL) &#x2013; "away from" (this one is more commonly mentioned / has
        more WP elaboration than the others; is it somehow more important?)
    -   Allative (ALL) &#x2013; "toward"
    -   Superessive (SUPE) &#x2013; "upon"
-   [ ] Use of `ag-` and `yi-` as intensifier and downtoner respectively should be
    extended to adjectives, even if they aren't verb-derived.
-   [ ] Take a moment to consider whether we have inadvertently created words
    that are deeply taboo, spoken or written, in English and whatever other
    languages we can think to check. Is there a good way to automate this check?


<a id="org4f02423"></a>

# How to *Puflantu*


<a id="org3b2afb3"></a>

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


<a id="orge1778f3"></a>

## Sounds

Perflontus consists of 27 phonemes, which are mapped onto the English alphabet
plus apostrophe `'`.


<a id="org070072a"></a>

### Vowels

It has six vowels: `a`, `e`, `i`, `o`, `u`, and `w`. The first four are pronounced as they
are in Spanish or Japanese; in English these vowels appear in "car", "bait",
"feat", and "goat" respectively.

`u` is pronounced as a schwa <ə>, which appears with some frequency in English
depending on how slack the speaker is in their unstressed syllables. Examples
are the "i" in "pencil", the "e" in "camera", or the second "o" in "chocolate".
<ʌ>, as in "butt", is a reasonable allophone.

`w` is pronounced as <u>, the "oo" sound you'd expect `u` to make but it doesn't.
"Goon" and "pool" are good English examples.


<a id="org6065515"></a>

### Consonants

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


<a id="org047fdbc"></a>

### Syllables

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
nouns, usually on the penultimate or antepenultimate.

    A- la- nu   Puf- lan- tu   ca-  tub.
    ah-LAH-nuh  puff-LAHN-tuh  zhah-TUB.

    Bu- nu   pa- i   to- re- lw- a   im   w- la- toc.
    BUH-nuh  PAH-ee  toh-RAY-loo-ah  EEM  oo-lah-TOZH.


<a id="orga78cf44"></a>

## Pronouns, Part 1 &#x2013; Personal Pronouns

Pronouns play a core role in Perflontic inflection, and therefore must be
addressed first. Perflontic pronouns have the following characteristics:

-   First/second/third person designations.
-   Subject/object designations. Formally the subject form is the nominative
    case, while the object form covers the oblique case, a.k.a. "everything
    else". (This is the same casing system English uses.)
-   Singular/dual/plural designations. The dual number refers specifically to
    two of a thing; thus separate pronouns are used to refer to "you, alone",
    "the two of you", and "y'all".
-   No gender distinctions, including for third person personals.
-   No sentience distinctions, i.e. he = she = it.

    ```
    |    | Singular | Dual    | Plural  |
    |----+----------+---------+---------|
    | 1P | wm / um  | wn / un | wy / uy |
    | 2P | iz / ez  | ij / ej | ix / ex |
    | 3P | at / ot  | ab / ob | ad / od |
    ```

Note that all the pronouns are a vowel and a consonant. (This is the main
exception to the rule that noun-like things end in vowels.) Furthermore the
vowel does not depend at all on the number, and the consonant does not depend at
all on the case.


<a id="orge5d2bd6"></a>

## Verbs, Part 1 &#x2013; Basic Infixes

Verbs have a root form which is inflected in various ways. In particular, the
root form of a verb is not a valid word unto itself. The most common way a verb
is inflected is to indicate its subject, object, and negation. This is done
through the use of infixes. The point at which a verb accepts infixes is always
immediately before its final vowel. To help in remembering this, the root form a
verb is always written with an asterisk indicating this position.

    wl*oc    "to eat"
    wlwmoc   eat-1S "I eat"
    wlizoc   eat-2S "you eat"

Each verb accepts up to three infixes, in the following order:

-   A subject pronoun, as described above. This is always present if the verb
    form is being used as a verb, even if the subject is explicitly named
    elsewhere in the sentence. (It may be absent in cases where the verb form is
    used to derive a noun.)

    ```
    Andursun  ke   toreli  wl[at]oc.
    Anderson  one  cookie  eat-3S.
    Anderson eats a cookie.

    Ke   toreli  wl[at]oc.
    One  cookie  eat-3S.
    He eats a cookie.

    Andursun ke toreli *wloc. -- Incorrect, [at] infix must still be provided.
    ```

-   A negation infix `ey`. This indicates the negation/lack of the action, *not* a
    reversal of the action. The corresponding distinction can be seen in English
    where "to not do" something is distinct from "to undo" it; this is the
    former.

    ```
    Canik    kofuri  ratiq.
    Yannick  coffee  drink-3S.
    Yannick drinks coffee.

    Canik    enxura  rat[ey]iq.
    Yannick  water   drink-3S-NEG.
    Yannick does not drink water.
    ```

-   An object pronoun, as described above. This is present to the degree that
    it needs to be for disambiguation:

    ```
    Dani   qek[wm]ad.
    Danny  meet-1S.
    I meet Danny.

    Qek[wm][ot]ad.
    Meet-1S-3O.
    I meet him.

    Dani   qek[wm][ot]ad. -- Valid with redundant 3O infix; may indicate emphasis.
    Danny  meet-1S-3O.
    I meet *Danny*.
    ```


<a id="orge9707d1"></a>

## Pronouns, Part 2 &#x2013; This, That, A, and The

"This" and "that" are demonstrative pronouns that differ from regular nouns
primarily in that they have special handling for their objective and possessive
cases that regular nouns don't. They are otherwise handled like regular nouns,
and in particular pluralized like them. These rules will be discussed later; for
now, the following table should suffice:

    |      | Singular  | Dual      | Plural      |
    |------+-----------+-----------+-------------|
    | This | ita / eta | itw / etw | itwa / etwa |
    | That | iqa / eqa | iqw / eqw | iqwa / eqwa |

Like most Perflontus nouns (again, to be covered more thoroughly later), `ita` et
al. may also be used as demonstrative adjectives.

    Demiunu  etwa       torelwa  et   wlatoc.
    Damien   these-OBJ  cookies  FUT  eat-3S.
    Damien will eat these cookies.

    Demiunu  etwa       et   wlatoc.
    Damien   these-OBJ  FUT  eat-3S.
    Damien will eat these.

    Ita       somatotun.
    This-SUB  please-3S-3O.
    This pleases him.

There is no direct equivalent for the definite article "the". Depending on the
context it is correct to either omit any qualifier at all or to use "this" or
"that" as appropriate instead.

Similarly there is no directly equivalent to the indefinite article "a(n)". When
it is necessary to refer to some indefinite item `ke` (literally "one") is used
instead.

    Tusvo  yipox  et   capatil.
    Bus    soon   FUT  arrive-3S.
    (The) bus will arrive soon.

    Ke   tusvo  yipox  et   capatil.
    One  bus    soon   FUT  arrive-3S.
    A bus will arrive soon.

    Iqa   ke   tusvo  yipox  et   capatil.
    That  one  bus    soon   FUT  arrive-3S.
    The 1 bus will arrive soon.


<a id="org43bf3b7"></a>

## Verbs, Part 2 &#x2013; Tense, Aspect, Degree, and Reversal

Perflontus expresses two non-present tenses, past and future; and two aspects,
imperfect and perfect. (Briefly, the imperfect aspect indicates that the verb
action is ongoing or otherwise incomplete; the perfect aspect indicates that the
verb action has concluded.) These expressions appear as proclitics, i.e. prefix
particles.

    | Present         | --       | Elaiza zumatuz.      | Eliza sleeps.           |
    | Past (PST)      | im       | Elaiza im zumatuz.   | Eliza slept.            |
    | Future (FUT)    | et       | Elaiza et zumatuz.   | Eliza will sleep.       |
    |-----------------+----------+----------------------+-------------------------|
    | Imperfect (IMP) | av / -av | Elaiza av zumatuz.   | Eliza is sleeping.      |
    |                 |          | Elaiza imav zumatuz. | Eliza was sleeping.     |
    |                 |          | Elaiza etav zumatuz. | Eliza will be sleeping. |
    |-----------------+----------+----------------------+-------------------------|
    | Perfect (PRF)   | or / -or | Elaiza or zumatuz.   | Eliza has slept.        |
    |                 |          | Elaiza imor zumatuz. | Eliza had slept.        |
    |                 |          | Elaiza etor zumatuz. | Eliza will have slept.  |

Verbs may be modified in degree or even reversed by the use of a prefix:

    |                    | Alpoxe horwmod.   | I remember that time.             |
    | Diminutive (DIM)   | Alpoxe yihorwmod. | I remember that time (a bit).     |
    | Augmentative (AUG) | Alpoxe aghorwmod. | I remember that time (intensely). |
    | Reverse (REV)      | Alpoxe vohorwmod. | I forget that time.               |

If multiple prefixes are used, DIM/AUG come before REV, i.e. `yivohor*od`, not
`voyihor*od`.


<a id="org815145d"></a>

## Nouns and Adjectives, Part 1 &#x2013; Number

Perflontic nouns always have at least two syllables (which is to say, vowels)
and always end in a vowel other than `w`. In their noun form, they don't take any
interesting inflections other than for number. When a noun is given the dual
number its final vowel is replaced by `w`. For the plural number, it is replaced
by `wa`. Zero is considered to be part of the plural number.

    Furedu  toreli  wlatoc.
    Fred    cookie  eat-3S.
    Fred eats (a) cookie.

    Ha   torelw     wlatoc.
    Two  cookie-DU  eat-3S.
    He eats two cookies.

    Hasa   pagke  torelwa    wlatoc.
    2*216  25     cookie-PL  eat-3S.
    He eats 461 cookies.

Nouns also function as adjectives with no additional inflection. Some root forms
are translated as one part of speech or the other in English, but the parts of
speech in Perflontus should be understood as interchangeable as appropriate.

Adjectives take on the numeric inflection of the nouns they modify. In addition,
adjectives may be negated by infixing `-ay-` before their final vowel.

    Jekobu  kolbao  toreli  wlatoc.
    Jakob   green   cookie  eat-3S.
    Jakob eats (a) green cookie.

    Jekobu  ha   kolbaw    torelw     wlatoc.
    Jakob   two  green-DU  cookie-DU  eat-3S.
    Jakob eats two green cookies.

    Jekobu  kolba[ay]wa   torelwa    wlateyoc.
    Jakob   green-NEG-PL  cookie-DU  eat-3S-NEG.
    Jakob does not eat non-green cookies.

Note that numbers (like `ha` "two" in the second example) are an exception to
this. They do not generally take on the same numeric inflection as the objects
they count, but might still be pluralized in cases where they are used as
estimation units (e.g. `yo torelwa` "36 cookies" vs `ywa torelwa` "36s of cookies").


<a id="orgcab24fd"></a>

## Verbs, Part 3 &#x2013; To Be

Perflontus has only one irregular verb, the copula `az` "to be". When inflected as
a main verb, `az` is inflected as `z*`:

    | z[wm] | z[at] | z[ad]    | z[at][ey] |
    | I am  | It is | They are | It is not |

It is possible for `az` to take an object "infix" in this form, e.g. `zateyot` "It
is not it", but it's unclear whether this is formally correct. A good example of
this issue is the use of "It is I" vs "It is me" in English, which raises
questions of whether the things linked by the copula should both have subjective
case and so forth. In other words, the use of `az` in these cases is undecided,
but the above object-free examples should be enough to get you through a lot of
use cases.

`az` is only "to be" in the strictly copular sense, i.e. one that expresses some
sort of identity relation. Separate verbs are used for other meanings that have
been folded into the English "to be", e.g. `z*if` "to be located", `j*if` "to
exist".

When `az` links to a negative noun/adjective, it also takes on a negative
inflection. This mirroring only happens for `az`, and only when the modifier in
question is the negative inflection; in particular, it does not also happen for
diminutive `yi-` nor reversal `vo-`.

    Didi  ruzeqo  zat.
    Didi  hungry  be-3S.

    Didi  ruzeq[ay]o  zat[ey].
    Didi  hunger-NEG  be-3S-NEG.


<a id="org052d0dd"></a>

## Nouns and Adjectives, Part 2 &#x2013; Verb-Derivation

Verbs may be suffixed to form nouns. These suffixes are applied to the root form
of the verb, including `az`. They are compatible with all the affixes described
previously, except for the pronoun infixes. The resulting noun/adjective is
considered a root form unto itself, so that inflections like `-ay-` that target
the final vowel of the word apply to the final vowel of the verb+suffix, not the
final vowel of the root verb.

    | Suffix type      | Noun sense                  | Adjective sense         | Suffix | Example              |
    |------------------+-----------------------------+-------------------------+--------+----------------------|
    | Gerund (GER)     | The act of X-ing            | In the process of X-ing | -a     | daxa "teaching"      |
    | Agent (AGT)      | A thing that X's            | Capable of X-ing        | -afe   | daxafe "teacher"     |
    | Patient (PAT)    | A thing that is X'd         | X-able                  | -who   | daxwho "student"     |
    | Instrument (INS) | A thing that enables X-ing  | X-assisting, for X-ing  | -aqo   | daxaqo "educational" |
    | Location (LOC)   | A place where X-ing happens | X-hosting               | -ice   | daxice               |
    | Cause (CAU)      | A thing that causes X-ing   | X-causing               | -ede   | daxede               |

It should be noted that the use of these suffixes should be taken very
literally, which is one of the reasons that many suffixes will not have a clean
gloss into English. For example, it may be tempting to gloss `daxice`
"teach-location" as "school" but you could just as easily interpret that as
"classroom". The best you can really do is just substitute "teaching-place"
where it appears to avoid carrying in any unmerited assumptions. Thus to specify
"school" you might have to say `daxice veonxi` "teaching-place building" as
opposed to `daxice jiso` "teaching-place room". Of course, Perflontus should
ultimately have root words for "school" and "classroom" directly.


<a id="org2024836"></a>

### Gerund Case `-a`

The gerund case of a verb is a derived noun meaning that verb's action. Some
uses of the infinitive in various languages also perform this role; in
Perflontus the two both use the gerund case.

    Zumuz[a]   Qarluz   somatun.
    sleep-GER  Charles  please-3P.
    Sleeping/to sleep pleases Charles. (Charles likes sleeping/to sleep.)

When used as an adjective this case always functions as a present participle,
and only with the connotation of a thing that is performing the action in
question. In particular, when describing something that is used *for* an action
rather than something that is performing the action itself, use the Instrumental
Case.

    Qarluz   eqa   zumuza     hie    zat.
    Charles  that  sleep-GER  human  be-3P.
    Charles is the sleeping person.

    *Zumuza     kworu    kworatem.  -- Incorrect, the clothes are *for* sleeping
    *sleep-GER  clothes  wear-3P
    He wears clothes that are sleeping.  -- unless the clothes are alive???

    Zumuzaqo   kworu    kworatem.
    sleep-INS  clothes  wear-3P
    He wears clothes that are for sleeping.


<a id="org1678c83"></a>

### Agent Case `-afe`


<a id="org6d02fc0"></a>

### Patient Case `-who`


<a id="orgdcb5b35"></a>

### Instrumental Case `-aqo`


<a id="orgee1bfc2"></a>

### Locative Case `-ice`


<a id="orgd1e75da"></a>

### Causative Case `-ede`
