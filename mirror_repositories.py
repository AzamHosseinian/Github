from github import Github
import subprocess
import os
import shutil

# Configuration
GITHUB_URL = 'https://your-github-enterprise-url/api/v3'
TOKEN = 'your_github_token'
SOURCE_ORG = 'source_organization_name'
TARGET_ORG = 'target_organization_name'

# Connect to GitHub
g = Github(base_url=GITHUB_URL, login_or_token=TOKEN)

# Get the source organization
source_org = g.get_organization(SOURCE_ORG)

# Get the target organization
try:
    target_org = g.get_organization(TARGET_ORG)
except Exception as e:
    print(f"Failed to find or create target organization: {e}")
    exit(1)

# Loop through all repositories in the source organization
for repo in source_org.get_repos():
    new_repo_name = repo.name
    clone_url = repo.clone_url.replace('https://', f'https://{TOKEN}@')
    exists = any(r.name == new_repo_name for r in target_org.get_repos())

    if exists:
        print(f"Repository {new_repo_name} already exists in {TARGET_ORG}.")
    else:
        print(f"Creating and mirroring repository {new_repo_name}...")
        new_repo = target_org.create_repo(new_repo_name)
        
        try:
            # Clone the repository
            clone_command = f"git clone {clone_url}"
            print(f"Running clone command: {clone_command}")
            result = subprocess.run(clone_command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error cloning repository {new_repo_name}: {result.stderr}")
                continue
            print(f"Cloned {new_repo_name} successfully.")

            # Change directory to the cloned repo
            os.chdir(f"{new_repo_name}")
            
            # Get the list of branches
            result = subprocess.run("git branch -r", shell=True, capture_output=True, text=True)
            branches = [line.strip() for line in result.stdout.split("\n") if line.strip()]
            print(f"Branches in {new_repo_name}: {branches}")
            
            # Rename and push branches
            for branch in branches:
                branch_name = branch.split('/')[-1]
                new_branch_name = f"{new_repo_name}-{branch_name}"
                
                # Checkout the branch
                checkout_command = f"git checkout {branch_name}"
                print(f"Running checkout command: {checkout_command}")
                result = subprocess.run(checkout_command, shell=True, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Error checking out branch {branch_name}: {result.stderr}")
                    continue
                
                # Rename the branch
                rename_command = f"git branch -m {branch_name} {new_branch_name}"
                print(f"Running rename command: {rename_command}")
                result = subprocess.run(rename_command, shell=True, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Error renaming branch {branch_name} to {new_branch_name}: {result.stderr}")
                    continue
                
                # Push the renamed branch to the new repository
                push_command = f"git push {new_repo.clone_url.replace('https://', f'https://{TOKEN}@')} {new_branch_name}"
                print(f"Running push command: {push_command}")
                result = subprocess.run(push_command, shell=True, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Error pushing branch {new_branch_name}: {result.stderr}")
                    continue
                print(f"Pushed branch {new_branch_name} successfully.")
            
            # Change back to the original directory
            os.chdir('..')
            
            # Remove the cloned repository to clean up
            shutil.rmtree(f"{new_repo_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error during cloning or pushing repository {new_repo_name}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
