import os
from dotenv import load_dotenv
import random

# load env variables
load_dotenv()

# list of random words
lst_of_random_words = ['word', 'hi', 'there', 'okayyyy']

# random word
word = random.choice(lst_of_random_words)

def main():
    # when in sub dir:
    # os.chdir('..')
    import subprocess
    commit_message = "{}".format(word)
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
    token = os.environ['GITHUB_TOKEN']
    username = "apinanyogaratnam"
    repo_name = "Stews-Bot"
    subprocess.call(['git', 'push', 'https://{}@github.com/{}/{}.git'.format(token, username, repo_name)])


if __name__ == '__main__':
    main()
