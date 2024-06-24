# GitLab Project User Manager

This project provides a GUI tool for managing users in multiple GitLab projects. You can add or remove users from selected projects with specified access levels.

## Features

- Authenticate with GitLab using a personal access token.
- Select one or multiple projects to manage.
- Add users to projects with specified access levels.
- Remove users from projects.
- Select all projects with a single button click.

## Prerequisites

- Python 3.x
- GitLab Python API (`python-gitlab`)
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bake1912/gitlab_management.git
    ```

2. Install the required Python packages:

    ```bash
    pip install python-gitlab
    ```

## Configuration

Update the `TOKEN`, `PROJECTS`, and `USERS` dictionaries in the script with your actual GitLab personal access token, project IDs, and user IDs.

Example configuration:

```python
GITLAB_URL = "https://gitlab.com"
TOKEN = "your_personal_access_token_here"
PROJECTS = {
    "project_1": "your_project_id_1",
    "project_2": "your_project_id_2",
    # Add more projects as needed
}
USERS = {
    "user_1": "user_id_1",
    "user_2": "user_id_2",
    # Add more users as needed
}
