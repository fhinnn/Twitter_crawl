import pandas as pd
import re

# Membaca dataset dari file CSV, pisahkan dengan tanda ";"
df = pd.read_csv('hasil/endorsement_rev.csv', delimiter=';')

# remove @ using regex
df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'@\w+', '', x))

# remove http using regex
df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'http\S+|www.\S+', '', x))

df.to_csv('regex/endorsement.csv', index=False)