from collections import OrderedDict as odict
import random
import re
import sys

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
                            self.template.replace('*', infixes) if infixes
                            else self.root,
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


# Maintain dictionaries of all the possible inflection parameter values
# This helps us do iteration and express certain morpheme choices more easily later
TENSES = odict({None: '', 'PST': 'im', 'FUT': 'et'})
ASPECTS = odict({None: '', 'IMP': 'av', 'PRF': 'uy'})
DEGREES = odict({None: '', 'AUG': 'ag', 'DIM': 'yi'})
INVERSION = odict({True: 'vo', False: ''})
VERB_POLARITIES = odict({None: '', 'NEG': 'ey'})
NOUN_POLARITIES = odict({None: '', 'NEG': 'ay'})
NOUN_SUFFIXES = odict({'AGT': 'afe', 'PAT': 'who', 'INS': 'aqo',
                       'LOC': 'ice', 'CAU': 'ede', 'GER': 'a'})
NOUN_CLASSES = [None, 'W', 'T', 'R']
NUMBERS = odict({None: '', 'DU': 'w', 'PL': 'wa'})
COMPARISONS = odict({None: '', 'CMP': "'", 'SUP': "'f"})
ADVERBIAL = odict({True: 'q', False: ''})
POSSESSIVE = odict({True: 're', False: ''})


class VerbLemma(Inflectable):
  """Manage inflections and derivations from a single verb form."""

  def __init__(self, lemma, gloss, template=None, derivative=False):
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
    self.derivative = derivative

  def GenerateProclitics(self, tense=None, aspect=None, **kwargs):
    result = [TENSES.get(tense, None), ASPECTS.get(aspect, None)]
    return [_ for _ in result if _]

  def GeneratePrefixes(self, degree=None, inverted=False, **kwargs):
    result = [DEGREES.get(degree, None), INVERSION.get(inverted, None)]
    return [_ for _ in result if _]

  def GenerateInfixes(self, subject=None, polarity=None, objekt=None, **kwargs):
    result = [GetPronoun(*subject) if subject else None,
              VERB_POLARITIES.get(polarity, None),
              GetPronoun(*objekt) if objekt else None]
    return [_ for _ in result if _]

  def GenerateSuffixes(self, nounify=None, **kwargs):
    result = [NOUN_SUFFIXES.get(nounify, None)]
    return [_ for _ in result if _]

  def Inflections(self, exclude_clitics=False, debug=None):
    """Generate all valid inflections.

    If a string is passed into debug, inflection parameters will be emitted to
    stderr whenever the input inflection is achieved.
    """
    for inverted in INVERSION:
      for degree in DEGREES:
        for polarity in VERB_POLARITIES:
          for subject in IterPronounArgs(case=['NOM']):
            if subject is None:
              continue
            for objekt in IterPronounArgs(case=['OBL']):
              for tense in ([None] if exclude_clitics else TENSES):
                for aspect in ([None] if exclude_clitics else ASPECTS):

                  kwargs = {'tense': tense, 'aspect': aspect,
                            'degree': degree, 'polarity': polarity,
                            'subject': subject, 'objekt': objekt,
                            'inverted': inverted, }
                  inflected_verb = self.Inflect(**kwargs)
                  if debug and inflected_verb[1].lower() == debug.lower():
                    # If the debug target is found, generate and output a gloss
                    gloss = '+'.join([_ for _ in [
                        self.gloss, tense, aspect, degree, polarity,
                        'INV' if inverted else '',
                        '-'.join(subject), '-'.join(objekt) if objekt else '']
                                      if _])
                    print(gloss, file=sys.stderr)
                  yield inflected_verb

          if not self.derivative:
            for nounify in NOUN_SUFFIXES:
              for noun_inflection in NounLemma(
                  self.Inflect(inverted=inverted, polarity=polarity,
                               degree=degree, nounify=nounify)[1],
                  '+'.join([_ for _ in [self.gloss, 'INV' if inverted else '',
                                        degree, polarity, 'N', nounify] if _]),
                  derivative=True).Inflections(exclude_clitics=exclude_clitics,
                                               debug=debug):
                # Debug targetting for nouns is passed down to the NounLemma layer
                yield noun_inflection

  def SampleInflection(self):
    kwargs = {}
    kwargs['inverted'] = random.choices([True, False], [.2, .8])[0]
    kwargs['degree'] = random.choices(list(DEGREES), [.8, .1, .1])[0]
    kwargs['polarity'] = random.choices(list(POLARITIES), [.75, .25])[0]
    if random.random() < .7:
      # Verb
      kwargs.update({
        'tense': random.choices(list(TENSES), [.6, .2, .2])[0],
        'aspect': random.choices(list(ASPECTS), [.6, .2, .2])[0],
        'subject': (random.choices(['1', '2', '3', 'REL'], [.3, .3, .3, .1])[0],
                    random.choices(['SG', 'DU', 'PL'], [1, 1, 1])[0], 'NOM')
        })
      if random.random() < .5:
        kwargs['objekt'] = (random.choices(['1', '2', '3', 'REL'], [.3, .3, .3, .1])[0],
                            random.choices(['SG', 'DU', 'PL'], [1, 1, 1])[0], 'OBL')
    else:
      # Noun
      kwargs['nounify'] = random.choices(list(NOUN_SUFFIXES), [1, 1, 1, 1, 1, 1])[0]
    return (self.Inflect(**kwargs), kwargs)


