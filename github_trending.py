import requests
import datetime


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    date_boundary = datetime.date.today() - datetime.timedelta(days=7)

    params = {
        'q': 'created:>{}'.format(date_boundary.isoformat()),
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size,
    }
    response = requests.get(url, params=params)
    return response.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name,
    )
    params = {'state': 'open'}
    response = requests.get(url, params=params)
    return len(response.json())


if __name__ == '__main__':
    trending_repos = get_trending_repositories(20)
    for rank, repo in enumerate(trending_repos, 1):
        repo_name = repo['name']
        repo_owner = repo['owner']['login']
        stars_number = repo['stargazers_count']
        repo_url = repo['html_url']

        amount_of_issues = get_open_issues_amount(repo_owner, repo_name)
        print('{:2}. repo-owner: {}'.format(rank, repo_owner))
        print('\trepo-name: {}'.format(repo_name))
        print('\t{} stars'.format(stars_number))
        print('\t{} issues'.format(amount_of_issues))
        print('\t{}'.format(repo_url))
