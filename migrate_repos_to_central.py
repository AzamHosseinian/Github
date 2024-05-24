from github import Github
import subprocess
import os

# Configuration
GITHUB_URL = 'https://your-github-enterprise-url/api/v3'
TOKEN = 'your_personal_access_token'
SOURCE_ORG = 'your_source_organization'
TARGET_REPO_NAME = 'your_target_repository'

# List of repositories to process
repo_names = [
    "Repo1", "Repo2", "Repo3", "Repo4", "Repo5",  # Add your repository names here
    # ... more repository names
]

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

try:
    central_repo = source_org.get_repo(TARGET_REPO_NAME)
except Exception as e:
    print(f"Failed to find the central repository '{TARGET_REPO_NAME}': {e}")
    exit(1)

# Collect existing branches in the central repository to prevent conflicts
existing_branches = {branch.name for branch in central_repo.get_branches()}

# Loop through specified repositories in the source organization
for repo_name in repo_names:
    try:
        repo = source_org.get_repo(repo_name)
        clone_url = repo.clone_url.replace('https://', f'https://{TOKEN}@')
        print(f"Cloning repository {repo.name}...")
        subprocess.run(f"git clone {clone_url}", shell=True)

        # Change directory to the cloned repo
        os.chdir(repo.name)

        # Get the list of branches
        branches = subprocess.run("git branch -r", shell=True, capture_output=True, text=True).stdout
        branches = [line.strip().split('/')[-1] for line in branches.split('\n') if line.strip()]

        for branch in branches:
            if branch in existing_branches:
                print(f"Skipping branch {branch} as it already exists in the central repository.")
                continue
            
            # Checkout the branch
            subprocess.run(f"git checkout {branch}", shell=True)

            # Push the branch to the central repository
            push_command = f"git push {central_repo.clone_url.replace('https://', f'https://{TOKEN}@')} {branch}"
            print(f"Pushing branch {branch} to central repository...")
            subprocess.run(push_command, shell=True)

        # Change back to the original directory, but do not delete the cloned repository
        os.chdir('..')
    except Exception as e:
        print(f"Error processing repository {repo_name}: {e}")

print("All non-conflicting branches have been migrated to the central repository.")
