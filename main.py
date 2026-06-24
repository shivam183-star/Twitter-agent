from news.fetcher import fetch_articles
from news.scorer import score_article
from ai.duplicate_checker import is_duplicate
from ai.tweet_writer import generate_tweet
from news.sender import send_message
import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

MINIMUM_SCORE = 8


def run_news_pipeline():
    logging.info("Agent started")

    print("\nFetching latest articles...\n")

    articles = fetch_articles()

    print(f"Found {len(articles)} articles\n")

    for article in articles:

        title = article["title"]
        summary = article["summary"]

        if len(summary) < 50:
            continue

        score = score_article(title, summary)

        print(f"Checking: {title}")
        print(f"Score: {score}")

        if score < MINIMUM_SCORE:
            continue

        if is_duplicate(title, summary):
            continue

        print("\nIMPORTANT ARTICLE FOUND\n")

        print(title)

        print("\nGenerating tweet...\n")

        tweet = generate_tweet(title, summary)

        if tweet:

            print("\nGenerated Tweet:\n")
            print(tweet)
            logging.info(f"Draft sent: {title}")

            message = f"""
HEADLINE

{title}

SCORE - {score}

SOURCE - {article['link']}

DRAFT TWEET

{tweet}
                """

            send_message(message)

            print("Draft sent to Telegram.")

            print("\nStopping after first valid article.")
            return

    print("\nNo suitable article found.")

run_news_pipeline()