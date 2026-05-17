import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(text):

    score = analyzer.polarity_scores(str(text))['compound']

    if score >= 0.05:
        label = 'POSITIVE'

    elif score <= -0.05:
        label = 'NEGATIVE'

    else:
        label = 'NEUTRAL'

    return label, score


def analyze_sentiment(df):

    df[['sentiment_label', 'sentiment_score']] = df['review'].apply(
        lambda x: pd.Series(classify_sentiment(x))
    )

    return df