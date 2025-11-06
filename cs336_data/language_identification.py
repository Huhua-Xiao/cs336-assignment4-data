import fasttext

model = fasttext.load_model("/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/classifiers/lid.176.bin")

def identify_language(text: str):
    text_clean = "".join(text.split())
    prediction = model.predict(text_clean)
    label = prediction[0][0]
    conf = float(prediction[1][0])
    lang_code = label.replace("__label__", "")

    return lang_code, conf