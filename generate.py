import phones
import morphemes

def main():
  verbs = {}
  with open('root_verbs.tsv', 'r') as f:
    for line in f:
      if not line.strip() or line.startswith('#'):
        continue
      root, meaning = line.strip().split('\t')
      if '/' in root:
        lemma, template = root.split('/')
        verbs[lemma] = morphemes.VerbLemma(lemma, meaning, template=template)
      else:
        verbs[root] = morphemes.VerbLemma(root, meaning)
  for v in verbs:
    print(verbs[v].SampleInflection())


if __name__ == '__main__':
  main()
