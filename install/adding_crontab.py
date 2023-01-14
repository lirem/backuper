import os
from termcolor import colored
#Writed in python because later I'll add backup frequency customization

try:
    os.system("crontab -l > cron_for_backuper")
    os.system("export python3location=`whereis python3 | cut -d' ' -f2`; export pwd_to_folder=`pwd`; export \
        pwd_to_script=''$pwd_to_folder'/backup.py'; echo @hourly $python3location \
        $pwd_to_script >> cron_for_backuper; crontab cron_for_backuper; rm cron_for_backuper \
        ")
except:
    print(colored("\nSomething went wrong, while adding crontab\n", "red"))
else:
    print(colored("\nBackuper was successfully sheduled, backuper will executed every one hour\n", "green"))