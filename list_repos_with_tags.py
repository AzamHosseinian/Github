from github import Github

# Configuration
GITHUB_URL = 'https://your-github-enterprise-url/api/v3'
TOKEN = 'your_personal_access_token'  # Ensure token has sufficient permissions
SOURCE_ORG = 'your_source_organization'
OUTPUT_FILE = 'repos_with_tags.txt'  # Output file to write repository names and tags

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

# Open a file to write the repository names and tags
with open(OUTPUT_FILE, 'w') as file:
    for repo in source_org.get_repos():
        tags = list(repo.get_tags())
        if len(tags) > 0:
            file.write(f"Repository '{repo.name}' has {len(tags)} tags:\n")
            for tag in tags:
                file.write(f"    - {tag.name}\n")
            file.write("\n")  # Add a newline for better readability between repositories

print(f"Repositories with tags have been written to {OUTPUT_FILE}.")
