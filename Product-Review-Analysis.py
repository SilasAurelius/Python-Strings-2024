# Task 1: Keyword Highlighter: Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.

# Task 2: Sentiment Tally: Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.

# Task 3: Review Summary: Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def keyword_highlighter(reviews, keywords):
    review_highlighter = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        review_highlighter.append(review)
    return review_highlighter

def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        words = review.lower().split()
        for word in words:
            word = word.strip(".,!?\"")
            # I was getting the wrong positive/negative word count so I added the strip() to remove puncuation. This should give a more accurate match to the lists.
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
                
    return positive_count, negative_count

def review_summary(review):
    summary_length = 30
    if len(review) <= summary_length:
        return review
    else:
        summary = review[:summary_length]
        if summary[-1] != ' ':
            last_space = summary.rfind(' ')
            if last_space != -1:
                summary = summary[:last_space]
        return summary + "..."

highlighted_reviews = keyword_highlighter(reviews, keywords)
for review in highlighted_reviews:
    print(review)

positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print(f"Positive words: {positive_count}, Negative words: {negative_count}")

for review in reviews:
    print(review_summary(review))

