import sql
from get_trending import get_trending_repos
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
parser.add_argument('--trending','-t',action='store_true')
parser.add_argument('--trending_install','-ti')

args=parser.parse_args()

#To view the files
if args.view:
    sql.view()
#To check for program
if args.install is not None:
    check_install.chk(args.install)
if args.trending:
    for i in range(len(get_trending_repos())):
        print(i,")",get_trending_repos()[i]['label'])
if args.trending_install:
    check_install.trend_chk(get_trending_repos()[int(args.trending_install)]['label'],get_trending_repos()[int(args.trending_install)]['link'])
