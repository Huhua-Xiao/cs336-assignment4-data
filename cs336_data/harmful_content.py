import fasttext


def identify_nsfw(text: str):
    model = fasttext.load_model("/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/classifiers/jigsaw_fasttext_bigrams_nsfw_final.bin")
    text_clean = text.replace("\n", " ").replace("\r", " ")
    prediction = model.predict(text_clean)
    label = prediction[0][0]
    label = label.replace("__label__", "")
    return label, float(prediction[1][0])

def identify_toxic_speech(text: str):
    model = fasttext.load_model("/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/classifiers/jigsaw_fasttext_bigrams_hatespeech_final.bin")
    text_clean = text.replace("\n", " ").replace("\r", " ")
    prediction = model.predict(text_clean)
    label = prediction[0][0]
    label = label.replace("__label__", "")
    return label, float(prediction[1][0])
