import sys

from pybloom import ScalableBloomFilter

import morphemes
import phones


KNOWN_COLLISIONS = set()
EXPANDED_LEXICON = ScalableBloomFilter(initial_capacity=1000, error_rate=.001)


def TestUniqueness(word):
  if EXPANDED_LEXICON.add(word) and word not in KNOWN_COLLISIONS:
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
  # Load inflections that are known to cause bloom filter collisions but are
  # actually okay
  try:
    with open('verb_collisions.tsv', 'r') as f:
      for line in f:
        if not line.strip() or line.startswith('#'):
          continue
        KNOWN_COLLISIONS.add(line.strip().lower())
  except FileNotFoundError:
    pass

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

      for _, inflected_verb, _ in verb.Inflections(exclude_clitics=True, debug=debug):
        if debug:
          continue
        errors += (1 - TestUniqueness(inflected_verb))
        errors += (1 - TestSyllabification(inflected_verb))
        count += 2

  return errors, count

def main(args):
  errors, count = 0, 0

  debug = args[1] if len(args) > 1 else None

  verb_errors, verb_count = TestVerbs(debug=debug)
  errors += verb_errors
  count += verb_count

  if count:
    print('Caught {} errors out of {} checks.'.format(verb_errors, verb_count),
          file=sys.stderr)



if __name__ == '__main__':
  main(sys.argv)
