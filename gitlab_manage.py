import tkinter as tk
from tkinter import messagebox
import gitlab_manage

# Configuration
GITLAB_URL = "https://gitlab.com"
TOKEN = "your_personal_access_token_here"
PROJECTS = {
    "project_1": "your_project_id_1",
    "project_2": "your_project_id_2",
    "project_3": "your_project_id_3",
    # Add more projects as needed
}
USERS = {
    "user_1": "user_id_1",
    "user_2": "user_id_2",
    "user_3": "user_id_3",
    # Add more users as needed
}

ACCESS_LEVELS = {
    "Guest": gitlab_manage.GUEST_ACCESS,
    "Reporter": gitlab_manage.REPORTER_ACCESS,
    "Developer": gitlab_manage.DEVELOPER_ACCESS,
    "Maintainer": gitlab_manage.MAINTAINER_ACCESS,
    "Owner": gitlab_manage.OWNER_ACCESS,
}

# Initialize GitLab
gl = gitlab_manage.Gitlab(GITLAB_URL, private_token=TOKEN)

def authenticate(gl):
    """Authenticate with GitLab."""
    try:
        gl.auth()
        messagebox.showinfo("Authentication", "Authentication successful.")
    except Exception as e:
        messagebox.showerror("Authentication", f"Authentication failed: {e}")
        exit(1)

def get_project(gl, project_id):
    try:
        project = gl.projects.get(project_id)
        return project
    except gitlab_manage.GitlabGetError as e:
        messagebox.showerror("Fetch Project", f"Failed to get project: {e}")
        return None

def remove_user_from_project(project, user_id):
    try:
        project.members.delete(user_id)
    except gitlab_manage.GitlabDeleteError as e:
        pass

def add_user_to_project(project, user_id, access_level):
    try:
        project.members.create({"user_id": user_id, "access_level": access_level})
    except gitlab_manage.GitlabCreateError as e:
        pass

def perform_action(action, user_id, access_level=None):
    selected_projects = project_listbox.curselection()
    if not selected_projects:
        messagebox.showerror("Action", "Please select at least one project.")
        return

    for i in selected_projects:
        project_id = list(PROJECTS.values())[i]
        project = get_project(gl, project_id)
        if project:
            if action == "add":
                add_user_to_project(project, user_id, access_level)
            elif action == "remove":
                remove_user_from_project(project, user_id)
    messagebox.showinfo("Action", f"User {action}ed successfully.")

def on_add_user():
    user_id = USERS[user_var.get()]
    access_level = ACCESS_LEVELS[access_var.get()]
    perform_action("add", user_id, access_level)

def on_remove_user():
    user_id = USERS[user_var.get()]
    perform_action("remove", user_id)

def select_all_projects():
    project_listbox.select_set(0, tk.END)

# Authenticate
authenticate(gl)

# Setup GUI
root = tk.Tk()
root.title("GitLab Project User Manager")

tk.Label(root, text="Select User:").grid(row=0, column=0, padx=10, pady=5)
user_var = tk.StringVar(value=list(USERS.keys())[0])
user_menu = tk.OptionMenu(root, user_var, *USERS.keys())
user_menu.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select Access Level:").grid(row=1, column=0, padx=10, pady=5)
access_var = tk.StringVar(value=list(ACCESS_LEVELS.keys())[3])
access_menu = tk.OptionMenu(root, access_var, *ACCESS_LEVELS.keys())
access_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select Project(s):").grid(row=2, column=0, padx=10, pady=5)
project_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10)
for project_name in PROJECTS.keys():
    project_listbox.insert(tk.END, project_name)
project_listbox.grid(row=2, column=1, padx=10, pady=5)

select_all_button = tk.Button(root, text="Select All Projects", command=select_all_projects)
select_all_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

add_button = tk.Button(root, text="Add User", command=on_add_user)
add_button.grid(row=4, column=0, padx=10, pady=20)

remove_button = tk.Button(root, text="Remove User", command=on_remove_user)
remove_button.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()
