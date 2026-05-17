from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(texts):

    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_features=20
    )

    X = vectorizer.fit_transform(texts.astype(str))

    keywords = vectorizer.get_feature_names_out()

    return keywords


def assign_theme(text):

    text = str(text).lower()

    if any(word in text for word in [
        'login', 'password', 'signin', 'account locked'
    ]):
        return 'Account Access Issues'

    elif any(word in text for word in [
        'slow', 'transfer', 'loading', 'transaction'
    ]):
        return 'Transaction Performance'

    elif any(word in text for word in [
        'otp', 'verification', 'code'
    ]):
        return 'Authentication Problems'

    elif any(word in text for word in [
        'fingerprint', 'feature', 'update', 'dark mode'
    ]):
        return 'Feature Requests'

    elif any(word in text for word in [
        'ui', 'design', 'easy', 'navigation'
    ]):
        return 'UI & User Experience'

    else:
        return 'Other'