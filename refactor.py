import csv

def rapikan_file_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        header = next(reader)  # Membaca baris header yang ada pada file
        header.extend(['id', 'tweet', 'tanggal', 'lokasi'])  # Menambahkan header baru

        for row in reader:
            id_value = row[0]  # Contoh: kolom ID berada pada indeks 0
            tweet_value = row[1]  # Contoh: kolom tweet berada pada indeks 1
            tanggal_value = row[2]  # Contoh: kolom tanggal berada pada indeks 2
            lokasi_value = row[3]  # Contoh: kolom lokasi berada pada indeks 3

            new_row = row + [id_value, tweet_value, tanggal_value, lokasi_value]  # Membuat baris baru dengan header tambahan
            data.append(new_row)

    with open(nama_file, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(header)  # Menulis header baru ke file CSV
        writer.writerows(data)  # Menulis data yang sudah diperbarui

    print("File CSV telah dirapikan!")

# Contoh penggunaan:
nama_file_csv = "hasil/pemilu.csv"  # Ganti dengan nama file CSV yang ingin dirapikan
rapikan_file_csv(nama_file_csv)

