from imports import os, time
import subprocess

ONE_DAY = 15
def commit_and_push():
    while True:
        p = subprocess.Popen(['./testing_commits_add'], 
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate(input='apinanyogaratnam\n' + os.environ['GIT_PASSWORD'] + '\n')
        time.sleep(ONE_DAY)

        p = subprocess.Popen(['./testing_commits_remove'], 
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate(input='apinanyogaratnam\n' + os.environ['GIT_PASSWORD'] + '\n')
        time.sleep(ONE_DAY)
