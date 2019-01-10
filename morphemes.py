from collections import OrderedDict as odict
import random
import re

import phones


class Inflectable(object):
  """Framework for managing a thing that can be inflected.

  If infixing is supported, the item must define a self.template containing
  exactly one asterisk to indicate the infix point."""
  def Inflect(self, **kwargs):
    proclitics = ''.join(self.GenerateProclitics(**kwargs))
    prefixes = ''.join(self.GeneratePrefixes(**kwargs))
    infixes = ''.join(self.GenerateInfixes(**kwargs))
    suffixes = ''.join(self.GenerateSuffixes(**kwargs))
    enclitics = ''.join(self.GenerateEnclitics(**kwargs))

    return (proclitics,
            '{}{}{}'.format(prefixes,
                            self.template.replace('*', infixes),
                            suffixes),
            enclitics)

  def GenerateProclitics(self, **kwargs):
    return []

  def GeneratePrefixes(self, **kwargs):
    return []

  def GenerateInfixes(self, **kwargs):
    return []

  def GenerateSuffixes(self, **kwargs):
    return []

  def GenerateEnclitics(self, **kwargs):
    return []


TENSES = odict({None: '', 'PST': 'im', 'FUT': 'et'})
ASPECTS = odict({None: '', 'IMP': 'av', 'PRF': 'uy'})
DEGREES = odict({None: '', 'AUG': 'ag', 'DIM': 'yi'})
INVERSION = odict({True: 'vo', False: ''})
POLARITIES = odict({None: '', 'NEG': 'ey'})
NOUN_SUFFIXES = odict({'AGT': 'afe', 'PAT': 'who', 'INS': 'aqo',
                       'LOC': 'ice', 'CAU': 'ede', 'GER': 'a'})

class VerbLemma(Inflectable):
  """Manage inflections and derivations from a single verb form."""


  def __init__(self, lemma, gloss, template=None):
    assert lemma[-1] in phones.CONSONANTS, \
        'Verb form {} must end in a consonant.'.format(lemma.upper())

    self.root = lemma
    if template is None:
      self.template = re.sub('([{}][{}]?)$'.format(phones.VOWELS, phones.CONSONANTS),
                             r'*\1', lemma, flags=re.I)
    else:
      self.template = template
    assert len(self.template.split('*')) == 2, \
        'Template {} must contain exactly one "*".'.format(self.template.upper())
    self.gloss = gloss

  def GenerateProclitics(self, tense=None, aspect=None, **kwargs):
    result = [TENSES.get(tense, None), ASPECTS.get(aspect, None)]
    return [_ for _ in result if _]

  def GeneratePrefixes(self, degree=None, inverted=False, **kwargs):
    result = [DEGREES.get(degree, None), INVERSION.get(inverted, None)]
    return [_ for _ in result if _]

  def GenerateInfixes(self, subject=None, polarity=None, objekt=None, **kwargs):
    result = [GetPronoun(*subject) if subject else None,
              POLARITIES.get(polarity, None),
              GetPronoun(*objekt) if objekt else None]
    return [_ for _ in result if _]

  def GenerateSuffixes(self, nounify=None, **kwargs):
    result = [NOUN_SUFFIXES.get(nounify, None)]
    return [_ for _ in result if _]

  def Inflections(self):
    """Generate all valid inflections."""
    for tense in TENSES:
      for aspect in ASPECTS:
        for degree in DEGREES:
          for inverted in INVERSION:
            for subject in IterPronounArgs(case=['NOM']):
              if subject is None:
                continue
              for polarity in POLARITIES:
                for objekt in IterPronounArgs(case=['OBL']):
                  yield self.Inflect(tense=tense, aspect=aspect,
                                     degree=degree, polarity=polarity,
                                     subject=subject, objekt=objekt,
                                     inverted=inverted)

  def SampleInflection(self):
    if random.random() < .7:
      # Verb
      kwargs = {
        'tense': random.choices(list(TENSES), [.6, .2, .2])[0],
        'aspect': random.choices(list(ASPECTS), [.6, .2, .2])[0],
        'degree': random.choices(list(DEGREES), [.8, .1, .1])[0],
        'inverted': random.choices([True, False], [.2, .8])[0],
        'polarity': random.choices(list(POLARITIES), [.75, .25])[0],
        'subject': (random.choices(['1', '2', '3', 'REL'], [.3, .3, .3, .1])[0],
                    random.choices(['SG', 'DU', 'PL'], [1, 1, 1])[0], 'NOM')
        }
      if random.random() < .5:
        kwargs['objekt'] = (random.choices(['1', '2', '3', 'REL'], [.3, .3, .3, .1])[0],
                            random.choices(['SG', 'DU', 'PL'], [1, 1, 1])[0], 'OBL')
    else:
      # Noun
      kwargs = {
        'inverted': random.choices([True, False], [.2, .8])[0],
        'polarity': random.choices(list(POLARITIES), [.75, .25])[0],
        'nounify': random.choices(list(NOUN_SUFFIXES), [1, 1, 1, 1, 1, 1])[0]
        }
    return (self.Inflect(**kwargs), kwargs)


