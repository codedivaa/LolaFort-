import requests
from collections import Counter

TOKEN =""

headers = {
    "Authorization": f"token {TOKEN}"
}


def get_profile(username):
    url = f"https://api.github.com/users/{username}"
    return requests.get(url, headers=headers).json()


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    return requests.get(url, headers=headers).json()


def language_stats(repos):
    langs = []

    for repo in repos:
        if repo["language"]:
            langs.append(repo["language"])

    return Counter(langs)


def top_repositories(repos):
    sorted_repos = sorted(
        repos,
        key=lambda x: x["stargazers_count"],
        reverse=True
    )

    return sorted_repos[:5]


def developer_score(profile, repos):
    score = (
        profile["followers"] * 0.2
        + profile["public_repos"] * 2
    )

    return round(score)