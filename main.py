import snscrape.modules.twitter as sntwitter
import pandas as pd
import os.path

def crawl_twitter_hashtag(num_tweets, start_date, end_date):
    hashtags = input("Masukkan hashtag yang akan dicari (pisahkan dengan koma jika lebih dari satu): ")
    hashtags = [tag.strip() for tag in hashtags.split(",")]

    output_file = 'hasil/pilkada.csv'
    csv_exists = os.path.isfile(output_file)
    tweet_ids = set()

    for hashtag in hashtags:
        query = f'{hashtag} since:{start_date} until:{end_date}'
        try:
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                if any(tag.lower() in tweet.rawContent for tag in hashtags):
                    tweet_data = {
                        'ID': tweet.id,
                        'Tweet': tweet.rawContent,
                        'Tanggal': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
                        'Lokasi': tweet.place.fullName if tweet.place is not None else None,
                        'Bahasa': tweet.lang
                    }

                    if tweet.lang == 'in' and tweet.id not in tweet_ids:
                        df = pd.DataFrame([tweet_data])
                        df.to_csv(output_file, mode='a', header=not csv_exists, index=False, sep=';', encoding='utf-8-sig')
                        csv_exists = True
                        tweet_ids.add(tweet.id)

                    if len(tweet_ids) >= num_tweets:
                        break

        except Exception as e:
            print(f"Error: {str(e)}")

num_tweets = 50000000
start_date = '2018-01-01'
end_date = '2019-06-05'

crawl_twitter_hashtag(num_tweets, start_date, end_date)

