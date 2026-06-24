KEYWORDS = {
    "war": 5,
    "military": 4,
    "missile": 5,
    "china": 4,
    "russia": 4,
    "india": 5,
    "taiwan": 5,
    "sanctions": 4,
    "nato": 4,
    "election": 3,
    "conflict": 5,
    "attacks": 5,
    "iran": 4,
    "israel": 4,
    "ukraine": 5,
    "ceasefire": 4,
    "trade": 2,
    "security": 3,
    "diplomatic": 3,
    "trump": 2,
    "putin": 3,
    "xi": 3,
    "tariff": 3,
    "usa": 5,
    "palestine": 5
}


def score_article(title, summary):

    score = 0

    combined = f"{title} {summary}".lower()

    for keyword, points in KEYWORDS.items():

        if keyword in combined:
            score += points

    return score