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

    if proclitics:
      proclitics += ' '
    if enclitics:
      enclitics.insert(0, '-')

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


class VerbLemma(Inflectable):
  """Manage inflections and derivations from a single verb form."""

  def __init__(self, lemma, gloss, template=None):
    assert lemma[-1] in phones.CONSONANTS, \
        'Verb form {} must end in a consonant.'.format(lemma.upper())

    self.root = lemma
    if template is None:
      self.template = re.sub('([{}][{}]?)$'.format(phones.VOWELS, phones.CONSONANTS),
                             r'*\1', lemma, flags=re.I)
    assert len(template.split('*')) == 2, \
        'Template {} must contain exactly one "*".'.format(template.upper())
    self.gloss = gloss

  def GenerateProclitics(self, tense=None, aspect=None, **kwargs):
    result = [
        {'PST': 'im', 'FUT': 'et'}.get(tense, None),
        {'IMP': 'av', 'PRF': 'uy'}.get(kwargs.get('aspect', None), None),
      ]
    return [_ for _ in result if _ is not None]

  def GeneratePrefixes(self, degree=None, **kwargs):
    result = [
        {'AUG': 'ag', 'DIM': 'yi'}.get(degree, None),
      ]
    return [_ for _ in result if _ is not None]

  def GenerateInfixes(self, subject=None, polarity=None, objekt=None, **kwargs):
    result = []
    if subject:
      result.append(GetPronoun(*subject))
    if polarity == 'NEG':
      result.append('ey')
    if objekt:
      result.append(GetPronoun(*objekt))
    return result

  def GenerateSuffixes(self, nounify=None, **kwargs):
    result = [
        {'AGT': 'afe', 'PAT': 'who', 'INS': 'aqo',
         'LOC': 'ice', 'CAU': 'ede', 'GER': 'a'}.get(nounify, None),
      ]
    return [_ for _ in result if _ is not None]


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
               ('2', 'SG'): 'j', ('2', 'DU'): 'c', ('2', 'PL'): 'x',
               ('3', 'SG'): 't', ('3', 'DU'): 'b', ('3', 'PL'): 'd',
               ('REL', 'SG'): 'l', ('REL', 'DU'): 'r', ('REL', 'PL'): 'ry'}[(person, number)]
  return vowel + consonant


if __name__ == '__main__':
  water = NounLemma('enxa', 'water')
  moon = NounLemma('orqude', 'moon')
  print('{} {}'.format(water.Inflect(klass='T'), moon.Inflect(klass='T')))
  print('{} {}'.format(moon.Inflect(klass='R'), water.Inflect(klass='R')))
