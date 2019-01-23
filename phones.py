import random
import re


CONSONANTS = "bcdfghjklmnpqrstvxyz'"
VOWELS = "aeiouw"

CONS_RE = re.compile('[{}]'.format(CONSONANTS), re.I)
VOWEL_RE = re.compile('[{}]'.format(VOWELS), re.I)

# This regex is for syllable splitting. It breaks up the word at letter
# boundaries except when it's able to identify the beginning of a syllable.
MAGIC_RE = re.compile('((?:[{}])?[{}]|)'.format(CONSONANTS, VOWELS), re.I)


def GenerateSyllable():
  type_rng = random.random()
  syllable = []
  if type_rng < .625:
    syllable.append(random.choice(CONSONANTS))
  syllable.append(random.choice(VOWELS))
  if type_rng >= .375:
    syllable.append(random.choice(CONSONANTS))
  return ''.join(syllable)


def GenerateWord():
  length_rng = random.choices([1, 2, 3, 4], weights=[.1, .5, .3, .1])[0]
  return ''.join(GenerateSyllable() for _ in range(length_rng))


def SyllableSplit(word):
  syllables = [_ for _ in re.split(MAGIC_RE, word) if _]
  # Attach any remaining singleton consonants to the preceding group
  position = 0
  while position < len(syllables) - 1:
    if syllables[position + 1] in CONSONANTS:
      syllables[position] += syllables[position + 1]
      del syllables[position + 1]
    position += 1
  assert all(re.match('^[{}]?[{}][{}]?$'.format(CONSONANTS, VOWELS, CONSONANTS),
                      syllable, re.I) for syllable in syllables), \
      '{} does not syllabize legally (C?VC?).'.format(repr(word.upper()))
  return syllables


if __name__ == '__main__':
  ## Execute this Python code on its own to just generate a bunch of
  ## phonetically valid words for brainstorming
  for _ in range(10):
    print('-'.join(SyllableSplit(GenerateWord())))
