from github import Github

# Configuration
GITHUB_TOKEN = 'your_personal_access_token'
GITHUB_URL = 'https://your-github-url/api/v3'  # Custom GitHub Enterprise API URL
ORGANIZATION_NAME = 'your_organization'

# List of repositories to delete
repos_to_delete = [
    "Repo1", "Repo2", "Repo3", "Repo4", "Repo5"  # Add your repository names here
]

# Connect to GitHub Enterprise with custom URL
g = Github(base_url=GITHUB_URL, login_or_token=GITHUB_TOKEN)

# Get the organization
org = g.get_organization(ORGANIZATION_NAME)

# Loop through the list of repositories to delete
for repo_name in repos_to_delete:
    try:
        # Get the repository object
        repo = org.get_repo(repo_name)
        # Delete the repository
        repo.delete()
        print(f"Repository '{repo_name}' has been deleted.")
    except Exception as e:
        print(f"Failed to delete repository '{repo_name}': {e}")
