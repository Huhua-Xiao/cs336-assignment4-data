###### wget the subsampled posotive URLS
wget --timeout=5 \
-i subsampled_positive_urls.txt \
--warc-file=subsampled_positive_urls \
-O /dev/null


# This will be much faster
wget \
  --tries=1 \
  --dns-timeout=2 \
  --connect-timeout=2 \
  --read-timeout=3 \
  --timeout=3 \
  --max-redirect=3 \
  --inet4-only \
  -i subsampled_positive_urls.txt \
  --warc-file=subsampled_positive_urls \
  -O /dev/null




###### Download negative sample warc file 
# 1) Download（warc.paths.gz）
wget https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/warc.paths.gz

# 2) pick the first path
FIRST_PATH=$(gunzip -c warc.paths.gz | head -n 1)

# 3) Download this warc file
wget "https://data.commoncrawl.org/${FIRST_PATH}"


###### Combined the train.txt
cat data/wiki/subsampled_positive_urls.txt data/webdata/negative_samples.txt > train.txt


###### Train fastText model
./fasttext supervised -input train.txt -output quality_classifier_model -epoch 10 -lr 0.5
