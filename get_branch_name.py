from github import Github

# Configuration
GITHUB_URL = 'https://your-github-url/api/v3'
TOKEN = 'your_personal_access_token'  # Ensure token has sufficient permissions
SOURCE_ORG = 'your_organization'
OUTPUT_FILE = 'branch_counts.txt'  # Output file to write branch counts

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

# Open a file to write the branch counts and names
with open(OUTPUT_FILE, 'w') as file:
    total_branch_count = 0

    # Loop through each repository in the organization
    for repo in source_org.get_repos():
        branches = list(repo.get_branches())
        branch_count = len(branches)
        file.write(f"Repository '{repo.name}' has {branch_count} branches:\n")

        # List all branch names
        for branch in branches:
            file.write(f"    - {branch.name}\n")

        total_branch_count += branch_count
        file.write("\n")  # Add a newline for better readability between repositories

    # Write the total count of branches in the organization
    file.write(f"Total branches in the organization: {total_branch_count}\n")

print(f"Branch counts and names have been written to {OUTPUT_FILE}.")
