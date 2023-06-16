import pandas as pd
import re

def remove_duplicate_entries(input_file, output_file):
    df = pd.read_csv(input_file, sep=';', encoding='utf-8-sig')
    df.drop_duplicates(subset=['Tweet'], keep='first', inplace=True)
    df.to_csv(output_file, index=False, sep=';', encoding='utf-8-sig')

def remove_by_regex(input_file):
    df = pd.read_csv('fix/pemilu.csv', delimiter=';')
    df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'@\w', '', x))
    df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'http\S+|www.\S+', '', x))
    df.to_csv('fix/pemilu.csv', index=False)

def main():
    input_file = 'hasil/pemilu_rev.csv'
    output_file = 'fix/pemilu.csv'

    remove_duplicate_entries(input_file, output_file)
    remove_by_regex(output_file)

if __name__== '__main__':
    main()


