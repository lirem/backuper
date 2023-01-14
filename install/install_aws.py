import os
from termcolor import colored
from pathlib import Path


def aws_configure():
    home_dir = str(Path.home())
    if os.path.isfile(f"{home_dir}/.aws/credentials"):
        print(colored("\nAWS CLI credentials is configured", "green"))
    else:
        print(colored("\nPlease configure your AWS credentials, you can find guide on my github page", "yellow"))
        os.system("aws configure")

aws_configure()