import requests
import os


def download_image(image_url):

    if image_url is None:
        return None

    try:

        os.makedirs("temp", exist_ok=True)

        path = "temp/article.jpg"

        response = requests.get(
            image_url,
            timeout=15
        )

        with open(path, "wb") as f:
            f.write(response.content)

        return path

    except Exception as e:

        print("Download Error:", e)

        return None