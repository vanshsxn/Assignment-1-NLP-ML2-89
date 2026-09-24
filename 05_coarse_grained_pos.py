import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cat runs quickly."
doc = nlp(text)

print("Coarse-Grained POS Tags:")

for token in doc:
    print(token.text, "->", token.pos_)
