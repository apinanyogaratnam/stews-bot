from imports import os, time

ONE_DAY = 15
def commit_and_push():
    while True:
        os.system("touch random.txt")
        os.system("git add .")
        os.system("git commit -m \"random commit with random.txt file\"")
        os.system("git push -u origin master")
        time.sleep(ONE_DAY)
        os.system("rm random.txt")
        os.system("git add .")
        os.system("git commit -m \"random commit with random.txt file\"")
        os.system("git push -u origin master")
        time.sleep(ONE_DAY)
