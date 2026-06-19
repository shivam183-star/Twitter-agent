from google import genai
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_tweet(title, summary):

    short_summary = summary[:500]

    prompt = f"""
    Write one short professional geopolitical news tweet.

    Rules:
    - Maximum 50 words
    - Neutral tone
    - No emojis
    - No hashtags
    - No markdown
    - No intro text
    - Sound like professional tweet

    Title:
    {title}

    Summary:
    {short_summary}
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if response.text:
            return response.text.strip()

        return None

    except Exception as e:
        traceback.print_exc()
        print(f"Gemini Error: {e}")

        return None
    


tweet = generate_tweet(
    "China expands military drills near Taiwan",
    "China increased naval activity near Taiwan amid rising regional tensions."
)

print(tweet)