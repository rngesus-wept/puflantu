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

    return '{}{}{}{}{}'.format(proclitics, prefixes,
                               self.template.replace('*', infixes),
                               suffixes, enclitics)

  def GenerateProclitics(self, **kwargs):
    pass

  def GeneratePrefixes(self, **kwargs):
    pass

  def GenerateInfixes(self, **kwargs):
    pass

  def GenerateSuffixes(self, **kwargs):
    pass

  def GenerateEnclitics(self, **kwargs):
    pass


class VerbLemma(Inflectable):
  """Manage inflections and derivations from a single verb form."""

  def __init__(self, lemma, gloss, template=None):
    assert lemma[-1] in phones.CONSONANTS, \
        'Verb form {} must end in a consonant'.format(lemma.upper())

    self.root = lemma
    if template is None:
      self.template = re.sub('([{}][{}]?)$', r'*\1', lemma, flags=re.I)
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


def GetPronoun(person,  # 1, 2, 3, or REL
               number,  # SG, DU, or PL
               case):   # NOM or ACC
  vowel = {('1', 'NOM'): 'w', ('1', 'ACC'): 'u',
           ('2', 'NOM'): 'i', ('2', 'ACC'): 'e',
           ('3', 'NOM'): 'a', ('3', 'ACC'): 'o',
           ('REL', 'NOM'): 'a', ('REL', 'ACC'): 'o'}[(person, case)]
  consonant = {('1', 'SG'): 'm', ('1', 'DU'): 'n', ('1', 'PL'): 'y',
               ('2', 'SG'): 'j', ('2', 'DU'): 'c', ('2', 'PL'): 'x',
               ('3', 'SG'): 't', ('3', 'DU'): 'b', ('3', 'PL'): 'd',
               ('REL', 'SG'): 'l', ('REL', 'DU'): 'r', ('REL', 'PL'): 'ry'}[(person, number)]
  return vowel + consonant
