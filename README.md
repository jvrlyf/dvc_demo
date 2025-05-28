# ✨ **Project README: Git and DVC for Code and Data Versioning** ✨


This project focuses on using Git for code versioning and Data Version Control (DVC) for data versioning. It documents tasks completed to understand and implement key commands for managing code and data in a project, highlighting the differences between Git and DVC and their respective workflows.

## Tasks

### 1. Understanding DVC and Git Differences

- **Git**: A distributed version control system primarily used for tracking changes in source code. It manages text-based files (e.g., code, scripts) efficiently and supports branching, merging, and collaboration via repositories (e.g., GitHub).
- **DVC**: Data Version Control, built on top of Git, is designed for managing large datasets and machine learning models. It tracks data files and pipelines, storing references in Git while linking large files to remote storage (e.g., S3, GCS).
- **Key Differences**:

  - Git tracks code; DVC tracks data and models.
  - Git stores file content in its repository; DVC stores data in external storage and tracks metadata in Git.
  - DVC integrates with Git workflows but adds data-specific commands like `dvc push` and `dvc pull`.

### 2. DVC Commands

The following DVC commands were executed as part of the tasks:
- **`dvc init`**:

  - Initializes a DVC project in the current directory.
  - Creates a `.dvc` folder with configuration files and a `.dvcignore` file.
  - Sets up the project to track data and pipelines using DVC alongside Git.
- **`dvc remote add -d <remote_name> <folder_location>`**:

  - Configures a remote storage location (e.g., local folder, S3, GCS) for DVC to store data files.
  - The `-d` flag sets the specified remote as the default.
  - Example: `dvc remote add -d myremote /path/to/storage` links DVC to a local folder.
- **`dvc checkout`**:

  - Restores data files to the workspace from the DVC cache or remote storage.
  - Ensures the workspace matches the tracked data state (similar to Git's checkout for code).
- **`dvc push`**:

  - Uploads tracked data files from the local DVC cache to the configured remote storage.
  - Ensures data is backed up and accessible to collaborators.
- **`dvc pull`**:

  - Downloads data files from the remote storage to the local DVC cache and workspace.
  - Synchronizes the local environment with the remote data state.

### 3. Git Commands

The following Git commands were used for version control:
- **`git init`**:

  - Initializes a new Git repository in the current directory.
  - Creates a `.git` folder to track code changes.
- **`git remote add <name> <github_link>`**:

  - Links the local Git repository to a remote repository (e.g., GitHub).
  - Example: `git remote add origin https://github.com/username/repo.git`.
- **`git status`**:

  - Displays the current state of the working directory and staging area.
  - Shows which files are modified, staged, or untracked.
- **`git add <file>`**:

  - Stages changes in specified files for the next commit.
  - Example: `git add .` stages all modified files.
- **`git checkout <branch_or_commit>`**:

  - Switches branches or restores working directory files to a specific commit.
  - Example: `git checkout main` switches to the main branch.

## Contact
For any questions or collaboration inquiries, feel free to reach out:
- 🔗 **LinkedIn**: **www.linkedin.com/in/rinkugurjar**

- 📧 **Email**: **jvrinku@gmail.com**

## Summary
This project demonstrates the use of Git for code versioning and DVC for data versioning. Git commands (`init`, `remote add`, `status`, `add`, `checkout`) manage code, while DVC commands (`init`, `remote add`, `checkout`, `push`, `pull`) handle data and model versioning. Understanding their differences ensures efficient management of both code and data in a project.