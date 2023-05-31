import snscrape.modules.twitter as sntwitter
import csv

def crawl_twitter_hashtag(hashtags, num_tweets, start_date, end_date, output_file):
    tweets = []

    for hashtag in hashtags:
        query = f'{hashtag} since:{start_date} until:{end_date}'
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if any(tag.lower() in tweet.content.lower() for tag in hashtags):
                tweets.append(tweet.content)
                if len(tweets) >= num_tweets:
                    break

    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Tweet'])
        for tweet in tweets:
            writer.writerow([tweet])

hashtags = ["#Pemilu"
#"#Pemilu2024",
#"#PemiluLegislatif",
#"#PemiluPresiden",
#"#Demokrasi",
#"#Politik",
#"#PartaiPolitik",
#"#SuaraRakyat",
#"#PerubahanPolitik",
#"#CalonLegislatif",
#"#CalonPresiden",
#"#Kampanye",
#"#DebatPublik",
#"#DebatPilpres",
#"#PemilihCerdas",
#"#HakPilih",
#"#DemokrasiIndonesia",
#"#PemiluSehat",
#"#PemiluDamai",
#"#TerkiniPemilu"
]

crawl_twitter_hashtag(hashtags, 400, '2021-01-01', '2023-12-31', 'hasil/pemilu/1.csv')
