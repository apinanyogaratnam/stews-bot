import os
from dotenv import load_dotenv

# load env variables
load_dotenv()


def main():
    # when in sub dir:
    os.chdir('..')
    import subprocess
    commit_message = "testing out commit using subprocess (1)"
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
    token = os.environ['TOKEN']
    username = "apinanyogaratnam"
    repo_name = "automate_git"
    subprocess.call(['git', 'push', 'https://{}@github.com/{}/{}.git'.format(token, username, repo_name)])


if __name__ == '__main__':
    # main()
    main()
