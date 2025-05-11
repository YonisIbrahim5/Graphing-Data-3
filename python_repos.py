import requests

url="https://api.github.com/search/repositories"

url += "?q=language:python+sort:stars+start:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print (f'Status Code: (response.status_code)')
response_dict = response.json()

print(f"Total Repo: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print (f"Repositories returned: {len(response_dict)}")

for repo_dict in repo_dicts:
    print(f"Total Keys: {len (repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)