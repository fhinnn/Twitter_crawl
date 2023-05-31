import snscrape.modules.twitter as sntwitter
import pandas as pd

def crawl_twitter_hashtag(hashtags, num_tweets, start_date, end_date, output_file):
    tweets = []
    tweet_id = 1  # Inisialisasi ID tweet

    for hashtag in hashtags:
        query = f'{hashtag} since:{start_date} until:{end_date}'
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if any(tag.lower() in tweet.rawContent.lower() for tag in hashtags):
                tweet_data = {
                    'ID': tweet_id,
                    'Tweet': tweet.rawContent,
                    'Tanggal': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'Lokasi': tweet.place
                }
                tweets.append(tweet_data)
                tweet_id += 1
                if len(tweets) >= num_tweets:
                    break

    df = pd.DataFrame(tweets)
    df = df[['ID', 'Tweet', 'Tanggal', 'Lokasi']]  # Menentukan urutan kolom
    df.to_csv(output_file, index=False)

hashtags = [
    "Pemilu2024",
    "#PemiluLegislatif",
    "PemiluPresiden",
    "#Demokrasi",
    "#Politik",
    "PartaiPolitik",
    "#SuaraRakyat",
    "#PerubahanPolitik",
    "#CalonLegislatif",
    "CalonPresiden",
    "#Kampanye",
    "#DebatPublik",
    "#DebatPilpres",
    "#PemilihCerdas",
    "#HakPilih",
    "#DemokrasiIndonesia",
    "#PemiluSehat",
    "#PemiluDamai",
    "#TerkiniPemilu"
]

crawl_twitter_hashtag(hashtags, 200, '2021-01-01', '2023-12-31', 'hasil/pemilu/1.csv')
