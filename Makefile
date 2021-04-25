DATASET=wiki
SOURCE_wiki=../wiki.spa.txt

all: vocabulary ngrams
vocabulary: $(DATASET).vocab 
ngrams: $(DATASET).bigram

.PHONY: vocabulary ngrams
.DELETE_ON_ERROR:

$(eval SOURCE:=$$(SOURCE_$(DATASET)))

$(DATASET).tokens.bin: $(SOURCE)
	./mtokenize.py <$< >$@

$(DATASET).vocab.bin: $(DATASET).tokens.bin
	./train-vocabulary.py $< >$@

$(DATASET).vocab: $(DATASET).vocab.bin
	./list-vocabulary.py $< >$@

$(DATASET).bigram: $(DATASET).bigram.bin
	./list-ngram.py $< >$@

$(DATASET).bigram.bin: $(DATASET).tokens.bin
	./train-ngram.py $< >$@
