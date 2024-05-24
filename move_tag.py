from github import Github
import subprocess
import os

# Configuration
GITHUB_URL = 'https://your-github-enterprise-url/api/v3'
TOKEN = 'your_personal_access_token'
SOURCE_ORG = 'your_source_organization'
TARGET_ORG = 'your_target_organization'
TARGET_REPO_NAME = 'your_target_repository'

# Repository and tags to be processed
repo_tags = {
    'Repo1': ['tag1'],
    'Repo2': ['tag2', 'tag3', 'tag4', 'tag5']
}

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source and target organizations
source_org = g.get_organization(SOURCE_ORG)
target_org = g.get_organization(TARGET_ORG)
target_repo = target_org.get_repo(TARGET_REPO_NAME)

# Process each repository and its tags
for repo_name, tags in repo_tags.items():
    repo = source_org.get_repo(repo_name)
    clone_url = repo.clone_url.replace('https://', f'https://{TOKEN}@')
    repo_path = os.path.join(os.getcwd(), repo_name)

    # Ensure the directory is clean before cloning (handled manually)
    # if os.path.exists(repo_path):
    #     shutil.rmtree(repo_path)

    print(f"Cloning repository {repo_name}...")
    subprocess.run(f"git clone {clone_url}", shell=True)
    os.chdir(repo_path)

    # Fetch all tags
    subprocess.run("git fetch --tags", shell=True)

    # Process each tag
    for tag_name in tags:
        new_tag_name = f"{repo_name}-{tag_name}"

        # Create a new tag with the new name
        subprocess.run(f"git tag {new_tag_name} {tag_name}", shell=True)

        # Push the new tag to the target repository
        subprocess.run(f"git push {target_repo.clone_url.replace('https://', f'https://{TOKEN}@')} {new_tag_name}", shell=True)
        print(f"Pushed tag {new_tag_name} to repository {TARGET_REPO_NAME}.")

    os.chdir('..')  # Move back to the original directory

print("All specified tags have been processed.")
