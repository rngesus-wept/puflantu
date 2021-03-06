"""Determine whether the current set of root forms collides with itself.

If provided with an argument, instead provides a definition for the word."""

import sys

from pybloom import ScalableBloomFilter

import morphemes
import phones


KNOWN_COLLISIONS = set()
EXPANDED_LEXICON = ScalableBloomFilter(initial_capacity=1000, error_rate=.001)


def TestUniqueness(word):
  if EXPANDED_LEXICON.add(word) and word.lower() not in KNOWN_COLLISIONS:
    # Word probably already exists
    print('{} may already exist in the lexicon.'.format(repr(word.upper())),
          file=sys.stderr)
    return False
  return True


def TestSyllabification(word):
  try:
    phones.SyllableSplit(word)
    return True
  except AssertionError as err:
    print(err, file=sys.stderr)
    return False


def TestVerbs(debug=None):
  errors, count = 0, 0

  with open('root_verbs.tsv', 'r') as f:
    for line in f:
      if not line.strip() or line.startswith('#'):  # comment syntax
        continue
      root, meaning = line.strip().split('\t')
      if '/' in root:  # indicator for irregularity
        lemma, template = root.split('/')
        verb = morphemes.VerbLemma(lemma, meaning, template=template)
      else:
        verb = morphemes.VerbLemma(root, meaning)

      for (_, inflected_verb, _), gloss in verb.Inflections(exclude_clitics=True):
        print('{:<32}{}'.format(inflected_verb, gloss))
        errors += (1 - TestUniqueness(inflected_verb))
        errors += (1 - TestSyllabification(inflected_verb))
        count += 2

  return errors, count


def TestNouns(debug=None):
  errors, count = 0, 0

  with open('root_nouns.tsv', 'r') as f:
    for line in f:
      if not line.strip() or line.startswith('#'):  # comment syntax
        continue
      root, meaning = line.strip().split('\t')
      noun = morphemes.NounLemma(root, meaning)

      for (_, inflected_noun, _), gloss in noun.Inflections(exclude_clitics=True, debug=debug):
        print('{:<32}{}'.format(inflected_noun, gloss))
        errors += (1 - TestUniqueness(inflected_noun))
        errors += (1 - TestSyllabification(inflected_noun))
        count += 2

  return errors, count


def LoadCollisions():
  # Load inflections that are known to cause bloom filter collisions but are
  # actually okay
  try:
    with open('collisions.tsv', 'r') as f:
      for line in f:
        if not line.strip() or line.startswith('#'):
          continue
        KNOWN_COLLISIONS.add(line.strip().lower())
  except FileNotFoundError:
    pass


def TestClosed(debug=None):
  errors, count = 0, 0

  with open('root_closed.tsv', 'r') as f:
    for line in f:
      if not line.strip() or line.startswith('#'):  # comment syntax
        continue
      word, meaning = line.strip().split('\t')
      print('{:<32}{}'.format(word, meaning))
      errors += (1 - TestUniqueness(word))
      errors += (1 - TestSyllabification(word))
      count += 2
  return errors, count


def TestAdverbs(debug=None):
  errors, count = 0, 0

  with open('root_adverbs.tsv', 'r') as f:
    for line in f:
      if not line.strip() or line.startswith('#'):  # comment syntax
        continue
      word, meaning = line.strip().split('\t')
      print('{:<32}{}'.format(word, meaning))
      errors += (1 - TestUniqueness(word))
      errors += (1 - TestSyllabification(word))
      count += 2
  return errors, count


def main(args):
  LoadCollisions()

  debug = [arg.lower() for arg in args[1:]] if len(args) > 1 else None

  closed_errors, closed_count = TestClosed(debug=debug)
  adverb_errors, adverb_count = TestAdverbs(debug=debug)
  verb_errors, verb_count = TestVerbs(debug=debug)
  noun_errors, noun_count = TestNouns(debug=debug)

  total_errors = sum([verb_errors, closed_errors, noun_errors])
  total_count = sum([verb_count, closed_count, noun_count])
  if total_count:
    print('Caught {} errors out of {} checks.'.format(total_errors, total_count),
          file=sys.stderr)


if __name__ == '__main__':
  main(sys.argv)
