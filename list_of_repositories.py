import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

import requests

# Constants
GITHUB_TOKEN = 'your_personal_access_token'
ORG_NAME = 'your_organization_name'
API_URL = 'https://your-github-url/api/v3'

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def list_repositories():
    # Initialize variables
    repos = []
    page = 1

    # Fetch all repositories
    while True:
        response = requests.get(f'{API_URL}/orgs/{ORG_NAME}/repos?type=all&page={page}', headers=headers)
        
        if response.status_code != 200:
            print(f"Failed with status code {response.status_code}")
            print(response.text)
            break

        data = response.json()

        if not isinstance(data, list):
            print("Unexpected response format:")
            print(data)
            break

        if not data:
            break
        repos.extend([repo['name'] for repo in data])
        page += 1

    return repos

repositories = list_repositories()

with open("repositories.txt", "w") as file:
    for repo in repositories:
        file.write(repo + '\n')

print(f"Repositories have been saved to 'repositories.txt'. Total: {len(repositories)}")
