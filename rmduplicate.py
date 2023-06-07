import pandas as pd

def remove_duplicate_entries(input_file, output_file):
    df = pd.read_csv(input_file, sep=';', encoding='utf-8-sig')

    # Menghapus data duplikat berdasarkan kolom kedua
    df.drop_duplicates(subset=['Tweet'], keep='first', inplace=True)

    # Menyimpan dataframe ke file CSV baru
    df.to_csv(output_file, index=False, sep=';', encoding='utf-8-sig')

input_file = 'hasil/pilkada.csv'
output_file = 'hasil/pilkada_rev.csv'

remove_duplicate_entries(input_file, output_file)

print("Data duplikat pada kolom kedua telah dihapus dan file CSV baru telah dibuat.")
