import requests

url ="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000"

headers ={'Accept': 'application/vnd.github.v3+json'}
r= requests.get(url, headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(f"Total number of repositories: {response_dict['total_count']}")
print(f"Is it full answer?: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Number of returned repos: {len(repo_dicts)}")
repo_dict = repo_dicts[0]
print("\n Some information about chosen repo:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repo: {repo_dict['html_url']}")
    print(f"Created at: {repo_dict['created_at']}")
    print(f"Updated at: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print(f"\n Keys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)