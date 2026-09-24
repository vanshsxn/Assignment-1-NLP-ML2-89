import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cat runs quickly."
doc = nlp(text)

print("Fine-Grained POS Tags:")

for token in doc:
    print(token.text, "->", token.tag_)
