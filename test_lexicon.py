import sys

from pybloom import ScalableBloomFilter

import morphemes
import phones


EXPANDED_LEXICON = ScalableBloomFilter(initial_capacity=1000, error_rate=.001)


def TestUniqueness(word):
  if EXPANDED_LEXICON.add(word):
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


def main(args):
  errors, count = 0, 0

  verb = morphemes.VerbLemma('riq', 'drink')
  if len(sys.argv) > 1:
    for _ in verb.Inflections(exclude_clitics=True, debug=sys.argv[1]):
      pass
    return True

  for _, inflected_verb, _ in verb.Inflections(exclude_clitics=True):
    errors += (1 - TestUniqueness(inflected_verb))
    count += 1
    errors += (1 - TestSyllabification(inflected_verb))
    count += 1

  print('Caught {} errors out of {} checks.'.format(errors, count),
        file=sys.stderr)


if __name__ == '__main__':
  main(sys.argv)
