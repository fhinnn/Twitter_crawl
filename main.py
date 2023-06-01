import snscrape.modules.twitter as sntwitter
import pandas as pd

def crawl_twitter_hashtag(num_tweets, start_date, end_date):
    hashtags = input("Masukkan hashtag yang akan dicari (pisahkan dengan koma jika lebih dari satu): ")
    hashtags = [tag.strip() for tag in hashtags.split(",")]

    for hashtag in hashtags:
        tweets = []

        query = f'{hashtag} since:{start_date} until:{end_date}'
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if any(tag.lower() in tweet.rawContent for tag in hashtags):
                tweet_data = {
                    'ID': tweet.id,
                    'Tweet': tweet.rawContent,
                    'Tanggal': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'Lokasi': tweet.place
                }
                tweets.append(tweet_data)
                if len(tweets) >= num_tweets:
                    break

        if tweets:
            df = pd.DataFrame(tweets)
            output_file = f'hasil/pemilu/{hashtag}.csv'
            df.to_csv(output_file, index=False)

num_tweets = 1000
start_date = '2022-01-01'
end_date = '2023-05-31'

crawl_twitter_hashtag(num_tweets, start_date, end_date)