class NounLemma(Inflectable):
  """Manage inflections and derivations from a single noun form."""

  def __init__(self, lemma, gloss, template=None, derivative=False):
    assert lemma[-1] in phones.VOWELS, \
        'Noun form {} must end in a vowel.'.format(lemma.upper())
    assert lemma[-1] is not 'w', \
        'Root noun form {} must not end in "w".'.format(lemma.upper())
    assert len(phones.SyllableSplit(lemma)) >= 2, \
        'Noun form {} must have at least 2 syllables.'.format(lemma.upper())

    self.root = lemma[:-1]
    self.template = lemma[:-1] + '*'
    self.final_vowel = lemma[-1]
    self.gloss = gloss
    self.derivative = derivative

  def Inflect(self, klass=None, **kwargs):
    proclitics, main, enclitics = super().Inflect(**kwargs)

    ## Now do noun class things
    if klass == 'W':
      main = re.sub(r'([{}]+)[{}]*$'.format(phones.CONSONANTS, phones.VOWELS),
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

  def GenerateInfixes(self, polarity=None, **kwargs):
    result = [NOUN_POLARITIES.get(polarity, None)]
    return [_ for _ in result if _]

  def GenerateSuffixes(self, number=None, compare=None, adverbial=False, **kwargs):
    result = []
    if compare:
      result.append(self.final_vowel)
      result.append(COMPARISONS.get(compare))
    if number is None or number == 'SG':
      result.append('i' if compare == 'SUP' else self.final_vowel)
    else:
      result.append(NUMBERS.get(number))
    result.append(ADVERBIAL.get(adverbial, None))
    return [_ for _ in result if _]

  def GenerateEnclitics(self, possessive=None, **kwargs):
    result = [POSSESSIVE.get(possessive, None)]
    return [_ for _ in result if _]

  def Inflections(self, exclude_clitics=False, debug=None):
    """Generate all valid inflections.

    If a string is passed into debug, inflection parameters will be emitted to
    stderr whenever the input inflection is achieved.
    """
    for polarity in NOUN_POLARITIES:
      for klass in NOUN_CLASSES:
        for number in NUMBERS:
          for possessive in ([] if exclude_clitics else POSSESSIVE):
            kwargs = {'polarity': polarity, 'klass': klass,
                      'number': number, 'possessive': possessive}
            inflected_noun = self.Inflect(**kwargs)
            if debug and inflected_noun[1].lower() == debug.lower():
              # if the debug target is found, generate and output a gloss
              gloss = '+'.join([_ for _ in [
                  self.gloss, polarity, klass, number, 'POS' if possessive else '']
                                if _])
              print(gloss, file=sys.stderr)
            yield inflected_noun
          for compare in COMPARISONS:
            kwargs = {'polarity': polarity, 'klass': klass,
                      'number': number, 'compare': compare}
            inflected_noun = self.Inflect(**kwargs)
            if debug and inflected_noun[1].lower() == debug.lower():
              # if the debug target is found, generate and output a gloss
              gloss = '+'.join([_ for _ in [
                  self.gloss, polarity, klass, number, compare]
                                if _])
              print(gloss, file=sys.stderr)
            yield inflected_noun
      for compare in COMPARISONS:
        ## Adverbial
        kwargs = {'polarity': polarity, 'compare': compare}
        inflected_noun = self.Inflect(adverbial=True, **kwargs)
        if debug and inflected_noun[1].lower() == debug.lower():
          gloss = '+'.join([_ for _ in [
              self.gloss, polarity, compare, 'ADV']
                            if _])
          print(gloss, file=sys.stderr)
        yield inflected_noun


  def SampleInflection(self):
    """Output a randomly generated inflection of this word, including its parameters."""
    kwargs = {}
    kwargs['polarity'] = random.choices(list(POLARITIES), [.75, .25])[0]
    if random.random() < .1:
      kwargs['adverbial'] = True
      kwargs['compare'] = random.choices(list(COMPARISONS), [6, 1, 1])[0]
    else:
      kwargs['klass'] = random.choices(list(NOUN_CLASSES), [7, 1, 1, 1])[0]
      kwargs['number'] = random.choices(list(NUMBERS), [2, 1, 1])[0]
      kwargs['compare'] = random.choices(list(COMPARISONS), [6, 1, 1])[0]
      if kwargs['compare'] is None and random.random() < .1:
        kwargs['possessive'] = True
    return (self.Inflect(**kwargs), kwargs)


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
               ('REL', 'SG'): 'l', ('REL', 'DU'): 'r', ('REL', 'PL'): 'v'}[(person, number)]
  return vowel + consonant


def IterPronounArgs(person=None, number=None, case=None):
  yield None
  for p in person or ['1', '2', '3', 'REL']:
    for n in number or ['SG', 'DU', 'PL']:
      for c in case or ['NOM', 'OBL']:
        yield (p, n, c)


if __name__ == '__main__':
  ## For debugging purposes
  for proclitic, main, enclitic in NounLemma('riqwho', 'drinkable').Inflections(exclude_clitics=True):
    print(proclitic, main, enclitic)
