import snscrape.modules.twitter as sntwitter
import pandas as pd
import os.path

def crawl_twitter_hashtag(num_tweets, start_date, end_date):
    hashtags = input("Masukkan hashtag yang akan dicari (pisahkan dengan koma jika lebih dari satu): ")
    #hashtags = ["pemilu", "pilpres", "pileg", "capres"]
    hashtags = [tag.strip() for tag in hashtags.split(",")]

    tweets = []

    for hashtag in hashtags:
        query = f'{hashtag} since:{start_date} until:{end_date}'
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if any(tag.lower() in tweet.rawContent for tag in hashtags):
                tweet_data = {
                    'ID': tweet.id,
                    'Tweet': tweet.rawContent,
                    'Tanggal': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'Lokasi': tweet.place.fullName if tweet.place is not None else None
                }
                tweets.append(tweet_data)
                if len(tweets) >= num_tweets:
                    break

    if tweets:
        df = pd.DataFrame(tweets)
        output_file = f'hasil/endorsment.csv'
        if os.path.isfile(output_file):
            df.to_csv(output_file, mode='a', header=False, index=False, sep=';', encoding='utf-8-sig')
        else:
            df.to_csv(output_file, index=False, sep=';', encoding='utf-8-sig')

num_tweets = 100
start_date = '2022-01-01'
end_date = '2023-02-21'

crawl_twitter_hashtag(num_tweets, start_date, end_date)
