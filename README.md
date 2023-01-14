# Tool for making file backups using the AWS S3 service

## Install
Please `cd` to the script folder and run `./install.sh` to install program. <br />
**!!!Important** if you want to backup folder not in your home directory(e.g. system files), please run the install with `sudo`.

### Configuring AWS
Please specify an account credentials which have full access to s3.<br />
If you don't have AWS account please create it using this guide:
[https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) <br />
And create AMI user with full s3 permissions:
[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) ** After creating the user don't close the page and copy credentials to program installer **


## Modifying script
You can free modify scripts for your needs, every block of code is independent and will not affect other.