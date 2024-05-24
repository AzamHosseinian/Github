
# GitHub Repository Management Scripts

This repository contains several Python scripts for managing GitHub repositories, including cloning, renaming, and migrating repositories and branches. These scripts are designed to work with GitHub Enterprise but can be adapted for use with standard GitHub.

## Prerequisites

- Python 3.x
- `PyGithub` library
- `requests` library
- `urllib3` library

You can install the required libraries using `pip`:

\`\`\`sh
pip install PyGithub requests urllib3
\`\`\`

## Scripts

### 1. `list_repos_with_tags.py`

This script lists all repositories in a specified organization that have tags and writes the repository names and tags to an output file.

#### Configuration

- `GITHUB_URL`: Your GitHub Enterprise URL.
- `TOKEN`: Your GitHub personal access token.
- `SOURCE_ORG`: The name of the source organization.
- `OUTPUT_FILE`: The output file where the repository names and tags will be written.

#### Usage

\`\`\`sh
python list_repos_with_tags.py
\`\`\`

### 2. `mirror_repositories.py`

This script clones repositories from a source organization and mirrors them to a target organization, renaming branches to prevent conflicts.

#### Configuration

- `GITHUB_URL`: Your GitHub Enterprise URL.
- `TOKEN`: Your GitHub personal access token.
- `SOURCE_ORG`: The name of the source organization.
- `TARGET_ORG`: The name of the target organization.
- `TARGET_REPO_NAME`: The name of the target repository.

#### Usage

\`\`\`sh
python mirror_repositories.py
\`\`\`

### 3. `rename_repository.py`

This script renames a specified repository in an organization.

#### Configuration

- `GITHUB_URL`: Your GitHub Enterprise URL.
- `TOKEN`: Your GitHub personal access token.
- `ORG_NAME`: The name of the organization.
- `REPO_NAME`: The name of the repository to rename.
- `NEW_NAME`: The new name for the repository.

#### Usage

\`\`\`sh
python rename_repository.py
\`\`\`

### 4. `repo_tags_processing.py`

This script processes specified repositories and their tags, cloning the repositories, renaming the tags, and pushing them to a target repository.

#### Configuration

- `GITHUB_URL`: Your GitHub Enterprise URL.
- `TOKEN`: Your GitHub personal access token.
- `SOURCE_ORG`: The name of the source organization.
- `TARGET_REPO_NAME`: The name of the target repository.
- `repo_tags`: A dictionary where keys are repository names and values are lists of tags to process.

#### Usage

\`\`\`sh
python repo_tags_processing.py
\`\`\`

### 5. `migrate_repos_to_central.py`

This script clones specified repositories from a source organization and migrates their branches to a central repository in the same organization, avoiding conflicts with existing branches.

#### Configuration

- `GITHUB_URL`: Your GitHub Enterprise URL.
- `TOKEN`: Your GitHub personal access token.
- `SOURCE_ORG`: The name of the source organization.
- `TARGET_REPO_NAME`: The name of the central repository.
- `repo_names`: A list of repository names to process.

#### Usage

\`\`\`sh
python migrate_repos_to_central.py
\`\`\`

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or feedback, please open an issue on GitHub.
