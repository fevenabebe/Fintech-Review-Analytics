from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking'
}

# Replace with actual Dashen app id if different
apps['Dashen'] = 'com.dashen.dashenmobile'

all_reviews = []

for bank_name, app_id in apps.items():
    print(f"Scraping reviews for {bank_name}...")

    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:
        all_reviews.append({
            'review_id': review['reviewId'],
            'review': review['content'],
            'rating': review['score'],
            'date': review['at'],
            'bank': bank_name,
            'source': 'Google Play'
        })

# Convert to DataFrame
reviews_df = pd.DataFrame(all_reviews)

# Save raw data
reviews_df.to_csv('data/raw_reviews.csv', index=False)

print("Raw reviews saved successfully.")
print(reviews_df.head())