import sql
import installer
import subprocess
import os

i=sql.get_data()
def chk(x):
    if i[0][0] == x:
       installer.check_present(x)
       os.chdir("bin")
       subprocess.call(['git','clone',i[0][1]])
       print("Installed!")
    else:
        print("Wrong name!\n To view all the apps use the --view flag")

def trend_chk(x,link):
    installer.check_present(x)
    os.chdir("bin")
    subprocess.call(['git','clone',link])
