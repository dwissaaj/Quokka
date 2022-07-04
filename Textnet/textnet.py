import textnets as tn
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")
tn.params["seed"] = 20
df = pd.read_excel("Book1.xlsx")
corpus = tn.Corpus.from_df(df, doc_col="text")
t = tn.Textnet(corpus.tokenized(),min_docs=1)
t.plot(label_nodes=True,
       show_clusters=True)
