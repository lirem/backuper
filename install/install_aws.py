import os
from termcolor import colored

if os.path.isfile("~/.aws/credentials"):
    print(colored("AWS CLI is configured", "green"))
else:
    os.system("aws configure")