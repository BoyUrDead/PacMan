import requests
from bs4 import BeautifulSoup

def get_trending_repos():
    url_to_call = "https://github.com/trending"

    response = requests.get(url_to_call, headers={'User-Agent': 'Mozilla/5.0'})

    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all_trending_repos = dom.select("article.Box-row h1")

    trending_repositories = []
    for each_trending_repo in all_trending_repos:
        href_link = each_trending_repo.a.attrs["href"]
        name = href_link[1:]
        repo = {"label": name,
                "link": "https://github.com{}".format(href_link)}
        trending_repositories.append(repo)
    return trending_repositories
