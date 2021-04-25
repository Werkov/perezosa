DATASET=wiki
SOURCE_wiki=../wiki.spa.txt

all: $(DATASET).vocab

$(eval SOURCE:=$$(SOURCE_$(DATASET)))

$(DATASET).vocab.bin: $(SOURCE)
	./train-vocabulary.py <$< >$@

$(DATASET).vocab: $(DATASET).vocab.bin
	./list-vocabulary.py $< >$@

