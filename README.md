## Perezosa

The lazy way how to learn a language.

- Assumption 1: Learn only what is really used (useful).
- Assumption 2: Vocabulary isn't sufficient, learn grammar from ngrams.

This builds upon [NLTK](https://www.nltk.org/).

## Results

- stopwords
  - vocabulary: exclude them but study stopwords separately too
  - bigrams: filter out too common/meaningless pairs
  - trigrams+: filter out useful phrases, better keep them in
- ngram metrics
  - PMI (pointwise mutual information)
    - tried only for bigrams, results in lots of proper names (name+surname)
      not real grammatical phrases
  - raw_freq
    - good enough to score bigrams or higher ngrams
- vocabulary (unigrams)
  - how many words to learn to govern given proportion of the corpus (wiki)
    - 1.00: 770000
    - 0.95: 48226
    - 0.9: 17000
    - 0.8: 4000
- order of ngrams
  - bigrams show some common phrases but not complete grammar
  - trigrams show fragments of some grammar rules, but too short to capture it well
  - quadgrams -- no data, corpus too big to process (Python :-/)

## TODO

- ngram cummulative cropping
- stem vocabulary
- try spanning windows
- try bigger corpora (:=ditch NLTK)

## Dismissed

- Use NLTK Spanish corpora directly

