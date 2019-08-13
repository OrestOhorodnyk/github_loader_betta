import os
import base64
from github.AuthenticatedUser import AuthenticatedUser
from github.Repository import Repository

a = base64.b64encode(bytes("OrestOhorodnyk:Orest121904!", 'utf-8'))
print(a)
b = base64.b64decode(a).decode('UTF-8').split(":")
print(b)

project_file_extensions = ['py', 'css', 'html', 'Dockerfile', 'db']


def project_files(root):
    file_paths = []
    for root, dirs, files in os.walk(root):
        for f in files:
            file__extention = f.split('.')[-1]
            if file__extention in project_file_extensions:
                file_paths.append(os.path.join(root, f))
    return file_paths


def create_repo(user: AuthenticatedUser, name: str, is_private: bool = False, auto_init: bool = True) -> Repository:
    """
    This function creates new repository for the user
    :param user: repo will be created for the user account
    :param name: repos name
    :param is_private: True if private and False if public
    :param auto_init: if True repo will be initiated and README.md file will be added to the master branch
     :return: new Repository obj
    """
    return user.create_repo(name=name, private=is_private, auto_init=auto_init)


def login_to_github():
    pass


def load_project_to_repo(repo: Repository, branch: str = 'master'):
    for file_path in project_files(os.getcwd()):
        if file_path == '/home/orest/Documents/code_snippets/Python/Flask_Blog/06-Login-Auth/app/site.db':
            continue
        with open(file_path) as f:
            print(file_path)
            content = f.read()
        repo_path = file_path.split('Flask_Blog/06-Login-Auth')[-1]
        repo.create_file(path=repo_path[1:], message="initial_commit", content=content, branch=branch)


# for i in project_tree(os.getcwd()):
#     print(i)
# for p in project_files(os.getcwd()):
#     print(p.split('Flask_Blog/06-Login-Auth')[-1])

# load_project_to_repo()