-- Count reviews per bank
SELECT bank_name, COUNT(*) AS total_reviews
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY bank_name;

-- Average rating per bank
SELECT bank_name, AVG(rating) AS average_rating
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY bank_name;

-- Check for missing review text
SELECT COUNT(*) AS missing_reviews
FROM reviews
WHERE review_text IS NULL;

-- Check for missing sentiment labels
SELECT COUNT(*) AS missing_sentiment
FROM reviews
WHERE sentiment_label IS NULL;