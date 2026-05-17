import pandas as pd

# Load raw data
reviews_df = pd.read_csv('data/raw_reviews.csv')

print("Initial Shape:", reviews_df.shape)

# Remove duplicates
reviews_df.drop_duplicates(subset='review_id', inplace=True)

# Remove missing values
reviews_df.dropna(subset=['review', 'rating'], inplace=True)

# Convert dates
reviews_df['date'] = pd.to_datetime(reviews_df['date']).dt.strftime('%Y-%m-%d')

# Strip spaces
reviews_df['review'] = reviews_df['review'].astype(str).str.strip()

# Remove empty reviews
reviews_df = reviews_df[reviews_df['review'] != '']

print("Final Shape:", reviews_df.shape)

# Save cleaned data
reviews_df.to_csv('data/clean_reviews.csv', index=False)

print("Cleaned dataset saved successfully.")