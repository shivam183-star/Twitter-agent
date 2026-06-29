import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def extract_image(article_url):

    try:

        response = requests.get(
            article_url,
            headers=HEADERS,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        og = soup.find("meta", property="og:image")

        if og:

            return og["content"]

    except Exception as e:

        print("Image Extraction Error:", e)

    return None