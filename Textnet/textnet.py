import textnets as tn
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")
tn.params["seed"] = 20
corpus = tn.Corpus(tn.examples.moon_landing)
t = tn.Textnet(corpus.tokenized(),min_docs=1)
t.plot(label_nodes=True,
       show_clusters=True)
t.save_graph("text.graphml")