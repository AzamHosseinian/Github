from github import Github

# Configuration
GITHUB_URL = 'https://your-github-url/api/v3'
TOKEN = 'your_personal_access_token'  # Ensure token has sufficient permissions
SOURCE_ORG = 'your_organization'
OUTPUT_FILE = 'repo_details.txt'  # Output file to write details

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

# Open a file to write the details
with open(OUTPUT_FILE, 'w') as file:
    total_branch_count = 0
    total_tag_count = 0  # Initialize total tag count

    # Loop through each repository in the organization
    for repo in source_org.get_repos():
        # Fetch branches
        branches = list(repo.get_branches())
        branch_count = len(branches)
        file.write(f"Repository '{repo.name}' has {branch_count} branches:\n")
        
        # List all branch names
        for branch in branches:
            file.write(f"    - {branch.name}\n")

        # Fetch tags
        tags = list(repo.get_tags())
        tag_count = len(tags)

        # Only write tag details if there are tags
        if tag_count > 0:
            file.write(f"Repository '{repo.name}' has {tag_count} tags:\n")
            for tag in tags:
                file.write(f"    - {tag.name}\n")
            total_tag_count += tag_count  # Add count of tags to total

        file.write("\n")  # Add a newline for better readability between repositories

    # Write the total counts of branches and tags in the organization
    file.write(f"Total branches in the organization: {total_branch_count}\n")
    file.write(f"Total tags in the organization: {total_tag_count}\n")  # Print total tags

print(f"Repository details including branches and tags have been written to {OUTPUT_FILE}.")
print(f"Total branches in the organization: {total_branch_count}")
print(f"Total tags in the organization: {total_tag_count}")  # Output total tags on console
