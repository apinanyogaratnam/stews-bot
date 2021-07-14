import time, os


def push(time_to_sleep, filename):
    while True:
        email = os.environ['EMAIL']
        os.system('git config user.email "{}"'.format(email))
        os.system('touch AutoPush/{}'.format(filename))
        os.system('python3 AutoPush/pygithub.py')
        # time.sleep(time_to_sleep)
        os.system('rm AutoPush/{}'.format(filename))
        os.system('python3 AutoPush/pygithub.py')
        time.sleep(time_to_sleep)
