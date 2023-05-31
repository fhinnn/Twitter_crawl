import snscrape.modules.twitter as sntwitter
import csv

def crawl_twitter_hashtag(hashtag, num_tweets, start_date, end_date, output_file):
    query = f'{hashtag} since:{start_date} until:{end_date}'
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append(tweet.rawContent)
        if len(tweets) >= num_tweets:
            break

    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Tweet'])
        for tweet in tweets:
            writer.writerow([tweet])

crawl_twitter_hashtag("pemilu", 10000, '2021-01-01', '2023-12-31', 'output.csv')
