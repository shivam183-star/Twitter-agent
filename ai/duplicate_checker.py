from __future__ import annotations

from typing import List

try:
    from rapidfuzz import fuzz
except ImportError:  # pragma: no cover
    fuzz = None


_stored_articles: List[str] = []

SIMILARITY_THRESHOLD = 75


def _normalize_text(text: object) -> str:
    return " ".join(str(text or "").split()).lower()


def _compute_similarity(text_a: str, text_b: str) -> int:
    if fuzz is not None:
        return fuzz.token_sort_ratio(text_a, text_b)

    from difflib import SequenceMatcher

    return int(SequenceMatcher(None, text_a, text_b).ratio() * 100)


def is_duplicate(title: object, summary: object, threshold: int = SIMILARITY_THRESHOLD) -> bool:
    content = _normalize_text(f"{title} {summary}")
    if not content:
        return False

    for old_content in _stored_articles:
        similarity = _compute_similarity(content, old_content)
        if similarity >= threshold:
            print(f"Duplicate detected ({similarity}%)")
            return True

    _stored_articles.append(content)
    return False


def clear_history() -> None:
    _stored_articles.clear()


def get_history() -> List[str]:
    return list(_stored_articles)


PROCESSED_FILE = "processed_articles.txt"
MAX_URLS = 1000

def already_processed(url):

    try:
        with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
            processed_urls = set(line.strip() for line in f)

        return url in processed_urls

    except FileNotFoundError:
        return False


def save_processed(url):

    try:
        with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f]

    except FileNotFoundError:
        urls = []

    urls.append(url)

    urls = urls[-MAX_URLS:]

    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(urls))