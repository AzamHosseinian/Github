from github import Github

# Configuration
GITHUB_URL = 'https://your-github-url/api/v3'
TOKEN = 'your_personal_access_token'  # Ensure token has sufficient permissions
SOURCE_ORG = 'your_organization'

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

# Initialize branch counter
total_branch_count = 0

# Loop through each repository in the organization
for repo in source_org.get_repos():
    # Count the branches in this repository
    branch_count = repo.get_branches().totalCount
    print(f"Repository '{repo.name}' has {branch_count} branches.")
    total_branch_count += branch_count

# Print the total count of branches in the organization
print(f"Total branches in the organization: {total_branch_count}")
