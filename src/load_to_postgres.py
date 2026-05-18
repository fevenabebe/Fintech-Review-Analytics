import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# Load CSV
# -----------------------------

df = pd.read_csv("data/final_reviews.csv")

# -----------------------------
# PostgreSQL connection
# -----------------------------

username = "postgres"
password = "12345678"
host = "localhost"
port = "5432"
database = "bank_reviews"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# -----------------------------
# Insert banks table
# -----------------------------

banks_df = pd.DataFrame({
    "bank_name": ["CBE", "BOA", "Dashen"],
    "app_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ]
})

banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

# -----------------------------
# Create bank_id mapping
# -----------------------------

bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

df["bank_id"] = df["bank"].map(bank_mapping)

# -----------------------------
# Keep required columns
# -----------------------------

reviews_df = df[
    [
        "review_id",
        "bank_id",
        "review_text",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
]

reviews_df = reviews_df.rename(columns={
    "date": "review_date"
})

# -----------------------------
# Insert reviews
# -----------------------------

reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully.")