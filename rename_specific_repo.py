from github import Github

# Configuration
GITHUB_URL = 'https://your-github-enterprise-url/api/v3'
TOKEN = 'your_personal_access_token'
ORG_NAME = 'your_organization_name'
REPO_NAME = 'your_repository_name'
NEW_NAME = 'your_new_repository_name'

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the organization or user
org = g.get_organization(ORG_NAME) if ORG_NAME else g.get_user()
repo = org.get_repo(REPO_NAME)

# Rename the repository
repo.edit(name=NEW_NAME)

print(f"Repository renamed to {NEW_NAME}")
