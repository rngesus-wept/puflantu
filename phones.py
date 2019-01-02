import random
import re


CONSONANTS = "bcdfghjklmnpqrstvxyz'"
VOWELS = "aeiouw"
STARTS = "bcdfhjkpqstvxz'"
LIQUIDS = "lr"

CONS_RE = re.compile('[{}]'.format(CONSONANTS), re.I)
VOWEL_RE = re.compile('[{}]'.format(VOWELS), re.I)

# This regex is for syllable splitting. It breaks up the word at letter
# boundaries except when it's able to identify the beginning of a syllable.
MAGIC_RE = re.compile('((?:[{}][{}]|[{}])?[{}]|)'.format(
    STARTS, LIQUIDS, CONSONANTS, VOWELS), re.I)


def GenerateSyllable():
  type_rng = random.random()
  syllable = []
  if type_rng < .625:
    if type_rng < .2:
      syllable.append(random.choice(STARTS))
      syllable.append(random.choice(LIQUIDS))
    else:
      syllable.append(random.choice(CONSONANTS))
  syllable.append(random.choice(VOWELS))
  if type_rng >= .375:
    syllable.append(random.choice(CONSONANTS))
  return ''.join(syllable)


def GenerateWord():
  length_rng = random.choices([1, 2, 3], weights=[.1, .6, .3])[0]
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
  return syllables


if __name__ == '__main__':
  for _ in range(10):
    print(re.sub('([{}][{}]?)$'.format(VOWELS, CONSONANTS), r'*\1',
                 GenerateWord(), flags=re.I))