class NounLemma(Inflectable):
  """Manage inflections and derivations from a single noun form."""

  def __init__(self, lemma, gloss, template=None):
    assert lemma[-1] in phones.VOWELS, \
        'Noun form {} must end in a vowel.'.format(lemma.upper())
    assert lemma[-1] is not 'w', \
        'Root noun form {} must not end in "w".'.format(lemma.upper())
    assert len(phones.SyllableSplit(lemma)) >= 2, \
        'Noun form {} must have at least 2 syllables.'.format(lemma.upper())

    self.root = lemma
    self.template = lemma[:-1] + '*'
    self.final_vowel = lemma[-1]
    self.gloss = gloss

  def Inflect(self, klass=None, **kwargs):
    proclitics, main, enclitics = super().Inflect(**kwargs)

    ## Now do noun class things
    if klass == 'W':
      main = re.sub(r'([{}]+)[{}]?$'.format(phones.CONSONANTS, phones.VOWELS),
                      r'\1w\g<0>', main)
    elif klass == 'T':
      main = re.sub(r'^[{}]?([{}])'.format(phones.CONSONANTS, phones.VOWELS),
                      r'\1t\g<0>', main)
    elif klass == 'R':
      main_syl = phones.SyllableSplit(main)
      if main_syl[1][0] in phones.VOWELS:
        main_syl[1] = 'r' + main_syl[1]
      else:
        main_syl[1] = re.sub(phones.VOWEL_RE, r'ur\g<0>', main_syl[1])
      main = ''.join(main_syl)

    return proclitics, main, enclitics

  def GenerateInfixes(self, polarity=None):
    result = [POLARITIES.get(polarity, None)]
    return [_ for _ in result if _]

  def GenerateSuffixes(self, number=None, compare=None, adverb=None, **kwargs):
    result = []
    if compare:
      result.append(self.final_vowel)
      result.append({'CMP': "'", 'SUP': "'f"}.get(compare))
    if number is None or number == 'SG':
      result.append('i' if compare == 'SUP' else self.final_vowel)
    else:
      result.append({'DU': 'w', 'PL': 'wa'}[number])
    if adverb:
      result.append('q')
    return result

  def GenerateEnclitics(self, possessive=None, **kwargs):
    result = []
    if possessive:
      result.append('re')
    return result


def GetPronoun(person,  # 1, 2, 3, or REL
               number,  # SG, DU, or PL
               case):   # NOM or OBL
  vowel = {('1', 'NOM'): 'w', ('1', 'OBL'): 'u',
           ('2', 'NOM'): 'i', ('2', 'OBL'): 'e',
           ('3', 'NOM'): 'a', ('3', 'OBL'): 'o',
           ('REL', 'NOM'): 'a', ('REL', 'OBL'): 'o'}[(person, case)]
  consonant = {('1', 'SG'): 'm', ('1', 'DU'): 'n', ('1', 'PL'): 'y',
               ('2', 'SG'): 'z', ('2', 'DU'): 'j', ('2', 'PL'): 'x',
               ('3', 'SG'): 't', ('3', 'DU'): 'b', ('3', 'PL'): 'd',
               ('REL', 'SG'): 'l', ('REL', 'DU'): 'r', ('REL', 'PL'): 'ry'}[(person, number)]
  return vowel + consonant


def IterPronounArgs(person=None, number=None, case=None):
  yield None
  for p in person or ['1', '2', '3', 'REL']:
    for n in number or ['SG', 'DU', 'PL']:
      for c in case or ['NOM', 'OBL']:
        yield (p, n, c)


if __name__ == '__main__':
  for _ in range(10):
    print(VerbLemma('riq', 'drink').SampleInflection())
  # for proclitic, main, enclitic in VerbLemma('riq', 'drink').Inflections():
  #   print('{}{}{}'.format((proclitic + ' ') if proclitic else '',
  #                         main,
  #                         ('-' + enclitic) if enclitic else ''))
