import sql
import argparse 
import check_install
import check_internet
import requests

print("Checking for internet connection")
if requests.get('https://www.github.com/').status_code != 200:
    print("Some Connection Error\nChecking Internet!")
    if check_internet.is_connected(check_internet.REMOTE_SERVER):
        print("Internet Is Available\nWebsite Is Down")
        exit(1)
print("[+] Connected to internet")

parser = argparse.ArgumentParser()
parser.add_argument('--install', '-i')
parser.add_argument('--view', '-v', action='store_true')
args=parser.parse_args()

#To view the files
if args.view:
    sql.view()
#To check for program
if args.install is not None:
    check_install.chk(args.install)
