from github import Github
import subprocess
import os

# Configuration
GITHUB_URL = 'https://your-github-url/api/v3'
TOKEN = 'your_personal_access_token'
SOURCE_ORG = 'your_source_organization'
TARGET_ORG = 'your_target_organization'
TARGET_REPO_NAME = 'your_target_repository'  # Specific repository for pushing the branches
REPO_LIST = [
    'Repo1', 'Repo2', 
    'Repo3', 'Repo4'
]

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

# Get the target repository
try:
    target_org = g.get_organization(TARGET_ORG)
    target_repo = target_org.get_repo(TARGET_REPO_NAME)
except Exception as e:
    print(f"Failed to find target organization or repository: {e}")
    exit(1)

# Loop through all repositories in the source organization
for repo in source_org.get_repos():
    if repo.name not in REPO_LIST:
        continue  # Skip repositories not in the specified list

    new_repo_name = repo.name
    clone_url = repo.clone_url.replace('https://', f'https://{TOKEN}@')

    print(f"Creating and mirroring repository {new_repo_name}...")
    subprocess.run(f"git clone {clone_url}", shell=True)
    os.chdir(new_repo_name)
    
    # Rename and list branches
    branches = subprocess.run("git branch -r", shell=True, capture_output=True, text=True).stdout.split('\n')
    for branch in branches:
        if '->' in branch or not branch.strip():
            continue
        branch_name = branch.strip().split('/')[-1]
        new_branch_name = f"{new_repo_name}-{branch_name}"
        subprocess.run(f"git checkout {branch_name}", shell=True)
        subprocess.run(f"git branch -m {new_branch_name}", shell=True)
        subprocess.run(f"git push {target_repo.clone_url.replace('https://', f'https://{TOKEN}@')} {new_branch_name}", shell=True)
        print(f"Renamed and pushed branch {branch_name} to {new_branch_name} in target repository.")

    # Change back to the original directory (no deletion of cloned repo)
    os.chdir('..')

print("Repositories have been processed.")
