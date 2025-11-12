import fasttext

model = fasttext.train_supervised(
    input="/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/train.txt",
    epoch=10,
    lr=0.5)

model.save_model("/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/classifiers/quality_classifier_model.bin")