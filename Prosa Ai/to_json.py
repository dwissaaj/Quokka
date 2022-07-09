import pandas as pd
df = pd.read_excel("act.xlsx")
with open('sa.json', 'w') as f:
    f.write(df['berita'].to_json(orient="records", lines=True))
